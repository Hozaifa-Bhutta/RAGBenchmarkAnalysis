# The datasets are available at: https://github.com/stanford-futuredata/ARES
import pandas as pd
import tiktoken
def count(text):
    encoding = tiktoken.get_encoding("o200k_base")
    tokens = encoding.encode(text)
    return len(tokens)
# now read all files in the directory that end with .tsv
chunks = set()
num_queries = 0
files = ["fever_synthetic_queries.tsv", "hotpotqa_synthetic_queries.tsv", "multirc_synthetic_queries.tsv", "nq_labeled_output.tsv", "nq_synthetic_queries.tsv", "record_synthetic_queries.tsv", "wow_synthetic_queries.tsv"]
for filename in files:
    if filename.endswith('.tsv'):
        # read the file
        df = pd.read_csv(filename, sep='\t')
        # print label and shape
        if "document" not in df.columns:
            for index, row in df.iterrows():
                num_queries += 1
                chunks.add(row["Document"])

        else:
            for index, row in df.iterrows():
                num_queries += 1
                chunks.add(row["document"])

chunk_sizes = [count(chunk) for chunk in chunks]
print(f'Number of queries: {num_queries}')
print(f'Number of tokens: {sum(chunk_sizes)}')
print(f"Smallest chunk size: {min(chunk_sizes)}")
print(f"Largest chunk size: {max(chunk_sizes)}")

