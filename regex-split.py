import re 

text = "apple, banana, oragne, kiwi, grapes,"
pattern = r","

split_result = re.split(pattern, text)
print("Split result", split_result)

