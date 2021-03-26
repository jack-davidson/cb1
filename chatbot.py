import json

with open("data/dataset.json") as f:
    chat_data = json.loads(f.read())
    f.close()


def jaccard(a: set[str], b: set[str]) -> float:
    return float(len(a.intersection(b)))/len(a.union(b))


def remove_punctuation(string):
    return string.strip('''!()-[]{};:'"\\,<>./?@#$%^&;*_~''')


def respond_to(query, data):
    if query == "bye":
        exit(1)

    query = remove_punctuation(query.lower()).split()

    suitable_entry = 0
    for i in range(len(data)):
        keywords = chat_data[i][0].split()
        if jaccard(set(query), set(keywords)) > jaccard(
                set(query), set(keywords)):
            suitable_entry = i

    if jaccard(set(query), set(data[suitable_entry][0].split())) == 0:
        return "I don't know"

    return data[suitable_entry][1]


while True:
    print(respond_to(input("> "), chat_data))
