import re
import random


def answer_prob(usr_message, recog_words, one_response=False, req_words=[]):
    answer_certainty = 0
    has_req_words = True

    for word in usr_message:
        if word in recog_words:
            answer_certainty += 1

    percentage = float(answer_certainty) / float(len(recog_words))

    for word in req_words:
        if word not in usr_message:
            has_req_words = False
            break

    if has_req_words or one_response:
        return int(percentage * 100)
    else:
        return 0


def check_messages(message):
    highest_prob_list = {}

    def responses(bot_response, list_of_words, one_response=False, req_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = answer_prob(message, list_of_words, one_response, req_words)

    responses('Hello,Good to see you!', ['hello', 'hey', 'hi', 'heyo'], one_response=True)
    responses('I am doing fine, and you?', ['how', 'are', 'you', 'doing', 'do', 'you'], req_words=['how', 'are'])
    responses('I am a chatbot created by Hala', ['what', 'are', 'you'],
              req_words=['what', 'you'])
    responses('I cannot eat or drink! I am a chatbot', ['what', 'can', 'you', 'eat'], req_words=['can', 'eat'])
    responses('You\'re welcome', ['thank', 'thanks', 'did', 'great', 'job'], one_response=True)
    responses('If I were you, I would go to the internet and type exactly what you wrote here', ['give', 'advice'],
              req_words=['advice'])
    responses('You can call me X-bot, I\'m X-bot, the assistant of Hala', ['what', 'is', 'your', 'name'],
              req_words=['what', 'name'])
    responses('I am an AI chatbot, so I don\'t have an age. My owner Hala is 20', ['how', 'old', 'are', 'you'],
              req_words=['how', 'old'])
    responses('Talk to you later!', ['goodbye', 'bye', 'see ya'], one_response=True)
    responses('Hala,She is a student at the faculty of computer science, dedicated to honing her skills and leveraging her '
              'education to make a meaningful impact in her chosen field', ['who','creator','creates',],req_words=['creates','creator','who'],one_response=True)
    responses('You can use Google to search for different categories of movies', ['recommend', 'a', 'movie'],
              req_words=['recommend'])
    responses('Sure, Why don\'t scientists trust atoms? Because they make up everything', ['joke', 'tell', 'say'],
              one_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return unknown_message() if highest_prob_list[best_match] < 1 else best_match


def unknown_message():
    response = ["What does that mean?",
                "...", "Could you please re-phrase that?", "I do not understand"][random.randrange(4)]
    return response


def get_response(usr_input):
    split_message = re.split(r'\s+|[,;!?.-]\s*', usr_input.lower())
    response = check_messages(split_message)
    return response


while True:
    print('Bot: ' + get_response(input('You: ')))
