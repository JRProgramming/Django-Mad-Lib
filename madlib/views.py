import re
import requests
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

responses = []
madlibAPI = requests.get("http://madlibz.herokuapp.com/api/random")
questions = madlibAPI.json()["blanks"]
story = madlibAPI.json()["value"]
title = madlibAPI.json()["title"]
form = "<input type='text' name='response'><input type='submit'><br>"
error = "<br><strong style='color: red;'>Please type something into the textfield</strong>"

def madlib(request):
    global questions, responses, story, title, form
    if request.POST.__contains__("restart") or (request.method == "GET" and len(responses) == 0):
        newGame()
        return render(
            request,
            'madlib/index.html', {
                'form': form,
                'partOfSpeech': questions[0]
            }
        )
    if request.method == "POST" and request.POST.__contains__("response") and len(request.POST.__getitem__("response").strip()) != 0:
        responses.append(request.POST.__getitem__("response")[0])
        if len(responses) == len(questions):
            storyString = ""
            for index, question in enumerate(story):
                if index < len(responses):
                    if index != 0:
                        responses[index] = responses[index].lower()
                    storyString += question + responses[index]
                else: 
                    if index != len(story) - 1:
                        storyString += question
            return render(
                request,
                'madlib/index.html',
                {
                    'title': title,
                    'story': storyString
                }
            )
        return render(
            request,
            'madlib/index.html',
            {
                'form': form,
                'partOfSpeech': questions[len(responses)]
            }
        )
    return render(
        request,
        'madlib/index.html',
        {
            'form': form,
            'error': error,
            'partOfSpeech': questions[len(responses)]
        }
    )
        
def newGame():
    global responses, madlibAPI, questions, story, title
    responses = []
    madlibAPI = requests.get("http://madlibz.herokuapp.com/api/random")
    questions = madlibAPI.json()["blanks"]
    story = madlibAPI.json()["value"]
    title = madlibAPI.json()["title"]