# [makememe.ai](http://makememe.ai/)

In the app, users create memes in under 5 seconds by describing them with natural language. This open-source project is a fun way for software developers to learn about AI and Python development.

You are welcome to fork this repo and make adjustments or contributions. If you fork or clone the repo, it is first required to review OpenAI's [go live policy](https://beta.openai.com/docs/going-live). You will need your own access and key in order to contribute.

If you have any technical or other questions, you can reach out to me at josh@makememe.ai. I am happy to answer questions and walk through how the project works.  

## [The Site](http://makememe.ai/)

<img src="media/makememe-homepage.png" width="600" alt="makememe.ai home page"></img>

## [The Demo](https://www.producthunt.com/posts/makememe-ai)

[![makememe.ai demo video](https://img.youtube.com/vi/wZ6KCDAcKws/0.jpg)](https://www.producthunt.com/posts/makememe-ai)

# Setup the website locally

There are three steps required to get the makememe.ai app to run on your computer. If you are not familiar with the technology stack I highly recommend [Corey Schafer's](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) Youtube series on [Python Flask Tutorial: Full-Featured Web App](https://www.youtube.com/watch?v=MwZwr5Tvyxo). The series goes over Flask and Postgres in detail. To learn more about the AI system, I recommend reading my Medium post [How To Make Memes with AI in Python](https://towardsdatascience.com/how-to-make-memes-with-ai-in-python-986944bce5b4).

1. Setup the Flask server
2. Install and run Postgres
3. Create Config file that includes an OpenAI Key

## 1. Setup the Flask Server

Create a [virtual environment](https://docs.python.org/3/library/venv.html)

```
python3 -m venv venv
```

Activate the environment

```
source venv/bin/activate
```

Install all packages into venv

```
pip3 install -r requirements.txt
```

If you are curious if this worked, you can try the following command `python run.py` and then go to `http://127.0.0.1:5000/`. You should see the app. The meme creation functionality will not work until you complete the remaining steps.

## 2. Install and run Postgres

If you do not have Postgres installed, you will need to install it on you computer.

Homebrew can help install Postgres. If you need to install Homebrew their [webpage](https://brew.sh/) has a tutorial.

Mac users you can install Postgres with the following [Homebrew command](https://formulae.brew.sh/formula/postgresql):

```
brew install postgresql
```

When Postgres is installed with Homebrew a postgres user needs to be created with the command below.

```
 /usr/local/opt/postgres/bin/createuser -s postgres
```

The next step is to start the Postgres service

```
brew services start postgresql
```

Now we can create the database for the application with the command below

```
createdb makememe
```

The next few commands need to be executed in the project directory. If you are not in that directory, please navigate there now (cd - change directory command).

Once you are in the project directory, make sure the virtual environment is activated (should show (venv) next to terminal user). If not, activate it with the command `source venv/bin/activate`

Now open the python terminal by typing the command below.

```
python
```

Finally, we will create the database tables in the python terminal with the commands below

```
from makememe import db
db.create_all()
db.session.commit()
```

Now you can exit.

```
exit()
```

## 3. Create Config file that includes an OpenAI Key

In order to run the project locally a few pieces of information need to be setup in a config file. Follow the steps below to setup prepare the project.

The first step is to create the following file (with a matching directory path).

```
/etc/make_meme/config.json
```

Once the file is created, we populate it with some information.

Flask requires a secret key to sign cookies. You can learn more about it [here](https://explore-flask.readthedocs.io/en/latest/configuration.html).

OpenAI provides a key when developers receive access to the API. The local project uses your key when making OpenAI API request. The request and billing will show up under your account. Assuming you are running the project for testing and development reasons, the cost should be small.

The project also requires a file with font information. It uses that font to display the text on the image.

Lastly, a database URI for Postgres is required. The Postgres user information will need to be entered into the URI.

```
{
        "SECRET_KEY": "~a Flask secret key here~",
        "OPEN_AI_KEY": "~your key~",
        "FONT_PATH": "~path to a font~",
        "DB_URI": "~your Postgres URI~"
}
```

Once this file is created then the project should be ready to run..

Navigate to the project directory and make sure the virtual environment is running (venv). Type the command below.

```
python run.py
```

Now you can enter the local server URL (below) in your web browser and you should see the app.

```
http://127.0.0.1:5000/
```
