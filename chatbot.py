data = [
    ['how are you doing today', 'I am doing well!']
]

def jaccard(a: set[str], b: set[str]) -> float:
    return float(len(a.intersection(b)))/len(a.union(b))

def respond_to(query, data):
    query = query.lower()

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&;*_~'''    
    for mark in punctuations: # Remove Punctuations
        query = query.replace(mark, '')

    for entry in data:
        keywords, response = entry
        
        keywords = set(keywords.split(' '))
        query = set(query.split(' '))

        if jaccard(query, keywords) > 0.5:
            return response

print(respond_to('How are you doing?', data))
