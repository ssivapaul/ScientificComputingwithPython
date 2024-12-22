word = "aLongAndComplexString"
newWord =[]
for index, char in enumerate(word):
    if char.isupper():
        char = char.lower()
        converted_char = '_' + char
        newWord.append(converted_char)
    else: newWord.append(char)

converted_char = ''.join(newWord)
print(converted_char)