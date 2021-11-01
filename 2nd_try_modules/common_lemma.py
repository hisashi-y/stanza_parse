import json

with open('/home/cl/hisashi-y/stanza_parse/2nd_try_modules/lemma_metaphor_id.json', mode = 'r') as f:
    lemma_metaphor_id = json.load(f)

with open('/home/cl/hisashi-y/stanza_parse/2nd_try_modules/lemma_nonmetaphor_id.json', mode = 'r') as f:
    lemma_nonmetaphor_id = json.load(f)

with open('/home/cl/hisashi-y/stanza_parse/2nd_try_modules/lemma_count.json', mode = 'r') as f:
    lemma_count = json.load(f)

#metaphorとしてもnonメタファーとしても用いられるlemmaの抽出

common_lemma = []
for key in lemma_metaphor_id.keys():
    if key in lemma_nonmetaphor_id.keys():
        common_lemma.append(key)
#print(common_lemma)

common_lemma_counts = {} #これはメタファーとして用いられているカウント
for lemma in common_lemma:
    count = lemma_count[lemma]
    common_lemma_counts[lemma] = count

print(common_lemma_counts)


# with open('lemma_metaphor_id.json', mode = 'wt', encoding = 'utf-8') as f:
#    json.dump(lemma_metaphor_id, f, ensure_ascii = False, indent = 2, cls = SetEncoder )

# with open('lemma_nonmetaphor_id.json', mode = 'wt', encoding = 'utf-8') as f:
#    json.dump(lemma_nonmetaphor_id, f, ensure_ascii = False, indent = 2, cls = SetEncoder )