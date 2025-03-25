import webbrowser
import speech_recognition as sr
import pyttsx3
from core.weather import get_weather
from core.news import get_news, categorize_news, summarize_text
from core.ai_tasks import answer_question
from core.desktop_ops import open_file, search_files
from core.order import order_food  # Import the order_food function
from core.order_items import shop_items  # Import the shop_items function
from core.summarizer import summarize_files  # Import the summarize_files function

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def app_intro():
    intro_text = (
        "Welcome to Aagni - Your AI-Powered Desktop Assistant! "
        "I can help you with weather updates, news, AI-driven queries, "
        "file operations, food ordering, shopping, and even voice-based interaction. How can I assist you today?"
    )
    print(intro_text)
    speak(intro_text)

def recognize_speech():
    """Capture voice input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
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

        # If speech recognition fails, prompt for manual input
        speak("Please type your command.")
        command = input("Please enter your command: ")
        return command.lower()

def interpret_and_execute(command):
    """Process user command and perform actions."""
    if "weather" in command:
        speak("Which city do you want the weather for?")
        city = recognize_speech()
        weather = get_weather(city)
        response = f"Weather in {city}: {weather}"
        print(response)
        speak(response)
    
    elif "news" in command:
        speak("What kind of news are you interested in?")
        query = recognize_speech()
        category = categorize_news(query)
        news = get_news(category)
        response = f"Here are the top {category} news headlines."
        print(response)
        speak(response)
        for article in news[:3]:  # Limit to 3 news headlines
            print(f"- {article['title']}")
            speak(article['title'])
    
    elif "question" in command or "ai" in command:
        speak("AI Chat Mode activated. Say 'exit' to stop.")
        while True:
            speak("Ask your question.")
            query = recognize_speech()
            if query.lower() == "exit":
                speak("Exiting AI chat mode.")
                break
            answer = answer_question(query)
            print(f"AI: {answer}")
            speak(answer)
    
    elif "open file" in command:
        speak("Please specify the file path.")
        file_path = recognize_speech()
        result = open_file(file_path)
        print(result)
        speak(result)
    
    elif "search file" in command:
        speak("Please specify the directory.")
        directory = recognize_speech()
        speak("Now specify the filename.")
        filename = recognize_speech()
        result = search_files(directory, filename)
        print(result)
        speak(result)

    elif "send a message" in command:
        speak("Please specify the phone number with country code.")
        phone_number = recognize_speech()
        speak("What message would you like to send?")
        message = recognize_speech()
        whatsapp_url = f"https://wa.me/{phone_number}?text={message}"
        speak("Opening WhatsApp to send your message.")
        print("Opening WhatsApp...")
        webbrowser.open(whatsapp_url)
    
    elif "open youtube" in command:
        speak("Opening YouTube.")
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    
    elif "cricket score" in command:
        speak("Searching for cricket scores on Google.")
        print("Searching for cricket scores on Google...")
        webbrowser.open("https://www.google.com/search?q=cricket+score")
    
    elif "live ipl match" in command:
        speak("Opening Hotstar for live IPL match.")
        print("Opening Hotstar for live IPL match...")
        webbrowser.open("https://www.hotstar.com/in/sports/cricket/ipl-2021/match/live-streaming")

    elif "i am feeling hungry" in command:
        speak("What type of food are you looking for?")
        food_type = recognize_speech()
        speak(f"Searching for {food_type} restaurants nearby.")
        print(f"Searching for {food_type} restaurants nearby...")
        webbrowser.open(f"https://www.google.com/maps/search/{food_type}+restaurants+near+me")

    elif "order food" in command:
        # Call the order_food function from core/order.py
        order_food()

    elif "let's do shopping" in command or "shopping" in command:
        # Call the shop_items function from core/order_items.py
        shop_items()

    elif "summarize files" in command or "summarizer" in command:
        summarize_files()

    elif "exit" in command:
        speak("Goodbye! Exiting the assistant.")
        print("Goodbye! Exiting the assistant.")
        exit()
    
    else:
        # If the command is not recognized, perform a Google search
        speak("I am not capable of this operation. Performing a Google search instead.")
        print(f"Performing a Google search for: {command}")
        webbrowser.open(f"https://www.google.com/search?q={command}")

def main():
    app_intro()
    while True:
        command = recognize_speech()
        interpret_and_execute(command)

if __name__ == "__main__":
    main()

