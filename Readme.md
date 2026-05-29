# 🌏 Global Public Holiday Notifier

A simple Python-based desktop notification app that reminds you about upcoming public holidays across multiple countries using the API Ninjas Holidays API and Windows Toast Notification.

## ✨ Features

* 🌍 Multi-country public holiday monitoring
* 🔔 Windows toast notification popup
* 📅 Checks tomorrow's public holiday automatically
* 🎵 Notification sound support
* 📌 Outlook Calendar quick access button
* ⚡ Lightweight and simple Python script

---

## 🌎 Supported Countries

Currently configured for:

* 🇮🇩 Indonesia
* 🇲🇾 Malaysia
* 🇸🇬 Singapore
* 🇫🇯 Fiji
* 🇨🇳 China
* 🇳🇱 Netherlands
* 🇬🇧 United Kingdom

You can easily add more countries using ISO country codes.

---

## 🛠 Requirements

* Python 3.10+
* Windows 10 / 11

---

## 📦 Installation

Install dependencies:

```bash
pip install requests winotify
```

---

## 🔑 API Key Setup

This project uses the Ninjas Holidays API.

Get your free API key from:

https://api-ninjas.com/

Then replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your own API key.

---

## ▶️ Run the Script

```bash
py holiday_notifier.py
```

---

## 🔔 Example Notification

```text
✨ Public Holiday Notification (All Country)

Indonesia: Independence Day
Singapore: National Day
China: Mid-Autumn Festival
```

---

## ⚙️ Automation (Recommended)

Use Windows Task Scheduler to automatically run the script every morning.

### Suggested Schedule

* Trigger: Daily
* Time: 08:00 AM

### Program

```text
py
```

### Arguments

```text
C:\path\holiday_notifier.py
```

---

## 📁 Project Structure

```text
.
├── holiday_notifier.py
└── README.md
```

---

## 🚀 Future Improvements

* System tray application
* GUI dashboard
* Teams / Slack integration
* Outlook calendar sync
* Holiday countdown
* Deployment freeze alerts
* Export to Excel / CSV
* Executable (.exe) version

## 🤝 Contributing

Pull requests and suggestions are welcome.

Feel free to fork and improve the project.
