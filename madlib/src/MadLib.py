import json
from random import randint

class MadLib:

    classId = 0

    def __init__(self, questions, story, responses, title, id):
        self.questions = questions
        self.story = story
        self.responses = responses
        self.title = title
        self.id = id
        MadLib.classId += 1

    def newGame(self):
        with open("madlib/src/madlib.json") as f:
            madLibJSON = json.load(f)
            madLibSelection = madLibJSON["templates"][randint(0, len(madLibJSON["templates"])-1)]
        self.questions = madLibSelection["blanks"]
        self.story = madLibSelection["value"]
        self.title = madLibSelection["title"]

    def generateStory(self, responses, story):
        storyString = ""
        for index, question in enumerate(story):
            if index < len(responses):
                if index != 0:
                    responses[index] = responses[index].lower()
                storyString += question + responses[index]
            else: 
                if index != len(story) - 1:
                    storyString += question
        return storyString 