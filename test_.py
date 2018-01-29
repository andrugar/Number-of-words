import number_of_words
import os

def test_file_by_strings():
    with open('test_text.txt', 'w') as in_file:
        in_file.write('Hello, World! My name is Test. James Test.\n'
                   'Am I a simple test func? Yes.')
    correct_out_list = ['Hello, World! My name is Test. James Test.',
                        'Am I a simple test func? Yes.']
    out_list = number_of_words.file_by_strings('test_text.txt')
    os.remove('test_text.txt')
    assert out_list == correct_out_list

def test_list_of_strings_by_sentences():
    in_list = ['Hello, World! My name is Test. James Test.',
               'Am I a simple test func? Yes.'] 
    correct_out_list = [['Hello, World', 'My name is Test', 'James Test.'],
                        ['Am I a simple test func', 'Yes.']]
    out_list = number_of_words.list_of_strings_by_sentences(in_list)
    assert out_list == correct_out_list

def test_list_of_sentences():
    in_list = [['Hello, World', 'My name is Test', 'James Test.'],
               ['Am I a simple test func', 'Yes.']] 
    correct_out_list = ['Hello, World', 'My name is Test', 'James Test.',
                        'Am I a simple test func', 'Yes.']
    out_list = number_of_words.list_of_sentences(in_list)
    assert out_list == correct_out_list

def test_count_words_t_mode():
    in_list = ['Hello, World', 'My name is Test', 'James Test.',
               'Am I a simple test func', 'Yes.']
    correct_out_list = [2, 4, 2, 6, 1]
    out_list = number_of_words.count_words(in_list)
    assert out_list == correct_out_list

def test_count_words_p_mode():
    in_list_of_lists = [['Hello, World', 'My name is Test', 'James Test.'],
                        ['Am I a simple test func', 'Yes.']]
    correct_out_list_of_lists = [[2, 4, 2], [6, 1]]
    out_list_of_lsts = number_of_words.count_words(in_list_of_lists, 'p')
    assert out_list_of_lsts == correct_out_list_of_lists

def test_delete_zeros_t_mode():
    in_list = [2, 0, 4, 2, 0, 0, 6, 1]
    correct_out_list = [2, 4, 2, 6, 1]
    out_list = number_of_words.delete_zeros(in_list)
    assert out_list == correct_out_list

def test_delete_zeros_p_mode():
    in_list = [[2, 0, 4, 2], [0, 0, 6, 1]]
    correct_out_list = [[2, 4, 2], [6, 1]]
    out_list = number_of_words.delete_zeros(in_list, 'p')
    assert out_list == correct_out_list

def test_write_number_of_words_t_mode():
    in_list = [2, 4, 2, 6, 1]
    correct_out_file_as_list = ['There are 2 words in the 1 sentence;\n',
                                'There are 4 words in the 2 sentence;\n',
                                'There are 2 words in the 3 sentence;\n',
                                'There are 6 words in the 4 sentence;\n',
                                'There are 1 words in the 5 sentence;\n']
    number_of_words.write_number_of_words(in_list, 't',
                                          'test_number_of_words.txt')
    with open('test_number_of_words.txt', 'r') as out_file:
        out_file_as_list = [string for string in out_file]
    os.remove('test_number_of_words.txt')
    assert out_file_as_list == correct_out_file_as_list

def test_write_number_of_words_p_mode():
    in_list = [[2, 4, 2], [6, 1]]
    correct_out_file_as_list = ['In the 1 paragraph there are:\n', 
                                '~ 2 words in the 1 sentence;\n',
                                '~ 4 words in the 2 sentence;\n',
                                '~ 2 words in the 3 sentence;\n',
                                'In the 2 paragraph there are:\n',
                                '~ 6 words in the 1 sentence;\n',
                                '~ 1 words in the 2 sentence;\n']
    number_of_words.write_number_of_words(in_list, 'p',
                                          'test_number_of_words.txt')
    with open('test_number_of_words.txt', 'r') as out_file:
        out_file_as_list = [string for string in out_file]
    os.remove('test_number_of_words.txt')
    assert out_file_as_list == correct_out_file_as_list