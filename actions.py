# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from boto3.resources import params
import requests
import json
from rasa_sdk import Action
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class ActionJobsearch(Action):

    def name(self):
        return 'job_details'

    def run(self, dispatcher, tracker, domain):
        category = tracker.get_slot('category')
        print(category)
        url = 'https://api.linkedin.com/v1/job-search{category}.json'.format(category=category)
        response = requests.get(url, params).text
        json_data = json.loads(response)['results']
        i = 0
        for results in json_data:
            i = i+1
            message = str(i) + "." + results['abstract']
            dispatcher.utter_message(message)
        return[]