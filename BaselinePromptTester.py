import json
from BasicFileReader import BasicFileReader
from LmHandler import LmHandler
from MetricsCalculator import MetricsCalculator


class BaselinePromptTester(object):

    def __init__(self, model, language, resultFileName, firstPromptId = 0):
        self.model = model
        self.language = language
        self.resultFileName = resultFileName
        self.firstPromptId = firstPromptId
        self.lmHandler = LmHandler()
        self.metricsCalculator = MetricsCalculator()
        fileReader = BasicFileReader("desing_instance_data/design_data_prompts.txt")
        self.prompts = fileReader.promtps
        fileReader = BasicFileReader("desing_instance_data/design_data_response.txt")
        self.responses = fileReader.promtps


    def run(self):
        f = open(self.resultFileName, "w")
        f.write("Prompt-ID\tPrompt\tBaseline\tResult\tCodeResult\tCodeBleuScore\tBleuScore\tExactMatchScore\n")
        for i in range(len(self.prompts)):
            prompt = self.prompts[i]
            prompt += f"\n Write a code in {self.language}"
            baselineResponse = self.responses[i]
            response = self.lmHandler.sendPrompt(prompt, self.model).content
            response = json.loads(response)
            response_content = str(response["choices"][0]["message"]["content"])
            code = response_content.split(f"```java")[1]
            code = code.split(f"```")[0]
            code = code.replace("\n", "").replace("\t", "")
            codeBleuScore = self.metricsCalculator.calc_code_bleu(baselineResponse, code, self.language)
            bleuScore = self.metricsCalculator.calc_bleu(baselineResponse, code)
            exactMatchScore = self.metricsCalculator.calc_exact_match(baselineResponse, code)
            prompt = prompt.replace("\n", "\\n")
            response_content = response_content.replace("\n", "\\n")
            baselineResponse = baselineResponse.replace("\n", "\\n")
            newLine = f"{self.firstPromptId + i}\t{prompt}\t{baselineResponse}\t{response_content}\t{code}\t{codeBleuScore}\t{bleuScore}\t{exactMatchScore}\n"
            f.write(newLine)
        f.close()
