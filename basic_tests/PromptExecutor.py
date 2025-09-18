from basic_tests.ResultsMerger import ResultsMerger


class PromptExecutor:

    def __init__(self, lmHandler, data, response_file):
        self.lmHandler = lmHandler
        self.data = data
        self.response_file = response_file

    def execute(self, system = "You are a Java programmer, just write code in Java and don't make explications"):
        models = self.lmHandler.config["models"]
        system = "You are a Java programmer, just write code on Java and don't make explications."
        responses = dict()
        for model in models:
            line_number = 1
            responses[model] = dict()
            for prompt in self.data["prompts"]:
                response = self.lmHandler.sendPrompt(prompt, model, system)
                responses[model][line_number] = response
                line_number += 1

        ResultsMerger(responses, self.response_file).save(len(self.data["prompts"]), self.data)
