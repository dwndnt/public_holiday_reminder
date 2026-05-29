import requests
from datetime import datetime, timedelta
from winotify import Notification, audio
import time

API_KEY = "fYSPlOBKKXIDJHxUBGWYUS1fGceUt4oWjZX4YJEY"

countries = {
    "ID": "Indonesia",
    "MY": "Malaysia",
    "SG": "Singapore",
    "FJ": "Fiji",
    "CN": "China",
    "NL": "Netherlands",
    "GB": "United Kingdom"
}

# Ambil tanggal besok
tomorrow = datetime.now() + timedelta(days=1)
target_date = tomorrow.strftime("%Y-%m-%d")

holiday_messages = []

for code, country_name in countries.items():

    url = "https://api.api-ninjas.com/v2/holidays"

    params = {
        "country": code,
        "type": "public_holiday"
    }

    headers = {
        "X-Api-Key": API_KEY
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        print(f"{country_name} -> {response.status_code}")

        if response.status_code != 200:
            print(response.text)
            continue

        holidays = response.json()

        for holiday in holidays:

            holiday_date = holiday.get("date")

            if holiday_date == target_date:

                holiday_name = holiday.get(
                    "name",
                    "Unknown Holiday"
                )

                holiday_messages.append(
                    f"{country_name}: {holiday_name}"
                )

    except Exception as e:
        print(f"Error {country_name}: {e}")

# ======================================
# SHOW WINDOWS TOAST NOTIFICATION
# ======================================

if holiday_messages:

    final_message = "\n".join(holiday_messages)

    toast = Notification(
        app_id="🌏Global Public Holiday",
        title="✨ Public Holiday Notification (All Country)",
        msg=final_message,
        duration="long"
    )

    # Optional sound
    toast.set_audio(audio.Default, loop=False)

    # Optional button
    toast.add_actions(
        label="Open Outlook Calendar",
        launch="https://outlook.office.com/calendar/"
    )

    toast.show()

    print("\n=== PUBLIC HOLIDAY FOUND ===")
    print(final_message)

else:

    toast = Notification(
        app_id="🌏Global Public Holiday",
        title="✨ Public Holiday Notification (All Country)",
        msg="No public holiday tomorrow",
        duration="short"
    )

    toast.set_audio(audio.SMS, loop=False)

    toast.show()

    print("\nNo public holiday tomorrow")

# Delay agar notif sempat muncul
time.sleep(15)