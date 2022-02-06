
# This program takes a movie script (fetched using script-getter.py in the same directory)
# and gets the amount of times any character mentions another while speaking.
#
# This data will be used for the graph later.

import json

script = open("hp-script.txt", "r").read()

characters = []

# For each line in the script, if the line starts with a character name, add it to the list of characters.
for i in script.splitlines():

    # We assume lines with a ":" are dialogue lines, and everything before the colon is the character name.
    if ":" in i:
        characters.append(
            i.split(":")[0].strip()
        )

# Remove duplicates.
characters = list(set(characters))

# Sanity check in case the parsing system included an entire sentence or something.
characters = list(filter(
    lambda x: len(x) < 20,
    characters
))

# Limiting line. Uncomment to only generate a truncated dataset with the main and first 25 characters.
# characters = characters[:25] + ["Harry", "Hermione", "Ron"]

print("\n".join(characters))

mentions = {}

for i in script.splitlines():

    # Go through each dialogue line and check for any character mentions.
    if ":" in i:
        speaking_character = i.split(":")[0].strip()
        if speaking_character not in characters:
            # If the character is not in the list of characters, skip it.
            # This happens because of the sanity check above.
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