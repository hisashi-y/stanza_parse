import json
import stanza
import re

nlp = stanza.Pipeline('en')

with open('/home/cl/hisashi-y/stanza_parse/2nd_try_modules/id_sentence.json', mode = 'r') as f:
    id_sentence = json.load(f)

lemma_count = {}
lemma_metaphor_id = {}
lemma_nonmetaphor_id = {}

for id in id_sentence.keys():
    for sentence in id_sentence[id]:
        label = sentence[0]
        target_word_idx = int(sentence.split()[-1])
        target_word = sentence.split()[target_word_idx + 1] #labelの一文字分indexがずれる
        target_word = re.match(r'\w+', target_word).group()
        doc = nlp(target_word)

        for sentence in doc.sentences:
            for word in sentence.words:
                lemma = word.lemma

        if label == '1': #メタファーとして使われている場合
            lemma_count.setdefault(lemma, 0)
            lemma_count[lemma] += 1 #そのlemmaがメタファーとして用いられた回数を+1する
            if lemma not in lemma_metaphor_id.keys(): #そのlemmaがメタファーとして用いられたことのある文のidを記録
                lemma_metaphor_id[lemma] = set([id]) #dictにそのlemmaがない場合は
            else:
                lemma_metaphor_id[lemma].add(id) #dictにそのlemmaがある場合は、既にあるidに加える形でリスト形式で列挙する
        else:
            if lemma not in lemma_nonmetaphor_id.keys():
                lemma_nonmetaphor_id[lemma] = set([id])
            else:
                lemma_nonmetaphor_id[lemma].add(id)

# dict = sorted(lemma_count.items(), key = lambda x:x[1], reverse=True)
# print('頻度順', dict)

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

# with open('lemma_count_sorted.json', mode = 'wt', encoding = 'utf-8') as f:
#    json.dump(dict, f, ensure_ascii = False, indent = 2 )

with open('lemma_count.json', mode = 'wt', encoding = 'utf-8') as f:
   json.dump(lemma_count, f, ensure_ascii = False, indent = 2 )


# with open('lemma_metaphor_id.json', mode = 'wt', encoding = 'utf-8') as f:
#    json.dump(lemma_metaphor_id, f, ensure_ascii = False, indent = 2, cls = SetEncoder )

# with open('lemma_nonmetaphor_id.json', mode = 'wt', encoding = 'utf-8') as f:
#    json.dump(lemma_nonmetaphor_id, f, ensure_ascii = False, indent = 2, cls = SetEncoder )