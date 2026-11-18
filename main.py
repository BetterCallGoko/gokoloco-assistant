import requests

BOT_TOKEN = "9282427240:AAGAOmLaouOWT2V1qaWzZfudgUKnS3743yY"
CHAT_ID = "6040591739"

message = """🌅 Günaydın Gökhan!

Bu ilk test mesajıdır.
Bot başarıyla çalışıyor. 🎉
"""

url = f"https://api.telegram.org/bot{9282427240:AAGAOmLaouOWT2V1qaWzZfudgUKnS3743yY}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
