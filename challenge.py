'''
Challenge: Write a function that takes a sentence, and
returns the longest even-length word in the sentence. Or
if it has no even-length words, return "00".
'''
def longest_even(text):
    longest = "00"
    for word in text.split():
        if len(word) % 2 == 0 and len(word) >= len(longest):
            longest = word
    return longest

string = "here is text that will spit out the longest even length word"

'''
Challenge: From a list of numbers, move zero to the end of the list.
'''

numbers = [4, 2, 7, 3, 4, 0, 2, 3, 1]
for num in numbers:
    if num == 0: numbers.append(numbers.pop(numbers.index(num)))

print(numbers)