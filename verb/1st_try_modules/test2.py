import json

f = open('/home/cl/hisashi-y/stanza_parse/vua18_verb.tsv')

datalist = f.readlines()

sentences = []
n_id = 0
for i in range(len(datalist)):
    lst = datalist[i].split()
    if i == 0:
        sentences.append([n_id, [' '.join(lst[2:])]])
        n_id += 1
    elif lst[3:-2] == datalist[i - 1].split()[3:-2]: #前のやつと同じだった場合
        sentences[-1][-1].append(' '.join(lst[2:]))
    else: #前のやつと違う場合
        sentences.append([n_id, [' '.join(lst[2:])]])
        n_id += 1
with open('id_sentence.json', mode = 'wt', encoding='utf-8') as f:
    json.dump(sentences,  f, ensure_ascii = False, indent = 2)
print(sentences[-1])
