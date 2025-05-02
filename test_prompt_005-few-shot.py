from datetime import datetime
from PromptTester import PromptTester

now_str = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
now_str = now_str.replace(":", "_")

model_name = "deepseek-r1-distill-qwen-7b"

prefix = "You need to resolve programming problems in Java. When you receive a problem, you have to return the solution."
prefix += "Example 1:\n"
prefix += "Problem:\n"
prefix += "I need a Java method that takes a string containing parentheses, brackets, and braces—for example, '[{()}]'—and determines if they are all correctly balanced. The method should return true if they are balanced and false if they are not.\n"
prefix += "Response:"
prefix += "public static boolean areBracketsBalanced(String input) {\n    Stack<Character> stack = new Stack<>();\n\n    for (char ch : input.toCharArray()) {\n        switch (ch) {\n            case '(': case '[': case '{':\n                stack.push(ch);\n                break;\n            case ')':\n                if (stack.isEmpty() || stack.pop() != '(') return false;\n                break;\n            case ']':\n                if (stack.isEmpty() || stack.pop() != '[') return false;\n                break;\n            case '}':\n                if (stack.isEmpty() || stack.pop() != '{') return false;\n                break;\n        }\n    }\n\n    return stack.isEmpty();}\n"
prefix += "\n"
prefix += "Example 2:\n"
prefix += "Problem:\n"
prefix += "Write a Java method that checks whether a given string is a palindrome. It should return true if the input string is a palindrome and false otherwise.\n"
prefix += "Response:"
prefix += "public static boolean isPalindrome(String input) {\n    String cleaned = input.replaceAll(\"[^a-zA-Z0-9]\", \"\").toLowerCase();\n    int left = 0, right = cleaned.length() - 1;\n    while (left < right) {\n        if (cleaned.charAt(left++) != cleaned.charAt(right--)) {\n            return false;\n        }\n    }\n    return true;\n}\n"
prefix += "\n"
prefix += "Example 3:\n"
prefix += "Problem:\n"
prefix += "Create a Java method that returns the factorial of a given non-negative integer. If the number is 0, return 1.\n"
prefix += "Response:"
prefix += "public static long factorial(int n) {\n    if (n == 0) return 1;\n    long result = 1;\n    for (int i = 1; i <= n; i++) {\n        result *= i;\n    }\n    return result;\n}\n"
prefix += "Please, resolve the following problem:\n"
prefix += "Problem:\n"

append = "\nResponse:"
strategy_code = "few-shot"

baselinePromptTester = PromptTester(model=model_name, language="java", prefix=prefix, append=append,
                                    resultFileName=f"results-test_{now_str}_{model_name}_{strategy_code}.csv")
baselinePromptTester.run()
