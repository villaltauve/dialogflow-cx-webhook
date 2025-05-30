# 🤖 Dialogflow CX Bot + Python Webhook

This project demonstrates how to connect a **Dialogflow CX** agent with a **Python Flask webhook** that captures user data (name, age, email) and saves it in a CSV file.

## 📌 Features

- Multi-step bot using Dialogflow CX Pages
- Parameter capturing: name, age, email
- Age validation (must be 21 or older)
- Webhook built in Python with Flask
- Data storage in `datos.csv`
- Exposed publicly using [Ngrok](https://ngrok.com)

---

## 🛠 Requirements

- Python 3.8 or higher
- Flask (`pip install flask`)
- Ngrok (for testing webhook remotely)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/dialogflow-cx-webhook.git
cd dialogflow-cx-webhook
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) Add `.env` for custom config

---

## 🚀 Running the Webhook

1. Start the Flask webhook locally:

```bash
python webhook.py
```

2. In another terminal, expose it using Ngrok:

```bash
ngrok http 5000
```

3. Copy the generated HTTPS URL (e.g., `https://abcd1234.ngrok.io`)

4. In **Dialogflow CX Console**:
   - Go to **Manage > Webhooks**
   - Click **Create Webhook**
   - Name: `GuardarDatos`
   - URL: `https://abcd1234.ngrok.io/webhook`
   - Method: `POST`
   - Authentication: `None` (for local testing)

---

## 🧠 Dialogflow CX Setup Summary

- Use **Pages** to ask for:
  - Name (`@sys.any`)
  - Age (`@sys.number`)
  - Email (`@sys.email`)
- Use **conditions** to reject users under 18
- In the final page (e.g., `ResumenPage`), call the webhook via **Entry Fulfillment**

---

## 🗂 Project Structure

```
.
├── webhook.py           # Flask server
├── requirements.txt     # Python dependencies
├── datos.csv            # Generated CSV file with user info
├── .gitignore           # Excludes CSV and cache files
└── README.md            # Instructions
```

---

## 📝 Notes

- `datos.csv` will be created automatically after the first request
- Parameters are extracted from `sessionInfo.parameters` in the webhook
- You can expand the project to:
  - Connect to a database (SQLite, MySQL)
  - Send confirmation emails
  - Save data in Google Sheets

---

## 📄 License

MIT License
