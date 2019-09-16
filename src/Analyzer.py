import re
import sys
from .Tagger import Tagger
from nltk.stem import WordNetLemmatizer
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from germalemma import GermaLemma
from lib import ClassifierBasedGermanTagger
sys.modules["ClassifierBasedGermanTagger"] = ClassifierBasedGermanTagger

class Analyzer():
  def __init__(self, language="english"):
    self.language = language
    self.tagger = Tagger()
    self.stopwords = stopwords.words(language)
    if self.language == "german":
      self.lemmatizer = GermaLemma()
      self.stopwords.append('dass')
    else:
      self.lemmatizer = WordNetLemmatizer()

  def lemmatize(self, word, label):
    if self.language == 'german':
      return self.lemmatizer.find_lemma(word, label)
    else:
      return self.lemmatizer.lemmatize(word)

  def analyse(self, text):
    clean = self.cleanup(text)
    return [
      self.lemmatize(token, label)
      for sentence in self.tokenize(clean)
      for (token, label) in self.tagger.tag(self.remove_stopwords(sentence))
      if not label.startswith("$")
      and len(token) > 1
    ]

  def tokenize(self, text):
    return [
      word_tokenize(sentence)
      for sentence in sent_tokenize(text)
    ]

  def remove_stopwords(self, sentence):
    return [
      token
      for token in sentence
      if token not in self.stopwords
      and token.lower() not in self.stopwords
      and not token.isnumeric()
    ]

  def cleanup(self, text):
    clean = text.replace('"', '').replace("-\r\n", "").replace(' . ', ' ')
    return re.sub(' +',' ', clean)
