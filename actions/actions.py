# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ValidateSymptomsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_symptoms_form"

    def validate_symptom(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate symptom input"""
        print(f"language_source given = {slot_value} length = {len(slot_value)}")
        symptom = slot_value
        if not isinstance(symptom, str):
            dispatcher.utter_message(text="I don't understand this symptom, could you try again?")
            return {'symptom': None}
        else:
            return {'symptom': symptom}


class ActionSaySymptom(Action):
    def name(self) -> Text:
        return "action_say_symptom"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        symptom = tracker.get_slot('symptom')
        print(f"I'm sorry to hear that you've got {symptom}")

        return []
