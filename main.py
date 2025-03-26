from ollama_conf import get_ai_response
from speech_conf import speech_to_text,text_to_speech
import json

characters = {
    "Alex": {"gender": "male", "personality": "funny and chill", "greeting": "Hello!  my name Alex, nice to meet you."},
    "Luna": {"gender": "female", "personality": "kind and smart", "greeting": "Hello! my name Luna, whats up brother!"}
}

def select_character():
    print("\n Pilih karakter yang tersedia atau buat sendiri:")
    for name in characters:
        print(f"- {name} ({characters[name]['gender']}) - {characters[name]['personality']}")

    choice = input("\nKetik nama karakter atau 'custom' untuk buat sendiri: ").strip()

    if choice in characters:
        return choice,characters[choice]
    
    elif choice.lower() == "custom":
        name = input("Masukkan nama karakter: ")
        gender = input("Pilih gender (male/female): ").strip().lower()
        personality = input("Deskripsikan kepribadian karakter: ")
        greeting = input("Masukkan greeting awal karakter: ")

        return name,{"gender": gender, "personality": personality, "greeting": greeting}

    else:
        print("Karakter tidak ditemukan, gunakan default.")
        return "Alex",characters["Alex"]

if __name__ == "__main__":
    character_name, character = select_character()
    text_to_speech(character["greeting"], character["gender"])

    while True:
        user_input = speech_to_text()
        if user_input in ["stop", "exit", "quit"]:
            print("Conversation ended.")
            break
        if user_input:
            ai_response = get_ai_response(user_input,character_name ,character["personality"])
            text_to_speech(ai_response, character["gender"])
