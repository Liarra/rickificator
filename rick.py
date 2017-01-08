import random

def rickify(text):
    new_text=""
    sentences=break_into_sentences(text)
    for s in sentences:
        s=apply_morty_rule(s)
        s=apply_burp_rule(s)
        new_text=new_text+s+" "
    
    return new_text

def apply_morty_rule(sentence):
    morty_chance=.1
    
    sentence_stoppers=('.','!','?')
    if not sentence.endswith(sentence_stoppers):
        return sentence
        
    dice=random.random()
    if dice<=morty_chance:
        insert_index= next((i for i, ch  in enumerate(sentence) if ch in sentence_stoppers),None)
        new_sentence=sentence[0:insert_index]+", Morty"+sentence[insert_index:]
        return new_sentence
    return sentence
    
def apply_burp_rule(sentence):
    burp_chance=.4
    
    dice=random.random()
    if dice<=burp_chance:
        possible_burp_places=[i for i, ltr in enumerate(sentence) if ltr == ' ']
        if len(possible_burp_places)<2:
            return sentence
        
        try:    
            insert_index=possible_burp_places[random.randint(0,len(possible_burp_places))]
        
        except IndexError:
            print(sentence)
            return sentence
        new_sentence=sentence[0:insert_index]+" *burp*"+sentence[insert_index:]
        return new_sentence
        
    return sentence

def break_into_sentences(text):
    import re
    caps = "([A-Z])"
    prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
    suffixes = "(Inc|Ltd|Jr|Sr|Co)"
    starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites = "[.](com|net|org|io|gov)"
    
    text = " " + text + "  "
    #text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace("...",".")
    text = text.replace("???","?")
    text = text.replace("!!!","!")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences


#print (rickify("How can this even happen to me???"))
content=open("test", 'r').read()
out=open('out','w+')
out.write(rickify(content))
out.close()
