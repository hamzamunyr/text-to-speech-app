from gtts import gTTS
from playsound import playsound
import tempfile
import os
import shutil

def do_tts(text):
    tts = gTTS(text)
        
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    temp_file.close()
    
    tts.save(temp_file.name)
    return temp_file.name

def get_next_default_filename():
    music_folder = os.path.join(os.path.expanduser("~"), "Music")
    if not os.path.exists(music_folder):
        os.makedirs(music_folder)
        
    index = 1
    while True:
        default_name = f"tts_{index}.mp3"
        if not os.path.exists(os.path.join(music_folder, default_name)):
            return default_name
        index += 1

def text_to_speech_input():
    user_text = input("Enter text to convert to speech: ")
    file_path = do_tts(user_text)
    print("Playing speech...")
    playsound(file_path)
    print("Speech completed.")
    
    # Ask to save
    while True:
        save_choice = input("Do you want to save this mp3 file to your Music folder? (yes/no): ").strip().lower()
        if save_choice in ['yes', 'y']:
            try:
                music_folder = os.path.join(os.path.expanduser("~"), "Music")
                default_name = get_next_default_filename()
                print(f"Suggested filename: {default_name}")
                filename = input("Enter filename (without extension) or press Enter to accept default: ").strip()
                if filename == "":
                    filename = os.path.splitext(default_name)[0]
                save_path = os.path.join(music_folder, f"{filename}.mp3")
                shutil.move(file_path, save_path)
                print(f"File saved as {save_path}")
            except Exception as e:
                print(f"Error saving file: {e}")
            break
        elif save_choice in ['no', 'n']:
            os.remove(file_path)
            print("Temporary file deleted.")
            break
        else:
            print("Please type 'yes' or 'no'.")

# Main program loop
while True:
    print("\n===== TEXT TO SPEECH SYSTEM =====")
    print("1. Enter text to convert to speech")
    print("2. Exit")
    
    choice = input("\nEnter your choice (1-2): ")
    
    if choice == "1":
        text_to_speech_input()
    elif choice == "2":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
