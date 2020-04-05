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
    selected_character = ""
    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")
        self.peopleList = knowledge_base.data["people"]
        self.selected_character = self.getRandCharacter(self.peopleList)

        print("data: {}".format(self.selected_character))

        super().__init__(knowledge_base)


    def name(self) -> Text:
        return "action_user_answers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Domain: {}".format(domain))
        entities = tracker.latest_message['entities']
        print("====> last message: {}".format(entities))
        if (len(entities) == 0):
            dispatcher.utter_message(text="Answer: {}".format("I cannot understand. Refrase your sentence as a yes/no question."))
            return []

        object_type = self.getObjectType(entities).lower()
        attribute_value = self.getAttributeValue(entities).lower()
        dispatcher.utter_message(text="Answer: {}".format(self.getAnswer(object_type, attribute_value)))

        return []

    def getRandCharacter(self, peopleList):
        random_number = random.randrange(0, len(peopleList))
        return peopleList[random_number]

    def getAttributeValue(self, entities):
        if (len(entities) == 1):
            return entities[0]['value']
        if (entities[0]['entity'] == "object_type"):
            return entities[1]['value']

        return entities['value']

    def getObjectType(self, entities):
        if (len(entities) == 1):
            return entities[0]['entity']
        if (entities[0]['entity'] == "object_type"):
            return entities[0]['value']

        return tracker.latest_message['entities'][1]['value']


    def getAnswer(self, object_type, attribute_value):
        if (object_type not in self.selected_character):
            return "I don't know. Please, ask in a different way"
        return "Yes" if (self.selected_character[object_type] == attribute_value) else "No"