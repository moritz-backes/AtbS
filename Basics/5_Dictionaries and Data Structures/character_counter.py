import pprint
message = 'It was a bright cold day in April, and the clocks where striking thriteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
