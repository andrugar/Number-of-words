import sys
import os.path
import re

def name_of_file():
    """Read the name of the file
    
    Read the input name of the file. But also can take the name as first 
    command line argument.
    """
    def name_check(my_file):
        if os.path.isfile(my_file):
            return my_file
        else:
            print('Error: No such file. Try to check the spelling.')
            return read_name()
    
    def read_name():
        my_file = str(input('Please enter the name of the file: '))
        return name_check(my_file)
    
    sys.argv.pop(0)
    if len(sys.argv) > 0:
        my_file = str(sys.argv.pop(0))
        return name_check(my_file)
    else:
        return read_name()

def choose_mode():
    """Allows to choose between the two modes
    
    Read the input command to select the mode. But also can take the command 
    as second command line argument.
    """
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

def read_file_by_strings(my_file):
    with open(my_file) as ff:
        for string_from_file in ff:
            yield string_from_file.strip()

def divide_string_by_sentences(string_generator):
    """
    Generator. Return list of sentences from string.
    """
    re_pattern = re.compile(r'[.!?...]\s')
    for unsplitted_string in string_generator:
        yield re_pattern.split(unsplitted_string)

def one_by_one(list_of_sentences_generator, mode='t'):
    """Generator. Return sentence one by one"""
    if mode == 't':
        for list_of_sentences in list_of_sentences_generator:
            for sentence in list_of_sentences:
                yield sentence
    elif mode == 'p':
        string_number = 0
        for list_of_sentences in list_of_sentences_generator:
            string_number += 1
            for sentence in list_of_sentences:
                yield (string_number, sentence)

def count_words(sentences_generator, mode='t'):
    """Generator. Counts the number of words in senetence.
       
    Have 2 modes:
    1) 't'-mode works with string. It returns the number of words in string.
    2) 'p'-mode works with tuples of the form (number, string). It
    returns tuples of the form (number, number of words in string).
    """  
    re_pattern = re.compile('\w+')
    if mode == 't':
        for sentence in sentences_generator:
            yield len(re_pattern.findall(sentence))
    elif mode == 'p':
        for string_number, sentence in sentences_generator:
            yield (string_number, len(re_pattern.findall(sentence)))

def delete_zeros(numbers_generator, mode='t'):
    """Generator. Delete zero elements from sequense.
    
    Have 2 modes:
    1) 't'-mode works with numbers.
    2) 'p'-mode works with tuples of the form (number, number).
    """
    if mode == 't':
        for number in numbers_generator:
            if number:
                yield number
    elif mode == 'p':
        paragraph = 1
        string_count = 1
        for string_number, number in numbers_generator:
            if number:
                if string_count != string_number:
                    paragraph += 1
                    string_count = string_number
                yield (paragraph, number)

def write_number_of_words(in_generator, mode='t',
                          name_of_out_file='Number_of_words.txt'):
    """Create the out_file and write there the answer
    
    Have 2 modes:
    1) 't'-mode write numbers of sentences counted throughout the entire
    text. In-generator should yield numbers.
    2) 'p'-mode write numbers of sentences for each paragraph separately.
    In-generator should yield tuples of the form (number, number).
    """
    with open(name_of_out_file, 'w') as out_file:
        if mode == 't':
            for sentence_count, number in enumerate(in_generator):
                out_file.write(
                    'There are {number_of_words} words in the {sentence_number} '
                    'sentence;\n'.format(
                        number_of_words=number, 
                        sentence_number=sentence_count+1
                        )
                    )
        elif mode == 'p':
            paragraph = 0
            sentence_count = 0
            for paragraph_number, number in in_generator:
                if paragraph != paragraph_number:
                    paragraph = paragraph_number
                    sentence_count = 0
                    out_file.write(
                        'In the {} paragraph there are:'
                        '\n'.format(paragraph_number)
                        )
                sentence_count += 1
                out_file.write(
                    '~ {number_of_words} words in the {sentence_number} '
                    'sentence;\n'.format(
                        number_of_words=number, 
                        sentence_number=sentence_count
                        )
                    )
    print('Done. Look at the file "{}".'.format(name_of_out_file))

def number_of_words():
    """Return a number of words in every sentence in file
    
    Can count sentences throughout the entire text or for each paragraph
    separately.
    You can interact with the program by answering it's questions or by using
    command line arguments. You can give the name of the file you want to
    process as first command line argument. And as the second command line 
    argument you can give the letter 't' or 'p' which will determine the mode 
    of program.
    't'-mode write numbers of sentences counted throughout the entire text.
    'p'-mode write numbers of sentences for each paragraph separately.
    """
    my_file = name_of_file()
    mode = choose_mode()
    strings_in_file = read_file_by_strings(my_file)
    strings_by_sentences = divide_string_by_sentences(strings_in_file)    
    sentences = one_by_one(strings_by_sentences, mode)
    words_count = count_words(sentences, mode)
    words_count_without_z = delete_zeros(words_count, mode)
    write_number_of_words(words_count_without_z, mode)

if __name__ == '__main__':
    
    number_of_words()
    