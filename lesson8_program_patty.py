######Fundamentals
######Say something: (input)  until  \end to end the program


# We will need a while loop with an "input", that continue runing until the input = "\end".
# It will print all the phrases, with the first letter capitalized and necessary punctuation.
# Depending on the first word it will define a different punctuation.

#function to convert the phrase into the formated one:
def sentence_maker (phrase):
    interrogatives = ('how', 'what', 'when', 'where', 'why', 'who')     #words that defines questions: how, what, when, where, why
    capitalize = phrase.capitalize()

    if phrase.startswith(interrogatives):
        return f"{capitalize}?"
    else:
        return f"{capitalize}."


phrase_bank = []

#Getting the info from the user:
while True:
    user_phrase = input("Say something: ")
    if user_phrase == "\end":
        break
    else:
        phrase_bank.append(sentence_maker(user_phrase))

print(' '.join(phrase_bank)) #converts lists to strings using the term between ' ' as the separator
    
