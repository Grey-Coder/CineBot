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


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionMovieRecommendation(Action):

    def name(self) -> Text:
        return "action_movie_recommendation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extract the 'genre' entity from the user's message
        genre = None
        for entity in tracker.latest_message.get("entities", []):
            if entity.get("entity") == "genre":
                genre = entity.get("value")
                break

        # Simple recommendation logic based on the genre
        if genre:
            genre_lower = genre.lower()
            if "অ্যাকশন" in genre_lower:
                recommendation = "ম্যাড ম্যাক্স: ফিউরি রোড"
            elif "কমেডি" in genre_lower:
                recommendation = "দ্য গ্র্যান্ড বুদাপেস্ট হোটেল"
            elif "ড্রামা" in genre_lower:
                recommendation = "দ্য শশাঙ্ক রিডেম্পশন"
            elif "সাই-ফাই" in genre_lower:
                recommendation = "ইন্টারস্টেলার"
            elif "হরর" in genre_lower:
                recommendation = "গেট আউট"
            else:
                recommendation = "ইনসেপশন"  # Fallback recommendation
        else:
            recommendation = "ইনসেপশন"  # Default if no genre is detected

        dispatcher.utter_message(
            text=f"আপনি {genre} ধরণের সিনেমা দেখতে চাইছেন? আমি পরামর্শ দিচ্ছি *{recommendation}*!"
        )

        return []
