RESPONSES_KEY = "responses"
RESPONSES_LENGTH = "responseslength"
SURVEY_LENGTH = "surveylength"
QUESTION = ""
CHOICES = ""
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from stories import story as story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)



@app.route('/')
def index():
    """Return homepage."""

    return redirect('/home')




@app.route('/home', methods=["POST", "GET"])
def index2():
    """Return homepage."""
    prompts = story.prompts
    our_requests = {}
    finaltext = ""
    if request.method == 'POST':
       
        return redirect('/createform')
    return render_template("home.html", story=story, prompts = prompts, our_requests=our_requests, finaltext=finaltext)


@app.route('/createform', methods=["POST", "GET"])
def index3():
    """Return homepage."""
    #import pdb
    #pdb.set_trace()
    prompts = story.prompts
    our_requests = {}
    finaltext = ""
    if request.method == 'POST':
        for response in prompts:
            word = request.form[response]
            our_requests[response] = word

        finaltext = story.generate(our_requests)
        return render_template("story.html", story=story, prompts = prompts, our_requests=our_requests, finaltext=finaltext )
    
    return render_template("createform.html", story=story, prompts = prompts, our_requests=our_requests, finaltext=finaltext )


@app.route('/story', methods=["POST", "GET"])
def index32():
    """Return homepage."""
    prompts = story.prompts
    if request.method == 'POST':
        return redirect('/home1')
    
        
    return render_template("story.html", story=story, prompts = prompts )








