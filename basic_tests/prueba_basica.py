from datetime import datetime

from LmHandler import LmHandler
from PromptReader import PromptReader
from basic_tests.PromptExecutor import PromptExecutor

now_str = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
now_str = now_str.replace(":", "_")
result_file = f"{now_str}_prueba_básica.tsv"

lm_handler = LmHandler(config="D:\\Universidad\\Tesis\\params\\config.json")
#prompts = PromptReader("D:\\Universidad\\Tesis\\datasets\\concode\\dev.json").getPrompts()
prompts = PromptReader("D:\\Universidad\\Tesis\\basic_tests\\dev_recortado.json").getPrompts()
prompt_executor = PromptExecutor(lmHandler=lm_handler, data=prompts, response_file=f"../results/{result_file}")
prompt_executor.execute()
