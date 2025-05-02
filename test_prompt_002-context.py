from datetime import datetime
from PromptTester import PromptTester

now_str = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
now_str = now_str.replace(":", "_")

model_name = "deepseek-r1-distill-qwen-7b"
context = "Context: You are a professional and experienced Java developer with a deep understanding of software engineering principles, design patterns, and enterprise-level application development. You write clean, efficient, and maintainable code, and always follow best practices in architecture, documentation, and testing. You communicate with clarity and precision, using a formal and respectful tone. When helping others, you are thorough, structured, and patient, ensuring every explanation is technically sound and backed by industry standards."
strategy_code = "persona001-programmer-context"

baselinePromptTester = PromptTester(model=model_name, language="java", prefix=context,
                                    resultFileName=f"results-test_{now_str}_{model_name}_{strategy_code}.csv")
baselinePromptTester.run()
