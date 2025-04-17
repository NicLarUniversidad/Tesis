from datetime import datetime

from BaselinePromptTester import BaselinePromptTester

now_str = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
now_str = now_str.replace(":", "_")

model_name = "deepseek-r1-distill-qwen-7b"

baselinePromptTester = BaselinePromptTester(model=model_name, language="java", resultFileName=f"results-baseline_{now_str}2_{model_name}.csv")
baselinePromptTester.run()
