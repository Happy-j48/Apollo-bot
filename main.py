# apollo_lookup_bot.py

import telebot
import speech_recognition as sr
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from flask import Flask, request, jsonify
import os

# === CONFIGURATION ===
TELEGRAM_BOT_TOKEN = '7612354488:AAEuncMg-5oq7cm3eRP_0IgS37YW8DF4wGk'  # Must include a colon (e.g., '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11')
GOOGLE_SHEET_NAME = 'Apollo Lookup Logs'

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# === GOOGLE SHEETS SETUP ===
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open(GOOGLE_SHEET_NAME).sheet1

# === SPEECH TO TEXT FUNCTION ===
def transcribe_voice(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language='hi-IN')
    except Exception as e:
        return ""

# === DUMMY PERSON LOOKUP ===
def lookup_apollo_person(query):
    # Simulated response instead of real Apollo API
    dummy_database = {
        "rahul": {
            "name": "Rahul Sharma",
            "title": "Software Engineer",
            "company": "TechMahindra",
            "email": "rahul.sharma@techm.com",
            "linkedin": "https://linkedin.com/in/rahulsharma"
        },
        "neha": {
            "name": "Neha Patel",
            "title": "Data Scientist",
            "company": "Infosys",
            "email": "neha.patel@infosys.com",
            "linkedin": "https://linkedin.com/in/nehapatel"
        }
    }
    query_lower = query.lower()
    return dummy_database.get(query_lower, {})

# === LOGGING FUNCTION ===
def log_to_sheet(prompt, data):
    row = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), prompt, data.get("name"), data.get("title"), data.get("company"), data.get("email"), data.get("linkedin")]
    sheet.append_row(row)

# === TELEGRAM HANDLERS ===
@bot.message_handler(content_types=['text'])
def handle_text(message):
    query = message.text
    bot.send_message(message.chat.id, f"Searching for: {query}")
    data = lookup_apollo_person(query)
    if data:
        formatted = f"Name: {data['name']}\nTitle: {data['title']}\nCompany: {data['company']}\nEmail: {data['email']}\nLinkedIn: {data['linkedin']}"
        bot.send_message(message.chat.id, formatted)
        log_to_sheet(query, data)
    else:
        bot.send_message(message.chat.id, "No results found.")

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    temp_path = f"voice_{message.chat.id}.ogg"
    with open(temp_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    # Convert .ogg to .wav (requires ffmpeg installed)
    wav_path = temp_path.replace('.ogg', '.wav')
    os.system(f"ffmpeg -i {temp_path} {wav_path}")

    query = transcribe_voice(wav_path)
    if not query:
        bot.send_message(message.chat.id, "Sorry, I couldn't understand the voice message.")
        return

    bot.send_message(message.chat.id, f"Searching for: {query}")
    data = lookup_apollo_person(query)
    if data:
        formatted = f"Name: {data['name']}\nTitle: {data['title']}\nCompany: {data['company']}\nEmail: {data['email']}\nLinkedIn: {data['linkedin']}"
        bot.send_message(message.chat.id, formatted)
        log_to_sheet(query, data)
    else:
        bot.send_message(message.chat.id, "No results found.")

    # Clean up temp files
    os.remove(temp_path)
    os.remove(wav_path)

# === FLASK SETUP FOR WEBHOOK ===
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    content = request.json
    query = content.get('query')
    data = lookup_apollo_person(query)
    return jsonify(data)

# === START BOT ===
if __name__ == '__main__':
    print("Bot is running...")
    bot.polling()
# apollo_lookup_bot.py

import telebot
import speech_recognition as sr
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from flask import Flask, request, jsonify
import os

# === CONFIGURATION ===
TELEGRAM_BOT_TOKEN = '7612354488:AAEuncMg-5oq7cm3eRP_0IgS37YW8DF4wGk'  # Must include a colon (e.g., '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11')
GOOGLE_SHEET_NAME = 'Apollo Lookup Logs'

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# === GOOGLE SHEETS SETUP ===
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open(GOOGLE_SHEET_NAME).sheet1

# === SPEECH TO TEXT FUNCTION ===
def transcribe_voice(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language='hi-IN')
    except Exception as e:
        return ""

# === DUMMY PERSON LOOKUP ===
def lookup_apollo_person(query):
    # Simulated response instead of real Apollo API
    dummy_database = {
        "rahul": {
            "name": "Rahul Sharma",
            "title": "Software Engineer",
            "company": "TechMahindra",
            "email": "rahul.sharma@techm.com",
            "linkedin": "https://linkedin.com/in/rahulsharma"
        },
        "neha": {
            "name": "Neha Patel",
            "title": "Data Scientist",
            "company": "Infosys",
            "email": "neha.patel@infosys.com",
            "linkedin": "https://linkedin.com/in/nehapatel"
        }
    }
    query_lower = query.lower()
    return dummy_database.get(query_lower, {})

# === LOGGING FUNCTION ===
def log_to_sheet(prompt, data):
    row = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), prompt, data.get("name"), data.get("title"), data.get("company"), data.get("email"), data.get("linkedin")]
    sheet.append_row(row)

# === TELEGRAM HANDLERS ===
@bot.message_handler(content_types=['text'])
def handle_text(message):
    query = message.text
    bot.send_message(message.chat.id, f"Searching for: {query}")
    data = lookup_apollo_person(query)
    if data:
        formatted = f"Name: {data['name']}\nTitle: {data['title']}\nCompany: {data['company']}\nEmail: {data['email']}\nLinkedIn: {data['linkedin']}"
        bot.send_message(message.chat.id, formatted)
        log_to_sheet(query, data)
    else:
        bot.send_message(message.chat.id, "No results found.")

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    temp_path = f"voice_{message.chat.id}.ogg"
    with open(temp_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    # Convert .ogg to .wav (requires ffmpeg installed)
    wav_path = temp_path.replace('.ogg', '.wav')
    os.system(f"ffmpeg -i {temp_path} {wav_path}")

    query = transcribe_voice(wav_path)
    if not query:
        bot.send_message(message.chat.id, "Sorry, I couldn't understand the voice message.")
        return

    bot.send_message(message.chat.id, f"Searching for: {query}")
    data = lookup_apollo_person(query)
    if data:
        formatted = f"Name: {data['name']}\nTitle: {data['title']}\nCompany: {data['company']}\nEmail: {data['email']}\nLinkedIn: {data['linkedin']}"
        bot.send_message(message.chat.id, formatted)
        log_to_sheet(query, data)
    else:
        bot.send_message(message.chat.id, "No results found.")

    # Clean up temp files
    os.remove(temp_path)
    os.remove(wav_path)

# === FLASK SETUP FOR WEBHOOK ===
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    content = request.json
    query = content.get('query')
    data = lookup_apollo_person(query)
    return jsonify(data)

# === START BOT ===
if __name__ == '__main__':
    print("Bot is running...")
    bot.polling()
