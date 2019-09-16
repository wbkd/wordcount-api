#! /usr/bin/env python

from collections import Counter
from src.Analyzer import Analyzer
from flask import Flask, escape, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

de_analyser = Analyzer(language="german")
en_analyser = Analyzer()

@app.route("/api/count/<lang>/", methods=["POST"])
def home(lang):
  values = request.get_json()
  if lang == 'de':
    words = de_analyser.analyse(values["text"])
  else:
    words = en_analyser.analyse(values["text"])
  word_freq = Counter(words)
  common_words = word_freq.most_common()
  return jsonify(common_words)

if __name__ == "__main__":
  app.run()
