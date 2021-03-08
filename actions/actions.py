# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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

# First Action (Get Random Joke)

# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, BotUttered, AllSlotsReset
import logging
import requests
import json
#from rasa_core_sdk import Action

logger = logging.getLogger(__name__)
global query_global

test1 = "news headline"
test2 = "news video"
a1 = test1.split()
a2 = test2.split()
s1 = set(a1)
s2 = set(a2)
s3 = s2 - s1
a3 = a1 + list(s3)
test3 = ' '.join(a3)

#print("Test: ", test2.find(test1))
print("test3: ", test3)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get(
            'https://official-joke-api.appspot.com/random_joke').text)  # make an api call
        # extract a joke from returned json response
        joke = request['setup'] + '\n' + '– ' + request['punchline']
        dispatcher.utter_message(joke)  # send the message back to the user
        return []


# class ActionResponseQuery(Action):
#     def name(self):
#         # define the name of the action which can then be included in training stories
#         return "action_response_query"

#     def run(self, dispatcher, tracker, domain):
#         # what your action should do
#         query = tracker.get_slot("query")
#         entity = next(tracker.get_latest_entity_values("query"), None)

#         print("latest entity values: ", entity)
#         print("slot value: ", query)
#         print("intent: ", tracker.get_intent_of_latest_message())

#         response = {}
#         data = {}
#         text = {}
#         query_r = {}

#         if query != entity:
#             query = query

#         query_r["query"] = query
#         text["text"] = query_r
#         data["data"] = text
#         data["payload"] = "query"
#         response["custom"] = data

#         print(response)
#         print("\n")

#         #response = {"custom": {"data": {"text": {"query": query}}, "payload": "query"}}

#         # if query == None:
#         #     utterance = "Here are your results."
#         # else::
#         #     utterance = "Here are your {} results.".format(response["custom"]["data"]["text"]["query"])

#         #dispatcher.utter_message("Here are your {} results.".format(response["custom"]["data"]["text"]["query"]))  # send the message back to the user
#         return [BotUttered(None, response), AllSlotsReset()]

