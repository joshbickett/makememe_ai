from meme.prompts.prompt import Prompt

class Classifier(Prompt):
    def __init__(self):
        self.instruction = '''
Select from these options: better, not a good idea, cry, they don't know, poor fix

"Apple is getting rid of headphone jacks and I am sad about it"
{"meme-type":"cry"} 
###
"I like coffee, but tea is much better"
{"meme-type":"better"} 
###
"The government prefers to print money and inflate the currency rather than have good discipline"
{"meme-type":"poor fix"} 
###
"I am so proud of my new website that sells dog treats"
{"meme-type":"they don't know"} 
###
"They don't know I started a company"
{"meme-type":"they don't know"} 
###
"Having a dog as a pet is much cooler than having a cat as a pet"
{"meme-type":"better"} 
###
"I'll never get to go to the moon and I wish so much that I could"
{"meme-type":"cry"} 
###
"It's a horrible idea for facebook to use AI in their scrolling technology"
{"meme-type":"not a good idea"} 
###
"Mountain biking is more fun than street biking"
{"meme-type":"better"} 
###
"Buying stuff you do not need is not important"
{"meme-type":"not a good idea"}
###
'''
