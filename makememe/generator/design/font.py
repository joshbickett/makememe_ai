import json

with open('/etc/make_meme/config.json') as config_file:
    config = json.load(config_file)

font_path = config['FONT_PATH']