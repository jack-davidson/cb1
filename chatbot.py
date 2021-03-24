data = [
    ['how are you doing today', 'I am doing well!']
]

def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

def respond_to(query, data):
    query = query.lower()

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&;*_~'''    
    for mark in punctuations: # Remove Punctuations
        query = query.replace(mark, '')

    for entry in data:
        keywords, response = entry
        
        keywords = keywords.split(' ')
        response = response.split(' ')
        query = query.split(' ')

        print(keywords, query, response)

        return jaccard(query, keywords)

print(respond_to('How are you doing today?', data))