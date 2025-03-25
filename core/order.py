import webbrowser
import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Capture voice input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("I'm listening.")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            print("Speech recognition service is unavailable.")
            speak("Speech recognition service is unavailable.")
        return None

def order_food():
    """Handle food ordering functionality."""
    speak("What type of food would you like to order?")
    food_type = recognize_speech()

    if not food_type:
        speak("I couldn't understand your response. Please type the food you want to order.")
        print("Please type the food you want to order:")
        food_type = input("Enter the type of food: ").strip().lower()

    if not food_type:
        speak("You did not provide any input. Please try again later.")
        print("No input provided. Exiting the food ordering process.")
        return

    # Redirect to Zomato with a search query for the specified food type in Bhubaneswar
    zomato_search_url = f"https://www.zomato.com/bhubaneswar/restaurants?q={food_type}"
    speak(f"Searching for {food_type} restaurants in Bhubaneswar on Zomato.")
    print(f"Opening Zomato for {food_type} restaurants in Bhubaneswar...")
    webbrowser.open(zomato_search_url)

    # Inform the user that the results have been displayed
    speak(f"I have displayed the {food_type} restaurants in Bhubaneswar on Zomato.")
    print(f"Displayed {food_type} restaurants in Bhubaneswar on Zomato.")

if __name__ == "__main__":
    order_food()