import random
import json

f = open("datasets/concode/dev.json")
lines = f.readlines()
f.close()

minimum_idx = 0
maximum_idx = len(lines)

f_prompts = open("desing_instance_data/design_data_prompts_001.txt", "w")
f_nl = open("desing_instance_data/design_data_response_001.txt", "w")

for i in range(100):
    num = int(random.random() * maximum_idx)
    json_line = json.loads(lines[num])
    f_prompts.write(f"{json_line['code']}\n")
    f_nl.write(f"{json_line['nl']}\n")

f_prompts.close()
f_nl.close()