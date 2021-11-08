from makememe.generator.prompts.prompt import Prompt

class Sentiment_Classifier(Prompt):
    def __init__(self):
        self.instruction = '''
Two options: Positive or negative 

###
Message: Apple is getting rid of headphone jacks and I am sad about it
sentiment: negative
###
Message: Tesla's new vehicle is so cool
sentiment: positive
###
Message: I am so proud of my new website that sells dog treats
sentiment: positive
###
Message: I like coffee, but tea is much better
sentiment: positive
###
Message: I'll never get to go to the moon and I wish so much that I could
sentiment: negative
######
Message: This is a test
sentiment: negative
###
'''
