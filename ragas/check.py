import datasets
import tiktoken
def count_tokens(text):
    encoding = tiktoken.get_encoding("o200k_base")
    return len(encoding.encode(text))
from datasets import load_dataset

dataset = load_dataset("explodinggradients/WikiEval")
print(dataset)
# split is just "train"
split = dataset["train"]
chunks = set()
for entry in split:
    for context in entry["context_v2"]:
        # print(f"Context: {context}")
        chunks.add(context)
chunk_sizes = [count_tokens(chunk) for chunk in chunks]
   
# print total token count, average, min, max, standard deviation
print(f"Num questions: {len(split)}")
print(f"Total tokens: {sum(chunk_sizes)}")
print(f"Min tokens: {min(chunk_sizes)}")
print(f"Max tokens: {max(chunk_sizes)}")


# meniton this was just used to evaluate the framework
# just look at the retrieved documents, topk chunks
# count queries by url * 2
# we have 2.4 million document, mention that
# 256 tokens per doc