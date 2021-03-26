import json

with open("data/dataset.json") as f:
    chat_data = json.loads(f.read())
    f.close()


def jaccard(a: set[str], b: set[str]) -> float:
    return float(len(a.intersection(b)))/len(a.union(b))


def remove_punctuation(string):
    punctuation = '''!()-[]{};:'"\\,<>./?@#$%^&;*_~'''
    for mark in punctuation:  # Remove Punctuation
        string = string.replace(mark, '')
    return string


def respond_to(query, data):
    query = remove_punctuation(query.lower()).split()

    suitable_entry = 0
    for i in range(len(data)):
        if jaccard(set(query), set(chat_data[i][0].split())) > jaccard(set(query), set(chat_data[suitable_entry][0].split())):
            suitable_entry = i

    if jaccard(set(query), set(data[suitable_entry][0])) == 0:
        return "I don't know"

    return data[suitable_entry][1]


print(respond_to('how are you doing today?', chat_data))
