class TechniqueManager:

    def __init__(self):

        self.techniques = [
            # {
            #     "name" : "baseline",
            #     "prompt_prefix" : "You are a Java programmer, just write code on Java and don't make explications.\n",
            #     "prompt_suffix" : "",
            #     "prompt_context" : ""
            # },
            # {
            #     "name" : "context",
            #     "prompt_prefix" : "",
            #     "prompt_suffix" : "",
            #     "prompt_context" : "You are a professional and experienced Java developer with a deep understanding of software engineering principles, design patterns, and enterprise-level application development. You write clean, efficient, and maintainable code, and always follow best practices in architecture, documentation, and testing. You communicate with clarity and precision, using a formal and respectful tone. When helping others, you are thorough, structured, and patient, ensuring every explanation is technically sound and backed by industry standards."
            # },
            # {
            #     "name" : "one-shot",
            #     "prompt_prefix" : "You need to resolve programming problems in Java. When you receive a problem, you have to return the solution. Example:\n Problem:\n this method deletes index files of the @linkplain indexcommit for the specified generation number . \n Response: void function ( Directory arg0 , Collection < SnapshotMetaData > arg1 , long arg2 ) { List < IndexCommit > loc0 = DirectoryReader . listCommits ( arg0 ) ; Map < String , Integer > loc1 = buildRefCounts ( arg1 , loc0 ) ; for ( IndexCommit loc2 : loc0 ) { if ( loc2 . getGeneration ( ) == arg2 ) { deleteIndexFiles ( arg0 , loc1 , loc2 ) ; break ; } } }\n Please, resolve the following problem.:\n Problem:\n",
            #     "prompt_suffix" : "\nResponse:",
            #     "prompt_context" : ""
            # },
            # {
            #     "name" : "few-shot",
            #     "prompt_prefix" : "You need to resolve programming problems in Java. When you receive a problem, you have to return the solution. Example 1:\n Problem:\n check if details are parsed . \n Response: boolean function ( ) { return isParsed ; }\n \n Example 2:\n Problem:\n answer the library file defining the library containing the compilation unit to be indexed or null if the library is not on disk \n Response: File function ( ) { return libraryFile ; }\n \n Example 3:\n Problem:\n this method deletes index files of the @linkplain indexcommit for the specified generation number . \n Response: void function ( Directory arg0 , Collection < SnapshotMetaData > arg1 , long arg2 ) { List < IndexCommit > loc0 = DirectoryReader . listCommits ( arg0 ) ; Map < String , Integer > loc1 = buildRefCounts ( arg1 , loc0 ) ; for ( IndexCommit loc2 : loc0 ) { if ( loc2 . getGeneration ( ) == arg2 ) { deleteIndexFiles ( arg0 , loc1 , loc2 ) ; break ; } } }\n Please, resolve the following problem:\n Problem:\n",
            #     "prompt_suffix" : "\nResponse:",
            #     "prompt_context" : ""
            # },
            # {
            #     "name" : "one-shot-gpt",
            #     "prompt_prefix" : "You need to resolve programming problems in Java. When you receive a problem, you have to return the solution. Example:\n Problem:\n I need a Java method that takes a string containing parentheses, brackets, and braces—for example, '[{()}]'—and determines if they are all correctly balanced. The method should return true if they are balanced and false if they are not.\n Response: public static boolean areBracketsBalanced(String input) {\n    Stack<Character> stack = new Stack<>();\n\n    for (char ch : input.toCharArray()) {\n        switch (ch) {\n            case '(': case '[': case '{':\n                stack.push(ch);\n                break;\n            case ')':\n                if (stack.isEmpty() || stack.pop() != '(') return false;\n                break;\n            case ']':\n                if (stack.isEmpty() || stack.pop() != '[') return false;\n                break;\n            case '}':\n                if (stack.isEmpty() || stack.pop() != '{') return false;\n                break;\n        }\n    }\n\n    return stack.isEmpty();}\n Please, resolve the following problem.:\n Problem:\n",
            #     "prompt_suffix" : "\nResponse:",
            #     "prompt_context" : ""
            # },
            # {
            #     "name" : "few-shot-gpt",
            #     "prompt_prefix" : "You need to resolve programming problems in Java. When you receive a problem, you have to return the solution. Example 1:\n Problem:\n I need a Java method that takes a string containing parentheses, brackets, and braces—for example, '[{()}]'—and determines if they are all correctly balanced. The method should return true if they are balanced and false if they are not.\n Response: public static boolean areBracketsBalanced(String input) {\n    Stack<Character> stack = new Stack<>();\n\n    for (char ch : input.toCharArray()) {\n        switch (ch) {\n            case '(': case '[': case '{':\n                stack.push(ch);\n                break;\n            case ')':\n                if (stack.isEmpty() || stack.pop() != '(') return false;\n                break;\n            case ']':\n                if (stack.isEmpty() || stack.pop() != '[') return false;\n                break;\n            case '}':\n                if (stack.isEmpty() || stack.pop() != '{') return false;\n                break;\n        }\n    }\n\n    return stack.isEmpty();}\n \n Example 2:\n Problem:\n Write a Java method that checks whether a given string is a palindrome. It should return true if the input string is a palindrome and false otherwise.\n Response: public static boolean isPalindrome(String input) {\n    String cleaned = input.replaceAll(\"[^a-zA-Z0-9]\", \"\").toLowerCase();\n    int left = 0, right = cleaned.length() - 1;\n    while (left < right) {\n        if (cleaned.charAt(left++) != cleaned.charAt(right--)) {\n            return false;\n        }\n    }\n    return true;\n}\n \n Example 3:\n Problem:\n Create a Java method that returns the factorial of a given non-negative integer. If the number is 0, return 1.\n Response: public static long factorial(int n) {\n    if (n == 0) return 1;\n    long result = 1;\n    for (int i = 1; i <= n; i++) {\n        result *= i;\n    }\n    return result;\n}\n Please, resolve the following problem:\n Problem:\n",
            #     "prompt_suffix" : "\nResponse:",
            #     "prompt_context" : ""
            # },
            {
                "name" : "one-shot-gpt-with-context",
                "prompt_prefix" : "You need to resolve programming problems in Java. When you receive a problem, you have to return the solution. Example:\n Problem:\n I need a Java method that takes a string containing parentheses, brackets, and braces—for example, '[{()}]'—and determines if they are all correctly balanced. The method should return true if they are balanced and false if they are not.\n Response: public static boolean areBracketsBalanced(String input) {\n    Stack<Character> stack = new Stack<>();\n\n    for (char ch : input.toCharArray()) {\n        switch (ch) {\n            case '(': case '[': case '{':\n                stack.push(ch);\n                break;\n            case ')':\n                if (stack.isEmpty() || stack.pop() != '(') return false;\n                break;\n            case ']':\n                if (stack.isEmpty() || stack.pop() != '[') return false;\n                break;\n            case '}':\n                if (stack.isEmpty() || stack.pop() != '{') return false;\n                break;\n        }\n    }\n\n    return stack.isEmpty();}\n Please, resolve the following problem.:\n Problem:\n",
                "prompt_suffix" : "\nResponse:",
                "prompt_context" : "You are a professional and experienced Java developer with a deep understanding of software engineering principles, design patterns, and enterprise-level application development. You write clean, efficient, and maintainable code, and always follow best practices in architecture, documentation, and testing. You communicate with clarity and precision, using a formal and respectful tone. When helping others, you are thorough, structured, and patient, ensuring every explanation is technically sound and backed by industry standards."
            },
            {
                "name" : "few-shot-gpt-with-context",
                "prompt_prefix" : "You need to resolve programming problems in Java. When you receive a problem, you have to return the solution. Example 1:\n Problem:\n I need a Java method that takes a string containing parentheses, brackets, and braces—for example, '[{()}]'—and determines if they are all correctly balanced. The method should return true if they are balanced and false if they are not.\n Response: public static boolean areBracketsBalanced(String input) {\n    Stack<Character> stack = new Stack<>();\n\n    for (char ch : input.toCharArray()) {\n        switch (ch) {\n            case '(': case '[': case '{':\n                stack.push(ch);\n                break;\n            case ')':\n                if (stack.isEmpty() || stack.pop() != '(') return false;\n                break;\n            case ']':\n                if (stack.isEmpty() || stack.pop() != '[') return false;\n                break;\n            case '}':\n                if (stack.isEmpty() || stack.pop() != '{') return false;\n                break;\n        }\n    }\n\n    return stack.isEmpty();}\n \n Example 2:\n Problem:\n Write a Java method that checks whether a given string is a palindrome. It should return true if the input string is a palindrome and false otherwise.\n Response: public static boolean isPalindrome(String input) {\n    String cleaned = input.replaceAll(\"[^a-zA-Z0-9]\", \"\").toLowerCase();\n    int left = 0, right = cleaned.length() - 1;\n    while (left < right) {\n        if (cleaned.charAt(left++) != cleaned.charAt(right--)) {\n            return false;\n        }\n    }\n    return true;\n}\n \n Example 3:\n Problem:\n Create a Java method that returns the factorial of a given non-negative integer. If the number is 0, return 1.\n Response: public static long factorial(int n) {\n    if (n == 0) return 1;\n    long result = 1;\n    for (int i = 1; i <= n; i++) {\n        result *= i;\n    }\n    return result;\n}\n Please, resolve the following problem:\n Problem:\n",
                "prompt_suffix" : "\nResponse:",
                "prompt_context" : "You are a professional and experienced Java developer with a deep understanding of software engineering principles, design patterns, and enterprise-level application development. You write clean, efficient, and maintainable code, and always follow best practices in architecture, documentation, and testing. You communicate with clarity and precision, using a formal and respectful tone. When helping others, you are thorough, structured, and patient, ensuring every explanation is technically sound and backed by industry standards."
            },
        ]

    def merger(self, models, data):
        models_with_techniques = dict()

        for model in models:
            models_with_techniques[model] = dict()
            for technique in self.techniques:
                upgraded_prompts = []
                i = 0
                for prompt in data["prompts"]:
                    upgraded_prompt = technique["prompt_prefix"] + prompt + technique["prompt_suffix"]
                    context = technique["prompt_context"]
                    nl = data["code"][i]
                    i += 1
                    upgraded_prompts.append({"prompt": upgraded_prompt, "context": context, "nl": nl, "prompt_id": i, "original" : prompt})

                models_with_techniques[model][technique["name"]] = upgraded_prompts
        return models_with_techniques
