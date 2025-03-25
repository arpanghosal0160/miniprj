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

def shop_items():
    """Handle shopping functionality."""
    speak("What item would you like to shop for?")
    item = recognize_speech()

    if not item:
        speak("I couldn't understand your response. Please type the item you want to shop for.")
        print("Please type the item you want to shop for:")
        item = input("Enter the item: ").strip().lower()

    if not item:
        speak("You did not provide any input. Please try again later.")
        print("No input provided. Exiting the shopping process.")
        return

    # Redirect to Amazon with a search query for the specified item
    amazon_search_url = f"https://www.amazon.in/s?k={item}"
    speak(f"Searching for {item} on Amazon.")
    print(f"Opening Amazon for {item}...")
    webbrowser.open(amazon_search_url)

    # Inform the user that the results have been displayed
    speak(f"I have displayed the search results for {item} on Amazon.")
    print(f"Displayed search results for {item} on Amazon.")

if __name__ == "__main__":
    shop_items()