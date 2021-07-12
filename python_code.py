import re
racial_slurr = ("is", "a","the") # SAMPLE WORDS

tweets = '''The word “profanity” is generally a reference to curse words and it is a word that has many meanings.    
It means using the type of words or language that can be construed as inappropriate, vulgar, insulting, foul, bad 
or dirty – essentially it is the act of cursing or swearing.'''        # SAMPLE Twitter tweets 

for i in tweets.split(". "):                         # LOOPING ON SENTENCES             
   sentence_split = re.findall(r'\w+', i.lower())    # CONVERTING SENTANCE TO LOWER CASE TO AVOID MIS MATCH CASE IN FINDING WORDS IN SENTENCE
   degree_of_profanity = sum(1 for t in sentence_split if t in racial_slurr) / len(sentence_split)   # CALCULATING degree_of_profanity BY DIVIDING TOTAL RACIAL WORDS IN A SENTENCE WITH TOTAL WORDS IN A SENTENCE
   print(degree_of_profanity,sentence_split)        
