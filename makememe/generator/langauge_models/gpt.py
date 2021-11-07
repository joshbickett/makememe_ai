import requests, json

with open('/etc/make_meme/config.json') as config_file:
    config = json.load(config_file)

class GPT:

    @staticmethod
    def request(prompt):
        d_url = 'https://api.openai.com/v1/engines/davinci/completions'
        payload = \
            {
                'prompt': prompt,
                'stop': '###',
                'temperature': 0.5,
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

    def content_filter(prompt):
        wrapped_prompt = "<|endoftext|>" + prompt + "\n--\nLabel:"
        print(f'wrapped_prompt: {wrapped_prompt}')
        d_url = 'https://api.openai.com/v1/engines/content-filter-alpha-c4/completions'
        payload = \
            {
                'prompt': wrapped_prompt,
                'temperature': 0,
                'top_p': 1,
                'frequency_penalty': 0,
                'presence_penalty': 0,
                'best_of': 1,
                'max_tokens': 1,
                'logprobs': 10
            }

        headers = {'Content-Type': 'application/json',
                   'Authorization': f'Bearer {config["OPEN_AI_KEY"]}'}
        response = requests.post(d_url, data=json.dumps(payload), headers=headers)
        response = response.json()
        return response

