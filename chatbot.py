import re

data = [
    ("^my name is", "Hello,")
]

# Boilerplate
def respond_to(query, data):
    for entry in data:
        regex, replacement = entry

        if re.match(regex, query, re.IGNORECASE):
            print("found match")

respond_to("My name is John Doe", data)
