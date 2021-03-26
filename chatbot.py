chat_data = [
    ['how are you doing today', 'I am doing well!'],
    ['are you doing today', 'yes']
]


def jaccard(a: set[str], b: set[str]) -> float:
    return float(len(a.intersection(b)))/len(a.union(b))


def remove_punctuation(string):
    punctuation = '''!()-[]{};:'"\\,<>./?@#$%^&;*_~'''
    for mark in punctuation:  # Remove Punctuation
        string = string.replace(mark, '')
    return string


def respond_to(query, data):
    query = query.lower().remove_punctuation(query).split()

    suitable_entry = 0
    for i in range(len(chat_data)):
        if jaccard(set(query), set(chat_data[i][0].split())) > jaccard(set(query), set(chat_data[suitable_entry][0].split())):
            suitable_entry = i

    return data[suitable_entry][1]


print(respond_to('how are you doing today?', chat_data))
