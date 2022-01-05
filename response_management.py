from re import split
import numpy as np
import google_searcher2 as gs
import long_responses as long
import warnings
warnings.filterwarnings("ignore")

def get_response(user_input):
    split_message = split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses ------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo', 'hiya', 'heya'], single_response=True)
    response('I don\'t have a name yet!', ['what', 'is', 'your', 'name'], required_words=['what', 'is', 'your','name'])
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how', 'are', 'you'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('I love you too!', ['i', 'love', 'you'], required_words=['i', 'love', 'you'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.joke(), ['tell', 'joke'], required_words=['joke'])
    response(long.R_LIKE, ['i','like', 'you'], required_words=['like', 'you'])
    response(long.R_WULIKE, ['what','do','you','like'],required_words=['what','you','like'])
    response(long.R_ANGRY,['i','am','not','happy'],required_words=['not', 'happy'])
    response(long.R_NAME,['tell','your','name'],required_words=['your','name'])
    response(long.R_GRESP,['i','am','good'], required_words=['i','good'])


    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0