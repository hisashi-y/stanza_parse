import json
import re

# f = open('/home/cl/hisashi-y/stanza_parse/vua18_verb.tsv')

# datalist = f.readlines()

# dict1 = {}
# dict2 = {}

# count = 0
# for i in datalist:
#     count += 1
#     lst = i.split()
#     if lst[2] == '1':
#         if (lst[0], lst[1]) not in dict1.keys():
#             dict1[(lst[0], lst[1])] = list(lst[-1])
#             dict2[(lst[0], lst[1])] = ' '.join(lst[3:-2])
#         else:
#             dict1[(lst[0], lst[1])].append(lst[-1])
#     if lst[1] == '49':
#         print('this is the', count, 'th line.')
        

# # print(dict1)
# # print(dict2)

# with open('id_sent.json', mode = 'wt', encoding = 'utf-8') as f: #idと文のセットをjsonで書き出し
#    json.dump(dict2, f, ensure_ascii = False, indent = 2 )

# #idとidxのセットもjsonで書き出しておく
# with open('id_idx.json', mode = 'wt', encoding = 'utf-8') as f:
#    json.dump(dict1, f, ensure_ascii = False, indent = 2 )

# dic = {"X": 80, "A": 200, "E": 5, "R": 20, "S": 40}
# print(sorted(dic.items()))

lemma = 'said,'
m = re.match(r'\w+', lemma)
print(m.group())