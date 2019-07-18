doc_list = ['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?']

keyword = 'car'
response = []
for sentence in doc_list:
    is_contained = False
    word_list = sentence.strip().lower().split()
    print(word_list)
    for word in word_list:
        if keyword.lower() == word.strip(','):
            is_contained = True
    if is_contained == True:
        response.append(doc_list.index(sentence))

print(response)
