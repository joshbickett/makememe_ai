
# todo: rename this class and all prompt types to something else, probably memes?
class Prompt:
    def __init__(self, instruction):
        self.instruction = instruction

    def append_example(self, example):
        self.instruction = self.instruction + '"' + example + '"'
