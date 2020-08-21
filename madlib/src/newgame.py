import json
from random import randint

responses = []
questions = []
story = []
title = ''

def newGame():
    global responses, questions, story, title
    responses = []
    with open("madlib.json") as f:
        madlibAPI = json.load(f)
    madlibAPI = madlibAPI["templates"]
    randomNum = randint(0, len(madlibAPI)-1)
    madlib = madlibAPI[randomNum]
    questions = madlib["blanks"]
    story = madlib["value"]
    title = madlib["title"]
    output = {}
    output['questions'] = questions
    output['story'] = story
    output['title'] = title
    return output