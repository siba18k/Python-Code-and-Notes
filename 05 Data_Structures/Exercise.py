from pprint import pprint  # This will make the output more readable

sentence = "This is a common interview question"
# We can find out how many times each character is repeated using a dictionary
# We can use the characters as the keys and the repetition as the value
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# This function take an iterable and sorts it
char_frequency_sorted = (
    sorted(char_frequency.items(),
           key=lambda kv: kv[1],
           reverse=True))
pprint(char_frequency_sorted[0])
# I have used the index[0] in order to represent the first value which is the highest
