import re
import json
from madlib.src.MadLib import MadLib
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

form = "<input type='text' name='response'><input type='submit'><br>"
error = "<br><strong style='color: red;'>Please type something into the textfield</strong>"
htmlFile = "madlib/index.html"
madLibLists = []

def madlib(request):
    # Needs to be initialized in order to be used, even if it is not the correct one
    madLibGame = madLibLists[0] if len(madLibLists) > 0 else None
    if (not request.POST.__contains__("id")):
        madLibGame = MadLib([], [], [], "", MadLib.classId)
        madLibLists.append(madLibGame)
    else:
        for game in madLibLists:
            if int(game.id) == int(request.POST.__getitem__("id")):
                madLibGame = game
                break
    if request.POST.__contains__("restart") or len(madLibGame.questions) == 0:
        madLibGame.newGame()
        return render(
            request,
            htmlFile, 
            {
                'form': form,
                'partOfSpeech': madLibGame.questions[0],
                'id': madLibGame.id
            }
        )
    if request.method == "POST" and request.POST.__contains__("response") and len(request.POST.__getitem__("response").strip()) != 0:
        madLibGame.responses.append(request.POST.__getitem__("response")[0])
        if len(madLibGame.responses) == len(madLibGame.questions):
            storyString = madLibGame.generateStory(madLibGame.responses, madLibGame.story)
            return render(
                request,
                htmlFile,
                {
                    'title': madLibGame.title,
                    'story': storyString,
                    'id': madLibGame.id
                }
            )
        return render(
            request,
            htmlFile,
            {
                'form': form,
                'partOfSpeech': madLibGame.questions[len(madLibGame.responses)],
                'id': madLibGame.id
            }
        )
    return render(
        request,
        htmlFile,
        {
            'form': form,
            'error': error,
            'partOfSpeech': madLibGame.questions[len(madLibGame.responses)],
            'id': madLibGame.id
        }
    )