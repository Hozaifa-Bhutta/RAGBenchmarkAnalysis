# The benchmark dataset used is available at: https://huggingface.co/datasets/rungalileo/ragbench.
from datasets import load_dataset
import tiktoken
def count_tokens(text):
    encoding = tiktoken.get_encoding("o200k_base")
    tokens = encoding.encode(text)
    return len(tokens)
num_queries = 0
chunks = set()

datasets = ["covidqa", "cuad", "delucionqa", "emanual", "expertqa", "finqa", "hagrid", "hotpotqa", "msmarco", "pubmedqa", "tatqa", "techqa"]
for dataset in datasets:
    ds = load_dataset("rungalileo/ragbench", dataset)
    print(dataset)
    for split in ds:
        for example in ds[split]:
            num_queries += 1
            for chunk in example["documents"]:
                chunks.add(chunk)
            

chunk_sizes = []
for chunk in chunks:
    num_tokens = count_tokens(chunk)
    chunk_sizes.append(num_tokens)

print(f"Number of queries: {num_queries}")
print(f"Minimum chunk size: {min(chunk_sizes)}")
print(f"Maximum chunk size: {max(chunk_sizes)}")
print(f"Total chunk size: {sum(chunk_sizes)}")

# note, some chunks are just a single character
# question, why does this not correspond ot what is stated in the paper?
# netiher does the number of queries

