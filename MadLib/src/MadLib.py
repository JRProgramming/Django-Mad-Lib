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
        with open("MadLib/src/MadLib.json") as f:
            madLibJSON = json.load(f)
            madLibSelection = madLibJSON["templates"][randint(0, len(madLibJSON["templates"])-1)]
        self.questions = madLibSelection["blanks"]
        self.story = madLibSelection["value"]
        self.title = madLibSelection["title"]

    def generateStory(self):
        storyString = ""
        for index, question in enumerate(self.story):
            if index < len(self.responses):
                if index != 0:
                    self.responses[index] = self.responses[index].lower()
                storyString += question + self.responses[index]
            else: 
                if index != len(self.story) - 1:
                    storyString += question
        return storyString 