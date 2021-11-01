import json
import stanza

id_sentence = {}

f = open('vua18_noun.tsv')

datalist = f.readlines()

#このやり方だと1行目の凡例が入ってしまっている

for line in datalist:
    lst = line.split()
    id = lst[0] + ' ' + lst[1]
    sentence = ' '.join(lst[2:])
    if id not in id_sentence.keys():
        id_sentence[id] = []
        id_sentence[id].append(sentence)
    else:
        id_sentence[id].append(sentence)

with open('id_sentence_noun.json', mode = 'wt', encoding = 'utf-8') as f:
    json.dump(id_sentence, f, ensure_ascii = False, indent = 2)