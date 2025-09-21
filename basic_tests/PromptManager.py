from basic_tests.PromptExecutor2 import PromptExecutor2
from basic_tests.TechniqueManager import TechniqueManager


class PromptManager:

    def __init__(self, lmHandler, data, response_file):
        self.lmHandler = lmHandler
        self.data = data
        self.response_file = response_file

    def execute(self, config):
        models = self.lmHandler.config["models"]
        technique_manager = TechniqueManager()
        prompt_data = technique_manager.merger(models, self.data)
        PromptExecutor2(prompt_data, self.response_file).execute(config)
