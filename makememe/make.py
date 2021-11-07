import json
# from makememe import Negative_Classifier
from makememe.generator.prompts.negative_classifier import Negative_Classifier
from makememe.generator.prompts.positive_classifier import Positive_Classifier
from makememe.generator.prompts.sentiment_classifier import Sentiment_Classifier
from makememe.generator.prompts.types.positive.better_in_comparison import Better_In_Comparison
from makememe.generator.prompts.types.negative.dont_care import Dont_Care
from makememe.generator.prompts.types.negative.sad import Sad
from makememe.generator.prompts.types.negative.poor_fix import Poor_Fix
from makememe.generator.prompts.types.both.they_dont_know import They_Dont_Know
from makememe.generator.prompts.types.positive.three_levels_getting_better import Three_Levels_Getting_Better
from makememe.generator.prompts.types.negative.waiting import Waiting
from makememe.generator.prompts.types.negative.not_good import Not_Good
from makememe.generator.prompts.types.negative.pompous import Pompous
from makememe.generator.prompts.types.negative.better import Better
from makememe.generator.prompts.types.negative.no_responsibility import No_Responsibility
from makememe.generator.prompts.types.negative.ineffective_solution import Ineffective_Solution
from makememe.generator.prompts.types.positive.in_my_opinion import In_My_Opinion
from makememe.generator.prompts.types.positive.accurate_depiction import Accurate_Depiction
from makememe.generator.prompts.types.positive.equal_in_comparison import Equal_In_Comparison
from makememe.generator.prompts.types.positive.so_good import So_Good
from makememe.generator.prompts.types.positive.better_and_distracting import Better_And_Distracting
from makememe.generator.langauge_models.gpt import GPT
from better_profanity import profanity

def make(description):
    user_input = description.strip()
    if not profanity.contains_profanity(user_input):
        print(f'user_input: {user_input}')
        sentiment_classifier = Sentiment_Classifier()
        sentiment_classifier.append_example(user_input)
        print('________start_________')
        print('________sentiment_classifier_prompt_________')
        print(f'prompt: {sentiment_classifier.instruction}')
        try:
            response = GPT.request(sentiment_classifier.instruction)['choices'][0]['text'].split(":")[1].strip()
            print('________sentiment_classifier_completion_________')
            print(f'response: {response}')
            if response == 'positive':
                classifier = Positive_Classifier()
                classifier.append_example(user_input)
                print('________classifier_prompt_________')
                print(f'prompt: {classifier.instruction}')
                response = GPT.request(classifier.instruction)['choices'][0]['text'].split(":")[1].strip()
                print('________classifier_completion_________')
                print(f'response: {response}')
                meme_description = response
                meme = generate_meme(user_input, meme_description)

            elif response == 'negative':
                classifier = Negative_Classifier()
                classifier.append_example(user_input)
                print('________classifier_prompt_________')
                print(f'prompt: {classifier.instruction}')
                # todo: change all to this format
                response = GPT.request(classifier.instruction)['choices'][0]['text'].split(":")[1].strip()
                print('________classifier_completion_________')
                print(f'response: {response}')
                meme_description = response
                meme = generate_meme(user_input, meme_description)
            else:
                meme = {
                    'meme': 'meme_pics/error.png'
                }
        except Exception as e:
            print(f'error: {e}')
            # flagged = e.args[0].startswith('The content has been flagged')
            # if flagged:
            #     meme = {
            #         'meme': 'meme_pics/flagged.png'
            #     }
            # else:
            meme = {
                'meme': 'meme_pics/error.png'
            }
    else:
        print("Error: Generation Flagged")
        meme = {
            'meme': 'meme_pics/flagged.png'
        }
        
    return meme


def generate_meme(user_input, meme_description):
    print('________meme_prompt_________')
    memes = [They_Dont_Know, Dont_Care, Poor_Fix, Sad, Waiting, Better_In_Comparison, Three_Levels_Getting_Better, Not_Good, Pompous, Better, No_Responsibility, Ineffective_Solution, In_My_Opinion, Accurate_Depiction, Equal_In_Comparison, So_Good, Better_And_Distracting]
    for meme in memes:
        if meme_description == meme.description:
            meme = eval(f'{meme.name}()')
            meme.append_example(user_input)
            print(f'prompt: {meme.instruction}')

            filter_no = GPT.content_filter(meme.instruction)['choices'][0]['text']
            if filter_no == '2':
                raise Exception('The content has been flagged')
            print('________meme_completion_________')
            response = GPT.request(meme.instruction)['choices'][0]['text'].strip()

            print(f'response:{response}')
            response = json.loads(response)
            image_name = meme.create(response)
            file_location = f'creations/{image_name}'
            context = {
                'meme': file_location
            }
            return context
    print("Meme type not found")
    context = {
        'meme': 'meme_pics/error.png'
    }
    return context

