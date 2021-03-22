import re

data = [
    ("^my name is", "Hello,")
]

# Boilerplate
def respond_to(query, data):
    for entry in data:
        regex, replacement = entry

        if re.match(regex, query, re.IGNORECASE):
            response = re.sub(regex, replacement, query, 1, re.IGNORECASE)
            return response

print(respond_to("My name is John Doe", data)) # Hello, John Doe

# This is probably going to be replaced, but it is a proof of concept :) - Rachit Kakkar