import random


R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_LIKE = "Thank you, I like you too!S2"
R_WULIKE = "I like your energy and our conversation as well :)!"
R_ANGRY ="Sorry if I made you feel that way :(, I will try hard to be a better bot for you!"
R_NAME = "I don't have a name, I am a bot. But my function is to help you with your question's, or we can just have a simple chat ;)!"
R_GRESP = "I am happy to know that :)! Please ask me more questions!"



def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response

def joke():
    response = ["Did you hear about the mathematician who\'s afraid of negative numbers? He\'ll stop at nothing to avoid them.",
                "Why do we tell actors to break a leg? Because every play has a cast.",
                "Hear about the new restaurant called Karma? There\'s no menu: You get what you deserve.",
                "Did you hear about the claustrophobic astronaut? He just needed a little space.",
                "Why can\'t you explain puns to kleptomaniacs? They always take things literally.",
                "How do you keep a bagel from getting away? Put lox on it.",
                "A man tells his doctor, -Doc, help me. I\'m addicted to Twitter! The doctor replies, -Sorry, I don\'t follow you... ",
                "Why should the number 288 never be mentioned? It\'s two gross.",
                "What did the left eye say to the right eye? Between you and me, something smells.",
                "What do you call a fake noodle? An impasta."
                ][
        random.randrange(10)]
    return response
