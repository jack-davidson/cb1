import json

with open("data/dataset.json") as f:
    chat_data = json.loads(f.read())
    f.close()


def jaccard(a: set[str], b: set[str]) -> float:
    return float(len(a.intersection(b)))/len(a.union(b))


def remove_punctuation(string):
    return string.strip('''!()-[]{};:'"\\,<>./?@#$%^&;*_~''')


def write_string_to_file(string, filepath):
    file = open(filepath, 'a')
    file.write(string + '\n')
    file.close()


def respond_to(query, data):
    if query == "quit":
        exit(1)

    # Save the query so we can write it to a text
    # file it the bot can't understand it
    query = remove_punctuation(query.lower()).split()

    best_response = 0
    for i in range(len(data)):
        keyword = data[i][0].split()
        if jaccard(set(query), set(keyword)) > jaccard(
                set(query), data[best_response][0].split()):
            best_response = i

    if jaccard(set(query), set(data[best_response][0].split())) < 0.2:
        write_string_to_file(str(query), "data/log.txt")
        return "I cannot understand your problem. Transferring you to my superior."

    return data[best_response][1]


print("Type 'quit' To Leave This Conversation")
while True:
    print(respond_to(input("> "), chat_data))

