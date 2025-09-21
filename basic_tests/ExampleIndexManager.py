import os

import faiss
import torch
from faiss import write_index, read_index
from transformers import AutoTokenizer, AutoModel

from PromptReader import PromptReader


class ExampleIndexManager:

    def __init__(self):
        self.index_file_name = "/tmp/prompt_examples.index"
        if ( not os.path.exists(self.index_file_name)):
            self.create_index()
        else:
            print("Loading index...")
            index = read_index(self.index_file_name)
            self.index = index



    def create_index(self):
        print("Creating index...")
        model_name = "microsoft/codebert-base"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModel.from_pretrained(model_name)

        data = PromptReader("../datasets/concode/train.json").getPrompts()
        prompts = data["prompts"]

        inputs = tokenizer(prompts, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)
            last_hidden_state = outputs.last_hidden_state

        # ===== Pooling por frase =====
        attention_mask = inputs['attention_mask'].unsqueeze(-1)  # shape: (batch_size, seq_len, 1)
        masked_embeddings = last_hidden_state * attention_mask
        sum_embeddings = masked_embeddings.sum(dim=1)  # sumar por tokens
        num_tokens = attention_mask.sum(dim=1)  # cantidad de tokens por frase
        phrase_embeddings = sum_embeddings / num_tokens  # shape: (batch_size, hidden_size)

        d = phrase_embeddings.shape[1]  # dimension
        nb = phrase_embeddings.shape[0]  # database size
        index = faiss.IndexFlatL2(d)
        index.add(phrase_embeddings)

        write_index(index, self.index_file_name)
        print("Index created...")

        self.index = index

