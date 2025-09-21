import json

from MetricsCalculator import MetricsCalculator


class ResultsMerger:

    def __init__(self, results, result_file):
        self.results = results
        self.result_file = result_file

    def save(self, prompt_count, data):
        #  results -> model | prompt number
        models = self.results.keys()
        metrics_calculator = MetricsCalculator()
        f = open(self.result_file, "w")
        header = "ID\tnl\tcode_original\t"
        #for model in models:
        #    header += f"{model}_response\t{model}_code\t{model}_BLEU\t{model}_CODE_BLEU\t{model}_EM\tparse_success\n"
        header += f"response\tcode\tBLEU\tCODE_BLEU\tEM\tparse_success\tprocessed\tmodel_id\ttechnique\n"
        f.write(header)
        f.close()
        for model in models:
            for i in range(1 , prompt_count + 1):
                index = i - 1
                prompt_result = dict()
                prompt_result["ID"] = i
                prompt_result["nl"] = data["prompts"][index]
                prompt_result["code_original"] = data["code"][index]
                reference = prompt_result["code_original"]
                if i in self.results[model].keys():
                    generation = self.results[model][i].content
                    generation = generation.decode("utf-8")
                    code, success = self.clean_response(generation)
                    generation = generation.replace("\n", "\\n")
                    prompt_result[f"response"] = generation
                    prompt_result[f"code"] = code
                    prompt_result[f"BLEU"] = metrics_calculator.calc_bleu(reference, code)
                    prompt_result[f"CODE_BLEU"] = metrics_calculator.calc_code_bleu_score(reference, code)
                    prompt_result[f"EM"] = metrics_calculator.calc_exact_match(reference, code)
                    prompt_result[f"parse_success"] = success
                    prompt_result[f"processed"] = "True"
                    prompt_result[f"model_id"] = model
                    prompt_result[f"technique"] = "baseline"
                else:
                    prompt_result[f"response"] = ""
                    prompt_result[f"code"] = ""
                    prompt_result[f"BLEU"] = ""
                    prompt_result[f"CODE_BLEU"] = ""
                    prompt_result[f"EM"] = ""
                    prompt_result[f"parse_success"] = ""
                    prompt_result[f"processed"] = "False"
                    prompt_result[f"model_id"] = model
                    prompt_result[f"technique"] = "baseline"
                values = [str(v) for v in prompt_result.values()]
                new_line = "\t".join(values)
                new_line = new_line.encode("cp1252", errors="replace").decode("cp1252")
                f = open(self.result_file, "a")
                f.write(f"{new_line}\n")
                f.close()
        #f.close()


    def clean_response(self, response):
        response = json.loads(response)
        response_content = str(response["choices"][0]["message"]["content"])
        success = True
        try:
            code = response_content.split(f"```java")[1]
            code = code.split(f"```")[0]
        except:
            code = response_content
            success = False
        code = code.replace("\n", "").replace("\t", "")

        return code, success
