import datetime

from BaselinePromptTester import BaselinePromptTester

now_str = str(datetime.time())
now_str = now_str.replace(":", "_")

model_name = "deepseek-coder-33b-instruct"

baselinePromptTester = BaselinePromptTester(model=model_name, language="java", resultFileName=f"results-baseline_{now_str}_{model_name}.csv")
baselinePromptTester.run()
