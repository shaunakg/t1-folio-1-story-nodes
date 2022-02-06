
# This is a script that will process a book in the format of a .txt file.
# It is made for VCE Algorithmics 3+4 (T1 2022) by Shaunak Gadkari.

# The task is: Design a graphical representation/model of the relationships that exist between major characters
# of your favourite book or movie.
# I chose "The House of Hades" by Rick Riordan.

# Basically, in this book series (Heroes of Olympus by Rick Riordan), the author starts each chapter from a different
# character's perspective. I chose this book specifically because of this, because this writing style makes it easy
# to analyse which character mentions which other characters (and how many times). I am going to use this for the
# weighted graph.

# (I'll explain this better in the written statement.)

# Read the file.
text = open("book-2.txt", "r").read()

import json

def int_to_roman(input):
    """
    Convert an integer to a Roman numeral.
    This code is from https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html.
    """

    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return "".join(result)


roman_numerals = [int_to_roman(x + 1) for x in range(60)]

chapter_lines = []

# If the line starts with a roman numeral, it is a chapter line.
for line in enumerate(text.splitlines()):
    if line[1].strip() in roman_numerals:
        chapter_lines.append(line)

chapters = []

# This basically just splits the text into chapters, since we already know the index of where the chapter
# lines are.
for line in enumerate(chapter_lines):
    chapters.append(
        "\n".join(
            text.splitlines()[chapter_lines[line[0] - 1][0] : chapter_lines[line[0]][0]]
        )
    )

# Since we already have that information, we are taking out the chapter lines from the text.
# This next line is specific to the book. There are 6 lines between the Roman numeral indicting the
# start of the chapter and the character name.
chapters = ["\n".join(c.strip().splitlines()[5:]) for c in chapters]

for i in chapters:
    # Remove chapter if it is empty. I think the first one is sometimes empty probably due to a quirk of the
    # splitting code above. This step just makes it irrelevant.
    if i.strip() == "":
        chapters.remove(i)

# This snippet gets the first line of each chapter, which is the perspective character's name.
# Note: I have also hard-coded some characters since I realised there needs to be at least 10 in the graph
main_characters = [
    "athena",
    "hera",
    "poseidon",
    "zeus",
    "apollo",
    "hermes",
    "artemis",
    "hades",
    "demeter",
    "ares"
]

for i in chapters:
    main_characters.append(i.splitlines()[1].lower())

# Since there are multiple chapters per character we can make it into a set which removes repeated instances.
main_characters = list(set(main_characters))

# Dictionary of dictionaries. This will be formatted like:
# {
#   "Jason": {
#       "Sophia": 78,
#       "Andrew": 12,
#       "David": 14
#   },
#
#   "Sophia": {
#       "Jason": 31,
#       "Andrew": 19,
#       "David": 11
#   },
# }
# Also this will all be in lowercase but it doesn't matter.
mentions_from_character_perspective = {}

for i in chapters:

    # Get the name of the character whose perspective we are looking at.
    perspective = i.splitlines()[1].lower()

    # For each word in the chapter
    for word in i.lower().split():

        # If the word is a main character's name (this is all adjusted for capitalisation and stuff also)
        if word in main_characters:

            # The if-statement is there to show that I know how to exclude when the character is talking about themselves.
            # I am purposely not doing that so that the final graph will have loops in it.
            # if word == perspective:
            #     continue

            # Add it to the dictionary.
            # This next complex block of code just makes sure that the keys that we are adding to the dictionary are
            # valid since it's nested and Python doesn't like it if you try to add a key that doesn't exist.

            if perspective in mentions_from_character_perspective:
                if word in mentions_from_character_perspective[perspective]:
                    # We have already seen this word in this perspective.
                    mentions_from_character_perspective[perspective][word] += 1
                else:
                    # We haven't seen this word in this perspective yet.
                    mentions_from_character_perspective[perspective][word] = 1
            else:
                # We haven't seen this perspective yet (the first run).
                mentions_from_character_perspective[perspective] = {word: 1}

print(json.dumps(mentions_from_character_perspective))
