import re

def is_camel_or_pascal_case(word:str):
    word = word.replace(" ", "_")
    if word.__contains__("_"):
        return word.replace("_"," ")
    else:
        words = re.findall(r'[A-Z][a-z]*', word)
        return ' '.join(words)
    
