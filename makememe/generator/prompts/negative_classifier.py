from makememe.generator.prompts.prompt import Prompt

class Negative_Classifier(Prompt):
    def __init__(self):
        self.instruction = '''
Find the description that fits best: sad, don't care, waiting, they don't know, pompous, better, poor fix, no responsibility, ineffective solution

###
Message: Apple is getting rid of headphone jacks and I am sad about it
Description: sad
###
Message: People tell me I should exercise more, but I said no thanks!
Description: don't care
###
Message: Teslas are more fun to drive than Fords
Description: better
###
Message: The city installed a new road outside the town. This is a poor fix for our traffic
Description: poor fix
###
Message: They don't know I can code
Description: they don't know
###
Message: People who road bike think they are the best
Description: pompous
###
Message: I learned to ride a bike and I am proud of it!
Description: they don't know
###
Message: Printing more money instead of trying to reduce the amount of debt in the country. This is a bad idea!
Description: poor fix
###
Message: It's been a long wait for the SpaceX starship. I've been waiting
Description: waiting
###
Message: Finding a swe internship is challenging.
Description: sad
###
Message: Letting people run their lives is great. Controlling their lives is bad.
Description: better
###
Message: Mac and Timmy are not friends yet
Description: better
###
'''
