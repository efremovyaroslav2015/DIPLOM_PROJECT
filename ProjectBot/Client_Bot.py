from telethon import TelegramClient, events, sync
import pandas as pd
import asyncio


# Вставьте ваш API id и API hash здесь
#api_id = 25198743
#api_hash = "f8a225d6f08d9302928cda0861788ebe"

#TOKEN = "7051789408:AAFzWmd5H1j4nmo4alk5lEY4S1IvK279oBU"
#channel_href = 'https://t.me/tanya_helps'
# Создание клиента
#client = TelegramClient('session_name', api_id, api_hash)


async def main():
    api_id = 25198743
    api_hash = "f8a225d6f08d9302928cda0861788ebe"
    #phone = '+71234567890'
    TOKEN = "7051789408:AAFzWmd5H1j4nmo4alk5lEY4S1IvK279oBU"
    channel_href = 'https://t.me/tanya_helps'

    client = TelegramClient('session_name', api_id, api_hash)
    client = await client.start(bot_token=TOKEN)
    dialogs = await client.get_dialogs()

    channels = {d.entity.username: d.entity
                for d in dialogs
                if d.is_channel}
    my_channel = channel_href.split('/')[-1]
    channel = channels[my_channel]

    members_telethon_list = await client.get_participants(channel, aggressive=True)

    username_list = [member.username for member in members_telethon_list]
    first_name_list = [member.first_name for member in members_telethon_list]
    last_name_list = [member.last_name for member in members_telethon_list]
    phone_list = [member.phone for member in members_telethon_list]

    df = pd.DataFrame()
    df['username'] = username_list
    df['first_name'] = first_name_list
    df['last_name'] = last_name_list
    df['phone'] = phone_list
    df.to_csv('subscribers.csv', index=False)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())