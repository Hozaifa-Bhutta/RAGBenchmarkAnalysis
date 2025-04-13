import json
import tiktoken
import statistics  

def count_tokens(text):
    enc = tiktoken.get_encoding("o200k_base")
    return len(enc.encode(text))

# List of files to process
# filenames = ["hotpot_train_v1.1.json","hotpot_dev_distractor_v1.json", "hotpot_dev_fullwiki_v1.json", "hotpot_test_fullwiki_v1.json"]
filenames = ["hotpot_train_v1.1.json"]

chunks = set() 
num_queries = 0
queries = set()
for filename in filenames:
    print("\nProcessing:", filename)
    with open(filename, "r") as f:
        data = json.load(f)
        for entry in data:
            num_queries += 1
            queries.add(entry["question"])
            for context in entry["context"]:
                chunk = ""
                for sentence in context[1]:
                    chunk += sentence + " "
                chunks.add(chunk)
    print("Finished processing:", filename)

chunk_sizes = []
for chunk in chunks:
    chunk_sizes.append(count_tokens(chunk))

print("min tokens: ", min(chunk_sizes))
print("max tokens: ", max(chunk_sizes))
print("total_len: ", sum(chunk_sizes))
print("num queries: ", num_queries)
print("num unique queries: ", len(queries))
#  include wikic retrieved chunks
# mention that they use the 5 milllion + wiki chunks
# make documentation that what each document represents 