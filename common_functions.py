import wikipedia
import nltk

from nltk.corpus import wordnet as wn

import string
import re

# nltk.download("wordnet")

postag_dict={'n':wn.NOUN, 'j':wn.ADJ,'v':wn.VERB, 'RB':wn.ADV}


def extract_word_top_def_from_wordnet(word):
    if word in wn.all_lemma_names():
        syns = wn.synsets(word)
        return [syns[0].definition()]
    else:
        return ['']


def extract_word_deflist_given_POS(word, pos_tag):
    if word in wn.all_lemma_names():
        wn_postag = postag_dict.get(pos_tag)
        return [sense.definition() for sense in wn.synsets(word, wn_postag)]
    else:
        return []

def replace_punctuation_in_text_by_whitespace(text):
    translator = re.compile('[%s]' % re.escape(string.punctuation))
    newtext = translator.sub(' ', text)
    return ' '.join(newtext.split())
    # replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
    # text = text.translate(replace_punctuation)
    # return ' '.join(text.split())


def wiki_definition_concept(concept):
    summary = wikipedia.summary(concept, sentences=1)
    return summary
    # if len(summary) ==0:
    #     print 'len(summary) ==0'
    #     exit(0)
    # sents = nltk.sent_tokenize(summary)
    # return sents[0]
