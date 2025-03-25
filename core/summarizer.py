import os
import pyttsx3
from tkinter import Tk, filedialog
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def summarize_file(file_path, sentence_count=3):
    """Summarize the content of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        parser = PlaintextParser.from_string(content, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, sentence_count)
        return " ".join(str(sentence) for sentence in summary)
    except Exception as e:
        print(f"Error summarizing file {file_path}: {e}")
        return None

def summarize_files():
    """Handle summarizing multiple files."""
    speak("How many files would you like to summarize?")
    try:
        file_count = int(input("Enter the number of files to summarize: "))
    except ValueError:
        speak("Invalid input. Please enter a valid number.")
        print("Invalid input. Exiting summarization process.")
        return

    if file_count <= 0:
        speak("The number of files must be greater than zero.")
        print("Invalid file count. Exiting summarization process.")
        return

    # Open file dialog to select files
    root = Tk()
    root.withdraw()  # Hide the root Tkinter window
    root.attributes('-topmost', True)  # Bring the file dialog to the front
    speak("Please select the files to summarize.")
    file_paths = filedialog.askopenfilenames(
        title="Select Files",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    root.destroy()  # Destroy the root window after file selection

    if len(file_paths) != file_count:
        speak("The number of selected files does not match the input count.")
        print("File count mismatch. Exiting summarization process.")
        return

    # Summarize each file
    summaries = []
    for file_path in file_paths:
        speak(f"Summarizing file: {os.path.basename(file_path)}")
        print(f"Summarizing file: {file_path}")
        summary = summarize_file(file_path)
        if summary:
            summaries.append(summary)

    # Combine summaries and write to a new Notepad instance
    combined_summary = "\n\n".join(summaries)
    if combined_summary:
        speak("Writing the summary to a new Notepad instance.")
        print("Writing the summary to Notepad...")
        with open("summary.txt", "w", encoding="utf-8") as summary_file:
            summary_file.write(combined_summary)
        os.system("notepad summary.txt")
    else:
        speak("No summaries were generated.")
        print("No summaries were generated.")

if __name__ == "__main__":
    summarize_files()