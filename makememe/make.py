import json
from makememe.generator.prompts.types.indifferent import Indifferent
from makememe.generator.prompts.types.sad import Sad
from makememe.generator.prompts.types.poor_fix import Poor_Fix
from makememe.generator.prompts.types.they_dont_know import They_Dont_Know
from makememe.generator.prompts.types.three_levels_increasing import Three_Levels_Increasing
from makememe.generator.prompts.types.waiting import Waiting
from makememe.generator.prompts.types.pompous import Pompous
from makememe.generator.prompts.types.better import Better
from makememe.generator.prompts.types.no_responsibility import No_Responsibility
from makememe.generator.prompts.types.ineffective_solution import Ineffective_Solution
from makememe.generator.prompts.types.in_my_opinion import In_My_Opinion
from makememe.generator.prompts.types.accurate_depiction import Accurate_Depiction
from makememe.generator.prompts.types.equal import Equal
from makememe.generator.prompts.types.distracting import Distracting
from makememe.generator.langauge_models.gpt import GPT
from flask_login import current_user
from makememe.models import Users, Meme
from datetime import datetime, timedelta
from sqlalchemy import Date, cast
from makememe import db
from better_profanity import profanity

def make(description):
    user_input = description.strip()
    nlp_output = ''
    if not profanity.contains_profanity(user_input):

        # hit_limit = did_hit_limit()
        hit_limit = False

        if hit_limit == False:
            print(f'user_input: {user_input}')
            
            print('________start_________')
            try:
                documents= ["sad", "indifferent", "waiting", "they don't know", "pompous", "better", "poor fix", "no responsibility", "ineffective solution", "in my opinion", "accurate depiction", "equal", "distracting", "three levels increasing"]
                
                testing = False
                if testing:
                    meme_description = documents[10]
                    print("meme_description: ", meme_description)
                else: 
                    best_result = {
                        "index": -1, 
                        "score": 0
                    }
                    response = GPT.search_request(documents, user_input)
                    for d in response['data']: 
                        print("d: ", d)
                        
                        if d["score"] > best_result["score"]:  
                            print("document: ", d["document"])
                            print("score: ", d["score"])
                            print("meme: ", documents[d["document"]])
                            best_result["score"] = d["score"]
                            best_result["index"] = d["document"]

                    print("best_result: ", best_result)
                    print("selected meme: ", documents[best_result["index"]])
                    meme_description = documents[best_result["index"]]
                
                nlp_output = meme_description
                meme = generate_meme(user_input, meme_description)
            except Exception as e:
                print(f'error: {e}')
                
                nlp_output = 'error'
                if isinstance(e.args[0], str): 
                    flagged = e.args[0].startswith('The content has been flagged')
                    if flagged:
                        nlp_output = 'flagged'
                        meme = {
                            'meme': 'meme_pics/flagged.png'
                        }
                    else:
                        meme = {
                            'meme': 'meme_pics/error.png'
                        }
                else: 
                    meme = {
                        'meme': 'meme_pics/error.png'
                    }
        else: 
            nlp_output = 'limit hit'
            meme = {
                'meme': 'meme_pics/limit_15.png'
            }
    else:
        nlp_output = 'flagged'
        meme = {
            'meme': 'meme_pics/flagged.png'
        }
    
    meme_for_db = Meme(title=meme['meme'], text_input=user_input, nlp_output=nlp_output, user_id=current_user.id)
    db.session.add(meme_for_db)
    db.session.commit()
    return meme


def generate_meme(user_input, meme_description):
    print('________meme_prompt_________')
    memes = [They_Dont_Know, Indifferent, Poor_Fix, Sad, Waiting, Better, Three_Levels_Increasing, Pompous, No_Responsibility, Ineffective_Solution, In_My_Opinion, Accurate_Depiction, Equal, Distracting]
    for meme in memes:
        if meme_description == meme.description:
            testing = False
            if testing: 
                meme = eval(f'{meme.name}()')
                image_name = meme.create({"depiction":"You want AI making memes. this is a long test a very long tdst"})
            else: 
                meme = eval(f'{meme.name}()')
                meme.append_example(user_input)
                print(f'prompt: {meme.instruction}')

                filter_no = GPT.content_filter(meme.instruction)['choices'][0]['text']
                print("filter_no: ", filter_no)
                if filter_no == '2':
                    raise Exception('The content has been flagged')
                print('________meme_completion_________')
                response = GPT.completion_request(meme.instruction)['choices'][0]['text'].strip()

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

def did_hit_limit(): 
    user = Users.query.filter_by(id=current_user.id).first()
    now = datetime.now()
    day_ago = now - timedelta(hours=24)
    meme_count = Meme.query.filter(Meme.date_created > day_ago, Meme.user_id == current_user.id).count()
    if meme_count > 15:
        return True
    else: 
        return False




