import nltk


from nltk.tokenize import sent_tokenize


with open("/veld/input/step_0_The_Project_Gutenberg_Etext_Fairy_Tales,_by_the_Grimm_Brothers.txt", "r") as f:
    text = f.read()

text = text.replace("\n", " ")
with open("/veld/output/step_1_The_Project_Gutenberg_Etext_Fairy_Tales,_by_the_Grimm_Brothers.txt", "w") as f:
    f.write(text)

