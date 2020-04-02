from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")
        self.people = knowledge_base.data["people"]
        self.peopleDict = self.getPeopleDict(self.people)
        print("data: {}".format(self.peopleDict))

        # overwrite the representation function of the hotel object
        # by default the representation function is just the name of the object
        knowledge_base.set_representation_function_of_object(
            "hotel", lambda obj: obj["name"] + " (" + obj["city"] + ")"
        )

        super().__init__(knowledge_base)
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