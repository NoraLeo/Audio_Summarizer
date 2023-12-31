"""
In this module, I will be analyzing songs, and generating a musical score (maybe at a later part, need to understand how notations like 
bar lines, bars, clefs, notes, etc).
If the song has lyrics, then I will be recognizing the lyrics as well.

Currently, this module analyzes English-language songs (pure english, basically all the words should be found in the English Dictionary (Should I connect to a dictionary?))

Preprocessing stage:
1. Remove noise
2. Remove explicit words/phrases

Analysis Stage:
Line-by-line translation of sung lyrics to text
Summarization of the resultant text (using another API)

Output stage: 
A summary in plain English
"""

from sp_recog import record_audio
from better_profanity import profanity

#Plain text parsers since we are parsing through text
from sumy.parsers.plaintext import PlaintextParser

#for tokenization
from sumy.nlp.tokenizers import Tokenizer

#importing the summarizer
from sumy.summarizers.lsa import LsaSummarizer

"""
TODO: Function to get the transcript of the song
"""
def transcribe(audio_file):
    return record_audio(audio_file)


"""
TODO: Function to filter explicit words

Ways to handle this:
1. Use an profanity filter API to filter such words
2. Connect to a rich database of known offensive words and profanities
3. Use a Python library (like profanity (32 word list), or better_profanity (912 word list))
    https://blog.apilayer.com/how-to-do-profanity-filter-with-pure-python-vs-rest-api/

For now, I will be using better_profanity to aid me in this process.
https://pypi.org/project/better-profanity/

"""
def filter_explicit_words(audio_file):
    transcript = transcribe(audio_file)
    clean_text = profanity.censor(transcript)
    return clean_text

"""
TODO: Function to write the text to a text file
"""
def write_text(audio_file):
    text = filter_explicit_words(audio_file)
    with open("lyrics.txt", "w") as f:
        f.write("%s\n" % text)
    return f

"""
TODO: Function to summarize the clean text
1. Using an API
2. Using a Python library

5 text-summarization techniques
https://www.turing.com/kb/5-powerful-text-summarization-techniques-in-python

I will be using abstract summarization, as I am particular about the structure and presentation of the summary. 
For that, I will be using sumy, a Python library under PyPI projects. I am also suprised that there are many algorithms that \
I can use to summarize my text. I will try using Latent Semantic Analysis algorithm.
"""
def summarization(audio):
    text_original = transcribe(audio)
    text = filter_explicit_words(text_original)
    txt_file = write_text(text)
    parser = PlaintextParser.from_file(txt_file, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document)

    for sentence in summary:
        print(sentence)


