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

        # Extract the genre entity from the latest message
        genre = None
        for entity in tracker.latest_message.get("entities", []):
            if entity.get("entity") == "genre":
                genre = entity.get("value")
                break

        # Simple recommendation logic based on genre
        if genre:
            genre_lower = genre.lower()
            if "action" in genre_lower:
                recommendation = "Avengers Infinity War or Avengers End Game"
            elif "comedy" in genre_lower:
                recommendation = "Hera Pheri"
            elif "drama" in genre_lower:
                recommendation = "Joker"
            elif "sci-fi" in genre_lower or "scifi" in genre_lower:
                recommendation = "Interstellar"
            elif "horror" in genre_lower:
                recommendation = "The Conjuring"
            elif "romance" in genre_lower:
                recommendation = "The Notebook or Sanam Teri Kasam"
            elif "thriller" in genre_lower:
                recommendation = "John Wick"
            elif "fantasy" in genre_lower:
                recommendation = "The Lord of the Rings: The Fellowship of the Ring"
            elif "mystery" in genre_lower:
                recommendation = "The Body or Freddy"
            elif "animated" in genre_lower:
                recommendation = "Spirited Away"
            elif "documentary" in genre_lower:
                recommendation = "Free Solo"
            elif "historical" in genre_lower:
                recommendation = "Chhaava"
            elif "biographical" in genre_lower:
                recommendation = "Sam Bahadur"
            elif "cartoon" in genre_lower:
                recommendation = "Shin-chan: Operation Golden Spy"
            else:
                recommendation = "Inception"  # fallback recommendation
        else:
            recommendation = "Inception"  # default recommendation if no genre is detected

        dispatcher.utter_message(text=f"If you're in the mood for {genre} movies, I recommend {recommendation}!")
        return []
