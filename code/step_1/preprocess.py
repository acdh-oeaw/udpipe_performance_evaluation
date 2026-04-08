import re

import nltk
from nltk.tokenize import sent_tokenize


with open("/veld/input/step_0_test.txt", "r") as f:
    text = f.read()
text = re.sub(r"\s+", " ", text)
sentence_list = sent_tokenize(text, "german")
text_output = ""
for sentence in sentence_list:
    token_list = nltk.word_tokenize(sentence, "german")
    text_output += "\n"
    for token in token_list:
        text_output += token + "\n"
with open("/veld/output/step_1_test.txt", "w") as f:
    f.write(text_output)

