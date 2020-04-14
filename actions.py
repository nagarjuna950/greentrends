
import os
import requests
from rasa_sdk import Action, Tracker
from rasa_core_sdk.forms import FormAction
from rasa_core_sdk.events import SlotSet
from typing import Dict, Text, Any, List, Union, Optional 

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import FollowupAction
from rasa_core_sdk.events import ActionReverted


class MoodIdentifier(Action):
    def name(self) -> Text:
        return 'action_service'

    def run(self, dispatcher, tracker, domain):
        intent =  tracker.latest_message['intent'].get('name')
        message= tracker.latest_message.get('text')
        print('message',message)
        print(intent)
        print(type(intent))
        if message in "Male":
            dispatcher.utter_template("utter_male_services",tracker)
        else:
            dispatcher.utter_template("utter_female_services",tracker)
        return[]

class MoodIdentifier(Action):
    def name(self) -> Text:
        return 'action_service_price'

    def run(self, dispatcher, tracker, domain):
        message = tracker.latest_message.get('text')
        print('message',message)

        intent =  tracker.latest_message['intent'].get('name')
        print(intent)
        print(type(intent))
        if message in "Haircut":
            dispatcher.utter_template("utter_male_services_price",tracker)
        elif message in "Hair Colour":
            dispatcher.utter_template("utter_ongoing",tracker)
            #FollowupAction('utter_male_services')
            return [ActionReverted(),ActionReverted()]
        else:
            dispatcher.utter_template("utter_female_services_price",tracker)
        return[]


class MoodIdentifier(Action):
    def name(self) -> Text:
        return 'action_yesno'

    def run(self, dispatcher, tracker, domain):
        intent =  tracker.latest_message['intent'].get('name')
        print(intent)
        print(type(intent))
        if intent in "mood_happy":
            dispatcher.utter_template("utter_yes",tracker)
        else:
            dispatcher.utter_template("utter_no",tracker)
        return[]
        
          






        
          






