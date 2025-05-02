from datetime import datetime
from PromptTester import PromptTester

now_str = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
now_str = now_str.replace(":", "_")

model_name = "deepseek-r1-distill-qwen-7b"

prefix = "You need to resolve programming problems in Java. When you receive a problem, you have to return the solution."
prefix += "Example:\n"
prefix += "Problem:\n"
prefix += "I need a Java method that takes a string containing parentheses, brackets, and braces—for example, '[{()}]'—and determines if they are all correctly balanced. The method should return true if they are balanced and false if they are not.\n"
prefix += "Response:"
prefix += "public static boolean areBracketsBalanced(String input) {\n    Stack<Character> stack = new Stack<>();\n\n    for (char ch : input.toCharArray()) {\n        switch (ch) {\n            case '(': case '[': case '{':\n                stack.push(ch);\n                break;\n            case ')':\n                if (stack.isEmpty() || stack.pop() != '(') return false;\n                break;\n            case ']':\n                if (stack.isEmpty() || stack.pop() != '[') return false;\n                break;\n            case '}':\n                if (stack.isEmpty() || stack.pop() != '{') return false;\n                break;\n        }\n    }\n\n    return stack.isEmpty();}\n"
prefix += "Please, resolve the following problem.:\n"
prefix += "Problem:\n"

append = "\nResponse:"
strategy_code = "one-shot"

baselinePromptTester = PromptTester(model=model_name, language="java", prefix=prefix, append=append,
                                    resultFileName=f"results-test_{now_str}_{model_name}_{strategy_code}.csv")
baselinePromptTester.run()
