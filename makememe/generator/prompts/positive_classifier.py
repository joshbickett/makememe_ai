from makememe.generator.prompts.prompt import Prompt

class Positive_Classifier(Prompt):
    def __init__(self):
        self.instruction = '''
Find the description that fits best: in my opinion, accurate depiction, they don't know, better in comparison, equal in comparison, better and distracting, three levels getting better

###
Message: They don't know I can code
Description: they don't know
###
Message: Tesla is the greatest car company on earth in my opinion
Description: in my opinion
###
Message: I was told that I am a picky person and they couldn't be more accurate
Description: accurate depiction
###
Message: Apple is way better than Android. Don't quote me.
Description: better in comparison
###
Message: I want to start a new project, but I am still working on old ones
Description: better and distracting
###
Message: Posting random memes on Twitter for marketing and long form stories on Linked for marketing are equally good
Description: equal in comparison
###
Message: Going for a run is so great, though some people may feel differently
Description: in my opinion
###
Message: Talking is ok. Reading is great, but coding is the best
Description: three levels getting better
###
Message: Sure remote work is good and meeting up often is great, but working together daily is the best.
Description: three levels getting better
###
Message: Breakfast is an unnecessary meal. Change my mind
Description: in my opinion
###
Message: I had a fortune cookie tell me I code too much and It is so correct
Description: accurate depiction
###
Message: I can't help but listening to the new Daft Punk album and stop listening to Radiohead for now
Description: better and distracting
###
Message: Tea and coffee are equally is good. They both make me happy
Description: equal in comparison
###
Message: Nothing is as cool as learning to code. Reading HTML is cool and learning about computers is ok.
Description: three levels getting better
###
Message: I don't want a Honda, I want a Tesla
Description: better in comparison
###
Message: Humans making memes ok, AI making memes awesome.
Description: better in comparison
###
Message: I don't know if you guys realized I can an write an App in ReactJS while also using the Django framework on the backend
Description: they don't know
###
'''
