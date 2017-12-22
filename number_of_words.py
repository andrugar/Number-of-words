"""Return a number of words in every sentence in file

"""

import re
import sys

# Read the name of the file
sys.argv.pop(0)
if len(sys.argv) > 0:
    file = str(sys.argv.pop(0))
else:
    file = str(input('Please enter the name of the file: '))

# Read the file by strings 
strings_in_file = []
with open(file) as ff:
    for string in ff:
        strings_in_file.append(string.strip())

# Delete empty strings
for i in range(strings_in_file.count('')):
    strings_in_file.remove('')

# Divides strings by sentences
strings_by_sentences = []
for string in strings_in_file:
    strings_by_sentences.append(re.split(r'[.!?...]\s', string))

# Create the out_file and write there the answer
with open('Number_of_words.txt', 'w') as out_file:
    for string in strings_by_sentences:
        paragraph_number = int(strings_by_sentences.index(string)) + 1
        out_file.write('In the ' + str(paragraph_number) + 
                       ' paragraph there are:\n')
        for sentence in string:
            sentence_number = string.index(sentence)+1
            words_count = len(re.findall('\w+', sentence))
            out_file.write('- ' + str(words_count) + ' words in the ' + 
                           str(sentence_number) + ' sentence;\n')

print('Done. See file "Number_of_words.txt".')