import os
from pyrogram import Client

api_id = os.environ.get('API_ID', '22469064')
api_hash = os.environ.get('API_HASH', 'c05481978a217fdb11fa6774b15cba32')
bot_token = os.environ.get('BOT_TOKEN', '7542241757:AAFgeHI2tr518Hbh8DOvLIfeCpQj0udfk-Y')
app = Client(
    "teraBox-Bypass",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token,
)
try:
    app.start()
    print(app.export_session_string())
finally:
    app.stop()
