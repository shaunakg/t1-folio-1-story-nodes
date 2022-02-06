
# This program takes a movie script (fetched using script-getter.py in the same directory)
# and gets the amount of times any character mentions another while speaking.
#
# This data will be used for the graph later.

import json

script = open("hp-script.txt", "r").read()

characters = []

for i in script.splitlines():
    if ":" in i:
        characters.append(
            i.split(":")[0].strip()
        )

characters = list(set(characters))
characters = list(filter(
    lambda x: len(x) < 20,
    characters
))

# Limiting line. Without this, there will be a huge amount of data.
# characters = characters[:25] + ["Harry", "Hermione", "Ron"]

print("\n".join(characters))

mentions = {}

for i in script.splitlines():
    if ":" in i:

        speaking_character = i.split(":")[0].strip()
        if speaking_character not in characters:
            continue

        for j in characters:
            if j in i:
                if speaking_character in mentions:
                    if j in mentions[speaking_character]:
                        mentions[speaking_character][j] += 1
                    else:
                        mentions[speaking_character][j] = 1
                else:
                    mentions[speaking_character] = {j: 1}

print(json.dumps(mentions))