# print date and name of the user

letter = 'Dear <|name|>,\n\t you are selected!\n\t date: <|date|>'

print(letter.replace("<|name|>", "mohit").replace("<|date|>", "22/06/2026"))
