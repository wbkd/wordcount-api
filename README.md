# NLPy

Python Natural Language Processing

## Installation

Requirements:
- Python
- Virtualenv (optional, but recommended)
- Virtualenvwrapper (optional, but recommended)

Run:
```
mkvirtualenv nlpy # optional
pip install -r requirements.txt
```

Copy the JSON and XML files into `data/`. There you will place the pickle files for the [NLTK german classifier](http://dsspace.wzb.eu/nltk_german_classifier_data.pickle.zip) and the [TIGER corpus](http://www.ims.uni-stuttgart.de/forschung/ressourcen/korpora/tiger.html).

You have to convert the extracted TIGER corpus in a `pickle` file as following:
```
python lib/GermaLemma.py data/tigercorpus-2.2.conll09
```

## API Server

Start the HTTP API server running:
```
./server.py
```

Then you can query the API sending a POST request containing a `text` body parameter:
```
curl -X POST -d '{"text": "Testen"}' localhost:5000/api/count/de/ -H 'Content-type: application/json'
```

or

```
curl -X POST -d '{"text": "Test it"}' localhost:5000/api/count/en/ -H 'Content-type: application/json'
```
