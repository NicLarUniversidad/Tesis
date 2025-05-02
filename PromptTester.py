import json
from BasicFileReader import BasicFileReader
from LmHandler import LmHandler
from MetricsCalculator import MetricsCalculator
from PromptModifier import PromptModifier


class PromptTester(object):

    def __init__(self, model, language, resultFileName, firstPromptId = 0, modifier = "", system = "", prefix="", append=""):
        self.model = model
        self.language = language
        self.resultFileName = f"results/{resultFileName}"
        self.firstPromptId = firstPromptId
        self.lmHandler = LmHandler()
        self.metricsCalculator = MetricsCalculator()
        self.promptModifier = PromptModifier(modifier)
        self.system = system
        fileReader = BasicFileReader("desing_instance_data/design_data_prompts_001.txt")
        self.prompts = fileReader.data
        fileReader = BasicFileReader("desing_instance_data/design_data_response_001.txt")
        self.responses = fileReader.data
        self.prefix = prefix
        self.append = append


    def run(self):
        f = open(self.resultFileName, "w")
        f.write("Prompt-ID\tPrompt\tBaseline\tResult\tCodeResult\tCodeBleuScore\tBleuScore\tExactMatchScore\n")
        for i in range(len(self.prompts)):
            prompt = self.prompts[i]
            prompt += f"\n Write a code in {self.language}"
            prompt = self.promptModifier.applyChanges(prompt)
            prompt = f"{self.prefix}\n\n\n{prompt}\n\n\n{self.append}"
            baselineResponse = self.responses[i]
            response = self.lmHandler.sendPrompt(prompt, self.model, self.system).content
            response = json.loads(response)
            response_content = str(response["choices"][0]["message"]["content"])
            try:
                code = response_content.split(f"```java")[1]
                code = code.split(f"```")[0]
                code = code.replace("\n", "").replace("\t", "")
            except:
                code = response_content
            code = code.replace("\n", "").replace("\t", "")
            codeBleuScore = self.metricsCalculator.calc_code_bleu(baselineResponse, code, self.language)
            bleuScore = self.metricsCalculator.calc_bleu(baselineResponse, code)
            exactMatchScore = self.metricsCalculator.calc_exact_match(baselineResponse, code)
            prompt = prompt.replace("\n", "\\n").replace("\t", "")
            system = self.system.replace("\n", "\\n").replace("\t", "")
            prompt += f"| system: |{system}"
            response_content = response_content.replace("\n", "\\n").replace("\t", "")
            baselineResponse = baselineResponse.replace("\n", "\\n").replace("\t", "")
            newLine = f"{self.firstPromptId + i}\t{prompt}\t{baselineResponse}\t{response_content}\t{code}\t{codeBleuScore}\t{bleuScore}\t{exactMatchScore}\n"
            try:
                f.write(newLine)
            except:
                print(f"Cannot write prompt: {i}")
        f.close()