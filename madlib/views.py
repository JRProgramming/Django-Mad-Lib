import re
import json
from madlib.src.newGame import newGame
from madlib.src.generateStory import generateStory
from random import randint
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

responses = []
questions = []
story = []
title = ''
form = "<input type='text' name='response'><input type='submit'><br>"
error = "<br><strong style='color: red;'>Please type something into the textfield</strong>"

def madlib(request):
    global questions, responses, story, title
    if request.POST.__contains__("restart") or len(questions) == 0:
        game = newGame()
        responses, questions, story, title = game.values()
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
            storyString = generateStory(responses, story)
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