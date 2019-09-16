import os
import pickle

class Tagger():
  def __init__(self, path='data', corpus='nltk_german_classifier_data.pickle'):
    filepath = os.path.join(path, corpus)
    with open(filepath, "rb") as f:
      self.tagger = pickle.load(f)

  def tag(self, sentence):
    return [
      (token, supported_pos(label))
      for (token, label) in self.tagger.tag(sentence)
    ]

def supported_pos(pos):
  if pos.startswith("N") or pos.startswith("V") or pos.startswith("ADJ") or pos.startswith("ADV"):
    return pos
  else:
    return "N"
