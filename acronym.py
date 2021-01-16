# acronym generator
phrase = input("Enter your phrase or text: ").upper()
words = phrase.split()
letters = [word[0] for word in words]
print("".join(letters))

