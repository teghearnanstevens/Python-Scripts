
import random

def main():
    make_sentence(1, "past")    
    make_sentence(1, "present")
    make_sentence(1, "future") 
    make_sentence(2, "past")   
    make_sentence(2, "present") 
    make_sentence(2, "future")  
     
def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)  # Correctly calling the full prepositional phrase
    
    # Construct the sentence with the prepositional phrase
    sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase}."
    
    print(sentence)

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    return random.choice(words)

def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    return random.choice(nouns)

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    return random.choice(verbs)

def get_preposition():
    
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", 
                    "behind", "below", "beneath", "beside", "between", "beyond", "down", 
                    "during", "except", "for", "from", "in", "inside", "into", "near", 
                    "of", "off", "on", "onto", "outside", "over", "past", "since", "through"]
    
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    preposition = get_preposition()  
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    return f"{preposition} {determiner} {noun}"

main()