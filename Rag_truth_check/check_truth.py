import json
import tiktoken
import statistics
# load source_info.jsonl as json
def count_tokens(text):
    encoding = tiktoken.get_encoding("o200k_base")
    tokens = encoding.encode(text)
    return len(tokens)
def load_jsonl(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return data
data = load_jsonl('source_info.jsonl')
print(f"Loaded {len(data)} records from source_info.jsonl")


num_questions = 0
chunks = set()
for entry in data:
    if (type(entry["source_info"]) is not dict):
        continue
    if (entry["source_info"].get("question") is not None):
        num_questions += 1
        chunks.add(entry["source_info"]["passages"])

chunk_sizes = []
for chunk in chunks:
    chunk_sizes.append(count_tokens(chunk))        
print(f"Minimum chunk size: {min(chunk_sizes)}")
print(f"Maximum chunk size: {max(chunk_sizes)}")
print(f"Total number of tokens: {sum(chunk_sizes)}")
print(f"Number of questions: {num_questions}")


# only include the question answer data
# if needed, mention that they don't divide the passages into a list