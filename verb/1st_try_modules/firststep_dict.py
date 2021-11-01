import stanza
import json
from collections import OrderedDict


# stanza.download('en')
nlp = stanza.Pipeline('en')

# f = open('/home/cl/hisashi-y/stanza_parse/vua18_verb.tsv')

# datalist = f.readlines()

# #文のidとその中でメタファーとして使われている動詞のidxのdict
# id_idx_dict = {}

# #文のidと文の中身のdict
# dict = {}

# #print(datalist)
# for i in datalist:
#    lst = i.split()
#    if lst[2] == '1':
#       if lst[1] not in id_idx_dict.keys():
#          id_idx_dict[lst[1]] = list(lst[-1])
#          dict[lst[1]] = ' '.join(lst[3:-2])
#       else:
#          id_idx_dict[lst[1]].append(lst[-1])

#print(dict)
#print(id_idx_dict)

# with open('id_sent.json', mode = 'wt', encoding = 'utf-8') as f: #idと文のセットをjsonで書き出し
#    json.dump(dict, f, ensure_ascii = False, indent = 2 )

# #idとidxのセットもjsonで書き出しておく
# with open('id_idx.json', mode = 'wt', encoding = 'utf-8') as f:
#    json.dump(id_idx_dict, f, ensure_ascii = False, indent = 2 )


#for i in dict.keys():
#    doc = nlp(dict[i])
#    print(doc)
#    print(doc.entities)

#メタファーに使われる動詞の頻度をみるために、lemmaと使われた回数のdictを作成

#同一のlemmaによるメタファーの文を見つけるために、lemmaとそれが使われた文のidとのdictを作成
#e.g., {'make': 12, 49, 50}

#負例負例

#doc = nlp(dict['49'])
#print(doc)
doc = nlp('Design: Crossed lines over the toytown tram: City transport could soon be back on the right track, says Jonathan Glancey')
# print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')
for sent in doc.sentences:
    for word in sent.words:
        print(word.id, word.lemma, word.upos)