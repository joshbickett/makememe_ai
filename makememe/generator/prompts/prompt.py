
# todo: move memes to the DB and load them all into one prompt class as objects
# get rid of individual classes for memes


class Prompt:

    def __init__(self, instruction, description):
        self.instruction = instruction



    def append_example(self, example):
        self.instruction = self.instruction + "Message:" + example + "\n" + "Meme:"