from django.shortcuts import render
from .models import Post
import requests, json
from meme.prompts.classifier import Classifier
from meme.prompts.types.better import Better
from meme.prompts.types.not_a_good_idea import Not_A_Good_Idea
from meme.prompts.types.cry import Cry
from meme.prompts.types.poor_fix import Poor_Fix
from meme.prompts.types.they_dont_know import They_Dont_Know
import sys

with open('/etc/make_meme/config.json') as config_file:
    config = json.load(config_file)

def home(request):
    if request.method == 'POST':
        user_input = request.POST["description"]
        classifier = Classifier()
        classifier.append_example(user_input)
        print('________start_________')
        print('________classifier_prompt_________')
        print(f'prompt: {classifier.instruction}')
        response = gpt3_request(classifier.instruction)
        try:
            response = response['choices'][0]['text'].strip('\n')
            response = json.loads(response)
            print('________classifier_response_________')
            print(f'response: {response}')
            meme_type = response['meme-type']
            print(f'meme_type: {meme_type}')
            print('________meme_prompt_________')
            if meme_type == 'better':
                better = Better()
                better.append_example(user_input)
                response = gpt3_request(better.instruction)
                response = response['choices'][0]['text'].strip('\n')
                print(f'prompt: {better.instruction}')
                print('________meme_response_________')
                print(f'response:{response}')
                response = json.loads(response)
                image_name = better.create(response)
                file_location = f'creations/{image_name}'
                context = {
                    'meme': file_location
                }
            elif meme_type == 'not a good idea':
                not_a_good_idea = Not_A_Good_Idea()
                not_a_good_idea.append_example(user_input)
                response = gpt3_request(not_a_good_idea.instruction)
                response = response['choices'][0]['text'].strip('\n')
                print(f'prompt: {not_a_good_idea.instruction}')
                print('________meme_response_________')
                print(f'response:{response}')
                response = json.loads(response)
                image_name = not_a_good_idea.create(response)
                file_location = f'creations/{image_name}'
                context = {
                    'meme': file_location
                }
            elif meme_type == 'cry':
                cry = Cry()
                cry.append_example(user_input)
                response = gpt3_request(cry.instruction)
                response = response['choices'][0]['text'].strip('\n')
                print(f'prompt: {cry.instruction}')
                print('________meme_response_________')
                print(f'response:{response}')
                response = json.loads(response)
                image_name = cry.create(response)
                file_location = f'creations/{image_name}'
                context = {
                    'meme': file_location
                }
            elif meme_type == "poor fix":
                poor_fix = Poor_Fix()
                poor_fix.append_example(user_input)
                response = gpt3_request(poor_fix.instruction)
                response = response['choices'][0]['text'].strip('\n')
                print(f'prompt: {poor_fix.instruction}')
                print('________meme_response_________')
                print(f'response:{response}')
                response = json.loads(response)
                image_name = poor_fix.create(response)
                file_location = f'creations/{image_name}'
                context = {
                    'meme': file_location
                }
            elif meme_type == "they don't know":
                they_dont_know = They_Dont_Know()
                they_dont_know.append_example(user_input)
                response = gpt3_request(they_dont_know.instruction)
                response = response['choices'][0]['text'].strip('\n')
                print(f'prompt: {they_dont_know.instruction}')
                print('________meme_response_________')
                print(f'response:{response}')
                response = json.loads(response)
                image_name = they_dont_know.create(response)
                file_location = f'creations/{image_name}'
                context = {
                    'meme': file_location
                }
            else:
                print("Meme type not found")
                context = {
                    'meme': 'meme_pics/error.jpg'
                }
        except Exception as e:
            print('Something went wrong')
            print(f'error: {e}')
            context = {
                'meme': 'meme_pics/error.jpg'
            }
    else:
        context = {
            'meme': 'meme_pics/default.jpg',
            'text': ''
        }
    print('________end_________')
    return render(request, 'meme/home.html', context)

def about(request):
    return render(request, 'meme/about.html')

def technology(request):
    return render(request, 'meme/technology.html')

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'meme/blog.html', context)

def gpt3_request(prompt):
    d_url = 'https://api.openai.com/v1/engines/davinci/completions'
    payload = \
        {
            'prompt': prompt,
            'stop': '###',
            'temperature': 0.7,
            'top_p': 1,
            'frequency_penalty': 0,
            'presence_penalty': 0,
            'best_of': 1,
            'max_tokens': 50
        }

    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {config["OPEN_AI_KEY"]}'}
    response = requests.post(d_url, data=json.dumps(payload), headers=headers)
    response = response.json()
    return response

def create_meme_context(meme):
    content = None
    return context
