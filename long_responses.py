import random

R_EATING = 'I don\'t like eating anything, since i am a bot :)'

def unknown():
    response = ['Could you please re-phrase that?',
                '...',
                'Sounds about right',
                'What does that mean?'
                '...What?',
                'I don\'t have a response for that'][random.randrange(6)]
    return response