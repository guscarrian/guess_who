# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import random

from typing import Any, Text, Dict, List

class Action_User_Answers(ActionQueryKnowledgeBase):
    selected_character = "Hello"
    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")
        self.peopleList = knowledge_base.data["people"]
        self.selected_character = self.getRandCharacter(self.peopleList)
        self.peopleDict = self.getPeopleDict(self.peopleList)

        print("data: {}".format(self.peopleDict))

        # overwrite the representation function of the hotel object
        # by default the representation function is just the name of the object
        knowledge_base.set_representation_function_of_object(
            "hotel", lambda obj: obj["name"] + " (" + obj["city"] + ")"
        )

        super().__init__(knowledge_base)


    def name(self) -> Text:
        return "action_user_answers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("====> last message: {}".format(tracker.latest_message['entities']))
        dispatcher.utter_message(text="Character: {}".format(self.selected_character["name"]))

        return []

    def getRandCharacter(self, peopleList):
        random_number = random.randrange(0, len(peopleList) - 1) 
        return peopleList[random_number]

    def getPeopleDict(self, peopleList):
        peopleDict = {}
        for people in peopleList:
            print("getPeopleDict: {}".format(people))
            peopleDict[people["name"]] = {
                "background": people["background"],
                "eyes" : people["eyes"],
                "hair" : people["hair"]
            }

        return peopleDict
