story_line_1 = "Alex, a boy was walking inside a {noun1}, but during the {adj1} day, Alex was held captive by a few {pluralNoun1}. Alex {verb} and {verb1} for his life. Then, Alex was at the {pluralNoun2} feast. "
story_line_2 = "Angela was in her backyard, and she was {verb2} a {noun1}. But then, she {verb_past1} and got {verb_past2}. During the horroring catastrophe, Angela was {verb1} to the {place1} and Brian the {noun2} was helping her with {noun3}. But then she was too {adj}, and she died."
stryln3 = "Werdna was {verb} by a {noun} and he got {verbPastTense}!!"



import random
type1 = {"noun", "adverb","verb","adjective","person's name","career job","feeling","number", "noun plural", "verb plural", "verb past tense", "place"}

type1 = {
  "noun": "Please enter a noun: ", 
  "adverb": "Dude, gimme an adverb, man, do you have ADHD??? ENTER!!!!!!!",
  "verb" : "Gimme a verb now! What are you, a rock?!",
  "adjective" : "Please give me an adjective"
}


def EggBrinnya(): 
  n= random.choice(type1)
  if n == 'noun':
    print("Enter a noun")
  elif n == "adverb":
    print("Enter an adverb")
  elif n == "verb":
    print("Enter a verb:")
  elif n == "adjective":
    print("Enter an adjective")
  elif n == "person's name":
    print("Give me a person's name:")
  elif n == "career job":
    print("Enter a career job:")


    
## AngelaT ake in a type to ask the user to enter, 
## get the input, return the input
## Example: type = "noun"
## This function prints sth like "Give me a noun"
## And returns what the user enters
## mytype must be one of "noun", "adverb", ... 
def get_input(mytype: str) -> str: 
  # print("Choose one of the following: noun, adverb, verb, adjective, person's name, career job, feeling, number, noun plural, verb plural, verb past tense, place")
  
  print(type1[mytype])
  mytype = input(">")
  return mytype
  






# Alex 
def play_game(): 
  ## Ask Aukangela's function to get a noun from the user, and store
  noun1 = get_input("noun")
  adj1 = get_input("adjective")
  pluralNoun1 = get_input("noun")
  verb = get_input("verb")
  verb1 = get_input("verb")
  pluralNoun2 = get_input("noun")
  # verb2 = get_input("verb")
  # noun1 = get_input("noun")
  # verb_past1 = get_input("verb past tense")
  # verb_past2 = get_input("verb past tense")
  # place1 = get_input("place")
  # noun2 = get_input("noun")
  # noun3 = get_input("noun")



  print(story_line_1.format(noun1=noun1, 
                            adj1=adj1, 
                            pluralNoun1=pluralNoun1, 
                            verb = verb, 
                            verb1=verb1, 
                            pluralNoun2=pluralNoun2))
  # print(story_line_2.format(noun=noun1)) Ellipsis weird!. . . 
  # print(stryln3.format(noun=noun1, adj1=adj1, adj2=adj2)

