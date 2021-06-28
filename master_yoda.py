# MASTER YODA: Given a sentence, return a sentence with 
# the words reversed

def master_yoda(text):
    wordlist = text.split()
    reversed_word_list = wordlist[::-1]
    return ' '.join(reversed_word_list)
