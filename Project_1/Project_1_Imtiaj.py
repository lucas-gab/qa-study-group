# 1.	Ask the user to input any sentence
# 2.	It will only stop asking when the user inputs /end
# 3.	When the user inputs /end, we are going to print all of the sentences separated by a blank space
# 4.	If the user types a question, we are going to add a ? to the end of it
# 5.	If the sentence is not a question, we are adding a . to the end of it
# 6.	All sentences have to be captalized

# def sentence_handle(user_input):
#     capitalize_sentence = user_input.capitalize()
#
#     return capitalize_sentence
#
#     print(sentence_handle("i'm not capitalized"))


def sentence_handle(user_input):
    question_tuple = ("who", "when", "where", "why", "how", "what")
    capitalize_sentence = user_input.capitalize()

    if user_input.startswith(question_tuple):
        return f'{capitalize_sentence}?'

    else:
        return f'{capitalize_sentence}.'

print(sentence_handle("why am I not capitalized"))

sentence_list = []
while True:
    user_sentence = input("Say something: ")

    if user_sentence == "end":
        break
    else:
        sentence_list.append(sentence_handle(user_sentence))

print(" ".join(sentence_list)) ##this is how we concatinated all the sentences

