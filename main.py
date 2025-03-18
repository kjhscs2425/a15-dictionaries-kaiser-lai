text = """
Everyone counts.
Everyone has access to great learning.
Every person's unique talents are valued equally.
Everyone takes responsibility for themselves and their community."""

# Make a dictionary where the keys are characters and the values are the number of times that character appears in the `text` print the dicitonary



char_counts = {}

for char in text:
    if char in char_counts:
        char_counts[char] += 1 
    else:
        char_counts[char] = 1
    
print(char_counts)