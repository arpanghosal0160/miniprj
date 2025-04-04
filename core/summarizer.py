import os
import cohere
import pyttsx3
from tkinter import Tk, filedialog
from docx import Document

# === CONFIG ===
COHERE_API_KEY = "ilAww2FKbcYb0nT7N5FmnosPvHxJtx7MXGw7hFgU"  # Replace with your actual key
SUMMARY_SENTENCES = 3

# === Text-to-Speech Engine ===
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# === Read .txt and .docx Files ===
def read_file_content(file_path):
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file type.")

# === Call Cohere API ===
def summarize_with_cohere(text):
    try:
        co = cohere.Client(COHERE_API_KEY)
        response = co.summarize(
            text=text,
            length='medium',
            format='paragraph',
            model='command',
            extractiveness='medium'
        )
        return response.summary
    except Exception as e:
        print(f"Error using Cohere API: {e}")
        return None

# === Main Summarization Handler ===
from tkinter import simpledialog, messagebox

def summarize_files():
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    # GUI prompt to ask how many files to summarize
    file_count = simpledialog.askinteger(
        "Number of Files",
        "How many files would you like to summarize?",
        minvalue=1,
        parent=root
    )

    if not file_count:
        speak("No input given. Exiting.")
        return

    speak("Please select your files.")
    file_paths = filedialog.askopenfilenames(
        title="Select Files",
        filetypes=[("Supported Files", "*.txt *.docx")]
    )
    root.destroy()

    if len(file_paths) != file_count:
        messagebox.showerror("File Count Mismatch", f"You selected {len(file_paths)} file(s) but expected {file_count}.")
        speak("Mismatch in number of selected files.")
        return

    summaries = []
    for path in file_paths:
        speak(f"Processing file {os.path.basename(path)}")
        print(f"Reading: {path}")
        try:
            content = read_file_content(path)
            if not content.strip():
                raise ValueError("Empty file.")

            summary = summarize_with_cohere(content)
            if not summary:
                summary = content[:500] + "..."  # Fallback

            summaries.append(f"Summary of {os.path.basename(path)}:\n{summary}\n")
        except Exception as e:
            print(f"Failed to summarize {path}: {e}")
            speak(f"Failed to summarize {os.path.basename(path)}")

    final_summary = "\n\n".join(summaries)
    with open("combined_summary.txt", "w", encoding="utf-8") as f:
        f.write(final_summary)

    speak("Summary written to Notepad.")
    os.system("notepad combined_summary.txt")


# === Entry Point ===
if __name__ == "__main__":
    summarize_files()
