import sys
import os.path
import re

def name_of_file():
    """Read the name of the file
    
       Read the input name of the file. But also can take
       the name as first command line argument"""
    def name_check(file):
        if os.path.isfile(file):
            return file
        else:
            print('Error: No such file. Try to check the spelling.')
            return read_name()
    
    def read_name():
        file = str(input('Please enter the name of the file: '))
        return name_check(file)
    
    sys.argv.pop(0)
    if len(sys.argv) > 0:
        file = str(sys.argv.pop(0))
        return name_check(file)
    else:
        return read_name()

def file_by_strings(file):
    """Read the file by strings without empty strings"""
    with open(file) as ff:
        return [string.strip() for string in ff]

def list_of_strings_by_sentences(list_of_strings):
    """Divide strings by sentences.
       Return [[Sentence, Sentence, ..], [Sentence, ..], ..]"""
    return [re.split(r'[.!?...]\s', string) for string in list_of_strings]

def choose_mode():
    """Allows to choose between the two modes
    
       Read the input command to select the mode. But also can take
       the command as second command line argument"""
    def command_check(decision):
        if decision in ('t', 'p'):
            return decision
        else:
            print('Incorrect command.\n'
                  'You should enter the letter t or p to select mode.')
            return read_command()
    
    def read_command():
        decision = input('(t/p): ')
        return command_check(decision)
    
    if len(sys.argv) > 0:
        decision = str(sys.argv.pop(0))
        return command_check(decision)
    else:
        print('Do you want to count sentences:\n'
          '-throughout the entire text(t)\n'
          'or\n'
          '-for each paragraph separately(p)?')
        return read_command()

def list_of_sentences(list_of_lists_of_sentences):
    """Integrate the list of lists into list"""
    out_list = []
    for list in list_of_lists_of_sentences:
        for sentence in list:
            out_list.append(sentence)
    return out_list

def count_words(list, mode='t'):
    """Counts the number of words in every element of the list.
       
       Have 2 modes:
       1) 't'-mode works with list of sentences. Return a list of 
       numbers.
       2) 'p'-mode works with list of lists of sentences. Return a list of
       lists of numbers."""
       
    if mode == 't':
        return [len(re.findall('\w+', string)) for string in list]
    elif mode == 'p':
        list_of_lists = list
        return [count_words(list) for list in list_of_lists]

def delete_zeros(list, mode='t'):
    """Delete zero elements from sequense
    
       Have 2 modes:
       1) 't'-mode works with list of numbers.
       2) 'p'-mode works with list of lists of numbers."""
    if mode == 't':
        return [i for i in list if i]
    elif mode == 'p':
        list_of_lists = list
        new_list_of_lists = [delete_zeros(list) for list in list_of_lists]
        return delete_zeros(new_list_of_lists)

def write_number_of_words(list, mode='t',
                          name_of_out_file='Number_of_words.txt'):
    """Create the out_file and write there the answer
    
       Have 2 modes:
       1) 't'-mode write numbers of sentences counted throughout the entire
       text. In-list should be the list of numbers.
       2) 'p'-mode write numbers of sentences for each paragraph separately.
       In-list should be the list of lists of numbers."""
    
    def writing(list_of_numbers, out_file, beginning):
        for sentence_count, number in enumerate(list_of_numbers):
            out_file.write(
                '{beginning} {words_count} words in the {sentence_number} '
                'sentence;\n'.format(
                    beginning=beginning,
                    words_count=number, 
                    sentence_number=sentence_count+1
                    )
                )
    
    with open(name_of_out_file, 'w') as out_file:
        if mode == 't':
            writing(list, out_file, beginning='There are')
        elif mode == 'p':
            for paragraph_count, list_of_numbers in enumerate(list):
                out_file.write(
                    'In the {paragraph_number} paragraph there are:\n'.format(
                        paragraph_number=paragraph_count+1)
                        )
                writing(list_of_numbers, out_file, beginning='~')
    print('Done. Look at the file "{}".'.format(name_of_out_file))

def number_of_words():
    """Return a number of words in every sentence in file
    
       Can count sentences throughout the entire text or for each paragraph
       separately."""
    
    file = name_of_file()
    strings_in_file = file_by_strings(file)
    strings_by_sentences = list_of_strings_by_sentences(strings_in_file)
    mode = choose_mode()
    if mode == 't':
        strings_by_sentences = list_of_sentences(strings_by_sentences)
    words_count = count_words(strings_by_sentences, mode)
    words_count = delete_zeros(words_count, mode)
    write_number_of_words(words_count, mode)

if __name__ == '__main__':
    
    number_of_words()