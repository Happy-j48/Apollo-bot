

# Apollo People Lookup Bot

## Overview

This project implements an AI-powered **Apollo People Lookup Bot** that allows users to retrieve personal details (name, title, company, email, LinkedIn) based on a person's name or email address. The bot accepts **voice** or **text** inputs and fetches data from the **FullContact API**. The results are sent back to the user and logged to a **Google Sheet** for record-keeping.

## Features

* **Voice and Text Input Support**: Accepts both text and voice queries (in Hindi/English).
* **FullContact API Integration**: Retrieves data such as name, title, company, email, and LinkedIn profile.
* **Google Sheets Logging**: Logs each query and result into a Google Sheet with timestamped entries.
* **Webhook Option**: Flask-based webhook integration for easy integration with automation tools like **n8n** or **Make.com**.

## Requirements

1. Python 3.x
2. **Telegram Bot Token**: Create a Telegram bot using [BotFather](https://core.telegram.org/bots#botfather).
3. **FullContact API Key**: Sign up on [FullContact](https://www.fullcontact.com/) and get an API key for person lookup.
4. **Google Sheets API Access**: Set up Google Sheets API and download your `credentials.json` for authentication.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/apollo-lookup-bot.git
cd apollo-lookup-bot
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# MacOS/Linux
source .venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Configure the Bot

* Replace the placeholders in `apollobot.py` with your actual **Telegram Bot Token** and **FullContact API Key**.

```python
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
FULLCONTACT_API_KEY = 'YOUR_FULLCONTACT_API_KEY'
GOOGLE_SHEET_NAME = 'Apollo Lookup Logs'
```

* Download **Google Sheets API credentials** and place the `credentials.json` file in the project directory.

### 5. Run the Bot

```bash
python apollo_lookup_bot.py
```

### 6. Testing

* Send **text** queries like "Find details of Sundar Pichai" or "Email of Sam Altman" to your bot.
* Send **voice** messages, and the bot will transcribe them to text and search for results.
* View logs in the Google Sheet under the name `Apollo Lookup Logs`.

### 7. Webhook Setup (Optional)

If you want to integrate the bot with **n8n** or **Make.com**:

1. Set up your webhook server (Flask).
2. Use the `/webhook` endpoint to send queries and receive results as JSON.

Example:

```bash
POST /webhook
{
  "query": "Sundar Pichai"
}
```

---

## Project Structure

```
apollo-lookup-bot/
│
├── apollo_lookup_bot.py      # Main bot script
├── requirements.txt          # Python dependencies
├── credentials.json          # Google Sheets API credentials
└── README.md                 # This file
```

---

## Future Improvements

* Implement more APIs for enriched data lookup.
* Add language support for other languages.
* Deploy bot to a cloud platform (Heroku/Render) for continuous operation.
* Provide a more detailed logging system with error tracking.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Let me know if you'd like further adjustments to the **README**!
