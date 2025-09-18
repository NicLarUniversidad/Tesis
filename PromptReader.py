import json


class PromptReader:

    def __init__(self, file):
        self.file = file

    def getPrompts(self):
        f = open(self.file)
        lines = f.readlines()
        f.close()
        data = dict()
        data["prompts"] = []
        data["code"] = []
        for line in lines:
            json_line = json.loads(line)
            nl = json_line['nl'].split("concode")[0]
            data["prompts"].append(nl)
            data["code"].append(json_line['code'])

        return data