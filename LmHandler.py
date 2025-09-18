import json
import time

import requests


class LmHandler(object):

    def __init__(self, config, url="localhost", port="1234", active_model = None):
        self.url = url
        self.port = port
        f = open(config, 'r')
        content = f.read()
        f.close()
        self.config = json.loads(content)
        self.active_model = active_model

    def getBaseUrl(self):
        baseUrl = f"http://{self.url}:{self.port}"
        return baseUrl

    def getModelListUrl(self):
        baseUrl = self.getBaseUrl()
        modelListUrl = f"{baseUrl}/v1/models"
        return modelListUrl

    def getModelList(self):
        modelListUrl = self.getModelListUrl()
        print(f"Calling to {modelListUrl}")
        page = ''
        while page == '':
            try:
                page = requests.get(modelListUrl)
                break
            except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                time.sleep(5)
                print("Was a nice sleep, now let me continue...")
                continue
        return page.content

    def getPromptUrl(self):
        baseUrl = self.getBaseUrl()
        promptUrl = f"{baseUrl}/v1/chat/completions"
        return promptUrl

    def sendPrompt(self, prompt, model_id, system=""):

        data = {
            "model": model_id,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": 1000
        }
        print(f"Sending prompt {prompt} to {self.getPromptUrl()}")
        promptUrl = self.getPromptUrl()
        response = requests.post(promptUrl, json=data)
        return response

    def sendPromptToAllModels(self, prompt, system=""):
        responses = dict()

        for model in self.config["models"]:
            response = self.sendPrompt(prompt, model, system=system)
            responses[model] = response.json()
