german_dict = {
    'mouth': 'Mund',
    'finger': 'Finger',
    'leg': 'Bein',
    'hand': 'Hand',
    'face': 'Gesicht',
    'nose': 'Nase',
}
while True:
    word = input('Enter a word in English or EXIT: ')
    if word == 'EXIT':
        break
    elif word in german_dict:
        print('Translation:', german_dict[word])
    else:
        print('No match!')
print('Bye!')



