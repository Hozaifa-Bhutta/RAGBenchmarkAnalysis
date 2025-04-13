import json
import tiktoken
def count_tokens(text):
    encoding = tiktoken.get_encoding("o200k_base")
    tokens = encoding.encode(text)
    return len(tokens)

# this code calculates topk tokens
files = ["slice0.json", "slice1.json", "slice2.json", "slice3.json", "slice4.json"]
chunks = set()
queries = set()
for file in files:
    print("Processing file:", file)
    with open(file, 'r') as f:
        data = json.load(f)
        for entry in data:
            for paragraph in entry["paragraphs"]:
                for url in paragraph["validated_urls"]:
                    for chunk in url["topk_chunks"]:
                        chunks.add(chunk["chunk_text"])
                    for query in url["queries"]:
                        queries.add(query["query"])
chunks_sizes = []
for chunk in chunks:
    chunks_sizes.append(count_tokens(chunk))
print("Max chunk size:", max(chunks_sizes))
print("Min chunk size:", min(chunks_sizes))
print(f"total topk tokens: {sum(chunks_sizes)}")
print(f"total number of queries: {len(queries)}")


# code below calculates total source document tokens

# print smallest and largest chunks
url_ids = set() # contains all unique url_ids for each fact
chunks = set()
# finds all unique url_ids
for file in files:
    print("Processing file:", file)
    with open(file, 'r') as f:
        data = json.load(f)
        for entry in data:
            for paragraph in entry["paragraphs"]:
                for url in paragraph["validated_urls"]:
                    url_ids.add(url["url_id"])
# finds all unique url_contents associated with those url_ids
for file in files:
    print("Processing file:", file)
    with open(file, 'r') as f:
        data = json.load(f)
        for entry in data:
            for paragraph in entry["paragraphs"]:
                for url in paragraph["urls"]:
                    if url["id"] in url_ids:
                        chunks.add(url["url_content"])
chunks_sizes = [count_tokens(chunk) for chunk in chunks]
print("Max chunk size:", max(chunks_sizes))
print("Min chunk size:", min(chunks_sizes))
print(f"total source document tokens: {sum(chunks_sizes)}")