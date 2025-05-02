from datetime import datetime
from PromptTester import PromptTester

now_str = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
now_str = now_str.replace(":", "_")

model_name = "deepseek-r1-distill-qwen-7b"

context = "You are an experienced Java software engineer with over 10 years of experience writing clean, well-documented code and following best practices. Your goal is to generate only **a single Java method**, with no additional classes, unnecessary explanations, or comments outside the code. The method must: "
context += "    - Be self-contained.\n"
context += "    - Have a descriptive name.\n"
context += "    - Include a clear `Javadoc` before the method.\n"
context += "    - Follow the standard Java coding style.\n"
context += "    - Do not print or read data unless explicitly stated.\n"

context += "Always respond with only the method code and nothing else."
context += "strategy_code = 'persona001-programmer-context'"
strategy_code = "context001-programmer"

baselinePromptTester = PromptTester(model=model_name, language="java", system=context,
                                    resultFileName=f"results-test_{now_str}_{model_name}_{strategy_code}.csv")
baselinePromptTester.run()
