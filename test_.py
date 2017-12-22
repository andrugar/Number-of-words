import number_of_words

def test_list_of_strings_by_sentences():
    in_list = ['Hello, World! My name is Func. Test Func.',
               'Am I a simple test func? Yes.']
    out_list = number_of_words.list_of_strings_by_sentences(in_list) 
    correct_out_list = [['Hello, World', 'My name is Func', 'Test Func.'],
                        ['Am I a simple test func', 'Yes.']]
    assert out_list == correct_out_list

def test_list_of_sentences():
    in_list = [['Hello, World', 'My name is Func', 'Test Func.'],
               ['Am I a simple test func', 'Yes.']]
    out_list = number_of_words.list_of_sentences(in_list) 
    correct_out_list = ['Hello, World', 'My name is Func', 'Test Func.',
                        'Am I a simple test func', 'Yes.']
    assert out_list == correct_out_list

def test_count_words():
    in_list = ['Hello, World', 'My name is Func', 'Test Func.',
               'Am I a simple test func', 'Yes.']
    out_list = number_of_words.count_words(in_list)
    correct_out_list = [2, 4, 2, 6, 1]
    assert out_list == correct_out_list

def test_count_words_p_mode():
    in_list_of_lists = [['Hello, World', 'My name is Func', 'Test Func.'],
                        ['Am I a simple test func', 'Yes.']]
    out_list_of_lsts = number_of_words.count_words(in_list_of_lists, 'p')
    correct_out_list_of_lists = [[2, 4, 2], [6, 1]]
    assert out_list_of_lsts == correct_out_list_of_lists

def test_delete_zeros():
    in_list = [2, 0, 4, 2, 0, 0, 6, 1]
    out_list = number_of_words.delete_zeros(in_list)
    correct_out_list = [2, 4, 2, 6, 1]
    assert out_list == correct_out_list

def test_delete_zeros_p_mode():
    in_list = [[2, 0, 4, 2], [0, 0, 6, 1]]
    out_list = number_of_words.delete_zeros(in_list, 'p')
    correct_out_list = [[2, 4, 2], [6, 1]]
    assert out_list == correct_out_list