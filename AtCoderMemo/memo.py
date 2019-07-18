doc_list = ['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?']
keyword = 'casino'

response = []
for sentence in doc_list:
    is_contained = False
    word_list = sentence.strip().lower().split()
    print(word_list)
    for word in word_list:
        if word == keyword.lower():
            print("haitta")
            is_contained = True
    print(is_contained)
    if is_contained == True:
        response.append(doc_list.index(sentence))
print(response)
