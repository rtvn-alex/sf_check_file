import string

with open('testfile.txt', encoding='utf8') as f:
    f_text = f.read()

tt = str.maketrans(dict.fromkeys(string.punctuation))
f_list = f_text.translate(tt).lower().split()
print(f_list)

dct = {}
for wrd in f_list:
    if len(wrd) > 3:
        if wrd in dct.keys():
            dct[wrd] += 1
        else:
            dct[wrd] = 1

cnt = 0
freq = ''
for key, value in dct.items():
    if value > cnt:
        freq, cnt = key, value

print(f'The word "{freq}" appears {cnt} times')

eng_words_list = []
length = 0
longest = ''
for wrd in f_list:
    is_eng = True
   # while is_eng:
    for char in wrd:
        if char not in string.ascii_letters:
            is_eng = False
    if is_eng:
        eng_words_list.append(wrd)
for wrd in eng_words_list:
    if len(wrd) > length:
        length = len(wrd)
        longest = wrd

print(f'The longest english word is {longest} - {length} letters!')
