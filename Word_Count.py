import string

# Open the file in read mode 
X = open("test.txt", "r")

# Storing each line in the file as a list item
txt = X.readlines()

# Creating dictionary
Dictionary = dict()

# Splitting line into words
for line in txt:
    line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
 
    for word in words: 
        # Check if the word is already in dictionary 
        if word in Dictionary:
            Dictionary[word] = Dictionary[word] + 1
        else: 
            # Add the word to dictionary with count 1 
            Dictionary[word] = 1
   
for key in list(Dictionary.keys()):
    print(key, ":", Dictionary[key], file=open("result.txt", "a"))

print("____________________", file=open("result.txt", "a"))
