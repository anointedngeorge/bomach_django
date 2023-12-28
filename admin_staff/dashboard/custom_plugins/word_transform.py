import re


def transformWord(word):
    # Use regular expression to add spaces
    formatted_word = re.sub(r'([a-z])([A-Z])', r'\1 \2', word)
    formatted_word = formatted_word[0].upper() + formatted_word[1:]
    return formatted_word