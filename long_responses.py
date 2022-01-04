import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_JOKE = "Sorry, but I don't have a sense of humor:(!"
R_LIKE = "Thank you, I like you too!S2"
R_WULIKE = "I like your energy and our conversation as well :)!"
R_ANGRY ="Sorry if I made you feel that way :(, I will try hard to be a better bot for you!"
R_NAME = "I don't have a name, I am a bot. But my function is to help you with your question's, or we can just have a simple chat ;)!"



def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response