class ActionResponseQueryNegative(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_response_query_negative"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        query = tracker.get_slot("query_negative")
        entity = next(tracker.get_latest_entity_values("query"), None)

        #print("state: ", tracker.current_state())
        print("latest entity values: ", entity)
        print("slot value: ", query)
        print("intent: ", tracker.get_intent_of_latest_message())

        response = {}
        data = {}
        text = {}
        query_r = {}

        if query != entity:
            query = query

        global query_global
        print("query_global: ", query_global)

        # if query_global != None and query.find(query_global) == -1 and query_global.find(query) == -1:
        if query_global != None:
            #    query = query_global + " " + query
            # elif query_global.find(query)
            a1 = query_global.split()
            a2 = query.split()
            s1 = set(a1)
            s2 = set(a2)
            s3 = s2 - s1
            a3 = a1 + list(s3)
            query = ' '.join(a3)

        query_r["query"] = query
        text["text"] = query_r
        data["data"] = text
        data["payload"] = "query_negative"
        response["custom"] = data

        print(response)
        print("\n")
        #response = {"custom": {"data": {"text": {"query": query}}, "payload": "query"}}

        # if query == None:
        #     utterance = "Here are your results."
        # else::
        #     utterance = "Here are your results without {}.".format(response["custom"]["data"]["text"]["query"])

        # dispatcher.utter_message("Here are your {} results.".format(response["custom"]["data"]["text"]["query"]))  # send the message back to the user
        return [BotUttered(None, response), AllSlotsReset()]

# class ActionResponseQueryExtended(Action):
#     def name(self):
#         # define the name of the action which can then be included in training stories
#         return "action_response_query_extended"

#     def run(self, dispatcher, tracker, domain):
#         # what your action should do
#         query = tracker.get_slot("query_extended")
#         entity = next(tracker.get_latest_entity_values("query"), None)

#         print("latest entity values: ", entity)
#         print("slot value: ", query)
#         print("intent: ", tracker.get_intent_of_latest_message())

#         response = {}
#         data = {}
#         text = {}
#         query_r = {}

#         if query != entity:
#             query = query

#         query_r["query"] = query
#         text["text"] = query_r
#         data["data"] = text
#         data["payload"] = "query_extended"
#         response["custom"] = data

#         print(response)
#         print("\n")

#         #response = {"custom": {"data": {"text": {"query": query}}, "payload": "query"}}

#         # if query == None:
#         #     utterance = "Here are your results."
#         # else::
#         #     utterance = "Here are your results with {}.".format(response["custom"]["data"]["text"]["query"])

#         #dispatcher.utter_message("Here are your {} results.".format(response["custom"]["data"]["text"]["query"]))  # send the message back to the user
#         return [BotUttered(None, response), AllSlotsReset()]


class ActionResponseQuery(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_response_query"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        query_1 = tracker.get_slot("query_1")
        query_2 = tracker.get_slot("query_2")
        query_3 = tracker.get_slot("query_3")
        query_4 = tracker.get_slot("query_4")
        query_5 = tracker.get_slot("query_5")
        query_6 = tracker.get_slot("query_6")

        entity_1 = next(tracker.get_latest_entity_values("query_1"), None)
        entity_2 = next(tracker.get_latest_entity_values("query_2"), None)
        entity_3 = next(tracker.get_latest_entity_values("query_3"), None)
        entity_4 = next(tracker.get_latest_entity_values("query_4"), None)
        entity_5 = next(tracker.get_latest_entity_values("query_5"), None)
        entity_6 = next(tracker.get_latest_entity_values("query_6"), None)

        print("latest entity values: ", [
              entity_1, entity_2, entity_3, entity_4, entity_5, entity_6])
        print("slot values: ", [query_1, query_2,
                                query_3, query_4, query_5, query_6])
        print("intent: ", tracker.get_intent_of_latest_message())

        response = {}
        data = {}
        text = {}
        query_r = {}

        # if query != entity:
        #     query = query

        if entity_1 != None:
            if query_1 != None and query_1 not in entity_1:
                query_1 = entity_1 + " " + query_1
            else:
                query_1 = entity_1
        else:
            if query_1 == None:
                query_1 = ""

        if entity_2 != None:
            print(query_1)
            if query_2 != None and query_2 not in entity_2 and query_2 not in query_1:
                query_2 = entity_2 + " " + query_2
            else:
                if query_2 in query_1:
                    query_2 = ""
                else:
                    query_2 = entity_2
        else:
            if query_2 == None:
                query_2 = ""

        if entity_3 != None:
            if query_3 != None and query_3 not in entity_3:
                query_3 = entity_3 + " " + query_3
            else:
                query_3 = entity_3
        else:
            if query_3 == None:
                query_3 = ""

        if entity_4 != None:
            if query_4 != None and query_4 not in entity_4:
                query_4 = entity_4 + " " + query_4
            else:
                query_4 = entity_4
        else:
            if query_4 == None:
                query_4 = ""

        if entity_5 != None:
            if query_5 != None and query_5 not in entity_5:
                query_5 = entity_5 + " " + query_5
            else:
                query_5 = entity_5
        else:
            if query_5 == None:
                query_5 = ""

        if entity_6 != None:
            if query_6 != None and query_6 not in entity_6:
                query_6 = entity_6 + " " + query_6
            else:
                query_6 = entity_6
        else:
            if query_6 == None:
                query_6 = ""

        # if query_2 == None:
        #     query_2 = ""
        #     if entity_2 != None:
        #         query_2 = entity_2

        # if query_3 == None:
        #     query_3 = ""
        #     if entity_3 != None:
        #         query_3 = entity_3

        # if query_4 == None:
        #     query_4 = ""
        #     if entity_4 != None:
        #         query_4 = entity_4

        # if query_5 == None:
        #     query_5 = ""
        #     if entity_5 != None:
        #         query_5 = entity_5

        query = ' '.join(
            filter(None, (query_1, query_2, query_3, query_4, query_5, query_6)))
        #query = query_1 + " " + query_2 + " " + query_3 + " " + query_4 + " " + query_5

        if query == "":
            query = None
        global query_global
        query_global = query

        query_r["query"] = query
        text["text"] = query_r
        data["data"] = text
        data["payload"] = "query_extended"
        response["custom"] = data

        print(response)
        print("\n")

        #response = {"custom": {"data": {"text": {"query": query}}, "payload": "query"}}

        # if query == None:
        #     utterance = "Here are your results."
        # else::
        #     utterance = "Here are your results with {}.".format(response["custom"]["data"]["text"]["query"])

        # dispatcher.utter_message("Here are your {} results.".format(response["custom"]["data"]["text"]["query"]))  # send the message back to the user
        return [BotUttered(None, response), AllSlotsReset()]


class ActionResponseMoreScreens(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_response_more_screens"

    def run(self, dispatcher, tracker, domain):
        # what your action should do

        #print("state: ", tracker.current_state())
        #print("latest entity values: ", entity)
        #print("slot value: ", query)
        print("intent: ", tracker.get_intent_of_latest_message())

        response = {}
        data = {}
        text = {}
        query_r = {}

        query_r["query"] = "query"  # query
        text["text"] = query_r
        data["data"] = text
        data["payload"] = "more_screens"
        response["custom"] = data

        print(response)
        print("\n")
        #response = {"custom": {"data": {"text": {"query": query}}, "payload": "query"}}

        # if query == None:
        #     utterance = "Here are your results."
        # else::
        #     utterance = "Here are your results without {}.".format(response["custom"]["data"]["text"]["query"])

        # dispatcher.utter_message("Here are your {} results.".format(response["custom"]["data"]["text"]["query"]))  # send the message back to the user
        utter = "Here are the next top 20 screens."

        return [BotUttered(utter, response)]
