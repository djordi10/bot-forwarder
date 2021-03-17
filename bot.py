from telethon import TelegramClient, events
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
#-569720378
#1201752472
# Remember to use your own values from my.telegram.org!
api_id = 3607299
api_hash = '684e145e5f89a759e89c8fe65c0cc8e8'
#api_id = 3175772
#api_hash ='8c4e8e3bf1c3b3ceac87edc5d5f0fa94'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()
    sender = await event.get_sender()
    chat_id = event.chat_id
    sender_id = event.sender_id
    if chat_id == -1001425186299 and sender_id == -1001425186299:
        print(chat_id)
        print(sender_id)
        print(event.text)
    if chat_id == -1001425186299 and sender_id == -1001425186299:
        await client.forward_messages(-421139059, "bot\n" + event.text)
        await client.forward_messages(-569720378, "bot\n" + event.text)


client.start()
client.run_until_disconnected()