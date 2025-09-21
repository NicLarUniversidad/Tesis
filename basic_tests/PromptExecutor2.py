import json

from LmHandler import LmHandler
from MetricsCalculator import MetricsCalculator
from basic_tests.ResultFileManager import ResultFileManager


class PromptExecutor2:

    def __init__(self, prompt_data, result_file):
        self.prompt_data = prompt_data
        self.result_file = result_file


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

    def execute(self, config):
        # self.prompt_data [model | technique | prompt ]
        metrics_calculator = MetricsCalculator()
        result_file_manager = ResultFileManager(self.result_file)
        result_file_manager.try_init()
        lm_handler = LmHandler(config)
        for model in self.prompt_data:
            for technique in self.prompt_data[model]:
                for prompt_data in self.prompt_data[model][technique]:
                    prompt_id = prompt_data["prompt_id"]
                    prompt = prompt_data["prompt"]
                    nl = prompt_data["nl"]
                    reference = prompt_data["original"]
                    context = prompt_data["context"]
                    result = dict()
                    result["ID"] = prompt_id
                    result["nl"] = nl
                    result["reference"] = reference
                    generation = lm_handler.sendPrompt(prompt, model, context).content

                    generation = generation.decode("utf-8")
                    code, success = self.clean_response(generation)
                    generation = generation.replace("\n", "\\n")
                    result[f"response"] = generation
                    result[f"code"] = code
                    result[f"BLEU"] = metrics_calculator.calc_bleu(reference, code)
                    result[f"CODE_BLEU"] = metrics_calculator.calc_code_bleu_score(reference, code)
                    result[f"EM"] = metrics_calculator.calc_exact_match(reference, code)
                    result[f"parse_success"] = success
                    result[f"processed"] = "True"
                    result[f"model_id"] = model
                    result[f"technique"] = technique
                    values = [str(v) for v in result.values()]
                    new_line = "\t".join(values)
                    result_file_manager.add(new_line)