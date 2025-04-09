import json

from LmHandler import LmHandler


class LlmHandler(object):

    def __init__(self, llm_code = None):
        self.valid_model = False
        if llm_code is None:
            print("No se cargó el modelo")
        else:
            self.lnHandler = LmHandler()
            modelListStr = self.lnHandler.getModelList()
            self.modelListJson = json.loads(modelListStr)
            for model in self.modelListJson["data"]:
                if model["id"] == llm_code:
                    self.valid_model = True
                    self.model = model
                    self.model_id = model["id"]

    def generate(self, prompt, system=""):
        response = self.lnHandler.sendPrompt(prompt, self.model_id, system)
        return response
