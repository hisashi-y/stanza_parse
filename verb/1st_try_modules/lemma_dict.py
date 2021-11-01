import stanza
import json
from collections import OrderedDict

#stanza.download('en')
nlp = stanza.Pipeline('en', use_gpu = True)

id_sentence = []
with open('id_sentence.json', mode = 'r') as f:
    id_sentence = json.load(f)

lemma_count = {}
for sentence in id_sentence[:10]:
    for i in sentence[1]:
        lst = i.split()
        label = int(lst[0])
        idx = int(lst[-1])
        if label == 1:
            doc = nlp(' '.join(lst[1:-2]))
            for sent in doc.sentences:
                for word in sent.words:
                    if word.id == idx + 1:
                        lemma_count.setdefault(word.lemma, 0)
                        lemma_count[word.lemma] += 1

# print(lemma_count)
# with open('lemma_count.json', mode = 'wt', encoding = 'utf-8') as f:
#    json.dump(lemma_count, f, ensure_ascii = False, indent = 2 )

dict = sorted(lemma_count.items(), key = lambda x:x[1])
print('頻度順', dict)

# with open('lemma_count_sorted.json', mode = 'wt', encoding = 'utf-8') as f:
#    json.dump(dict, f, ensure_ascii = False, indent = 2 )