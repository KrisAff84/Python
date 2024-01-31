from name_functon import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name('Silas', 'Afflerbaugh')
    assert formatted_name == 'Silas Afflerbaugh'

def test_first_middle_last_name():
    formatted_name = get_formatted_name('Silas', 'Afflerbaugh', 'William')
    assert formatted_name == 'Silas William Afflerbaugh'

def test_two_word_first_name_no_middle():
    formatted_name = get_formatted_name('Cara Ann', 'Afflerbaugh')
    assert formatted_name == 'Cara Ann Afflerbaugh'

def test_two_word_first_name_with_middle():
    formatted_name = get_formatted_name('Cara Ann', 'Afflerbaugh', 'Powers')
    assert formatted_name == 'Cara Ann Powers Afflerbaugh'
