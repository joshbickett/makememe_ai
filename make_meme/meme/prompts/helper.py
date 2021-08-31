import textwrap

class Helper:

    @staticmethod
    def wrap(text, width):
        new_text = ''

        wrapper = textwrap.TextWrapper(width=width)
        text = wrapper.wrap(text=text)

        for ii in text[:-1]:
            new_text = new_text + ii + '\n'
        new_text += text[-1]

        return new_text
