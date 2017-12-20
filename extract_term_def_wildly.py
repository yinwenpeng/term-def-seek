
import wikipedia
import nltk
import codecs
from common_functions import wiki_definition_concept, extract_word_top_def_from_wordnet


def load_concept_vocab(term):
    source = '(wordnet)'
    defi = ''
    defi = extract_word_top_def_from_wordnet(term)[0]
    if len(defi) ==0:
        defi = wiki_definition_concept(term)
        source = '(wikipedia)'
    return defi, source




if __name__ == '__main__':
    # load_concept_vocab()
    defi, s =  load_concept_vocab("Alibaba Group")
    print defi, s
