import json
import stanza

nlp = stanza.Pipeline('en', use_gpu = True)

with open('/home/cl/hisashi-y/stanza_parse/2nd_try_modules/lemma_metaphor_id.json', mode = 'r') as f:
    lemma_metaphor_id = json.load(f)

with open('/home/cl/hisashi-y/stanza_parse/2nd_try_modules/lemma_nonmetaphor_id.json', mode = 'r') as f:
    lemma_nonmetaphor_id = json.load(f)

with open('/home/cl/hisashi-y/stanza_parse/2nd_try_modules/id_sentence.json', mode = 'r') as f:
    id_sentence = json.load(f)

#まずはhaveについてそれぞれ1文ずつ見てみる
metaphor_id = lemma_metaphor_id['show'][1]
nonmetaphor_id = lemma_nonmetaphor_id['show'][1]

metaphor_sentences = id_sentence[metaphor_id]
nonmetaphor_sentences = id_sentence[nonmetaphor_id]

metaphor_sentence = ' '.join(metaphor_sentences[0].split()[1:-2])
# print(metaphor_sentence)

nonmetaphor_sentence = ' '.join(nonmetaphor_sentences[0].split()[1:-2])
# print(nonmetaphor_sentence)

doc1 = nlp(metaphor_sentence)
print('まずはメタファーのshowを含むケース')
print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc1.sentences for word in sent.words], sep='\n')

doc2 = nlp(nonmetaphor_sentence)
print('今度はメタファーではないshowを含むケース')
print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc2.sentences for word in sent.words], sep='\n')

