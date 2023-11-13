from telethon import TelegramClient, connection
import TelethonFakeTLS

# Use your own values from my.telegram.org
api_id = 2420963
api_hash = 'f0a28529c1aff3bf8b30e53e45030813'

# _proxy = _proxy = ('50.7.42.106', 443, '1603010200010001fc030386e24c3add6170706c652e636f6d')
# _con=TelethonFakeTLS.ConnectionTcpMTProxyFakeTLS
client =TelegramClient('anon', api_id, api_hash)

# client = TelegramClient('anon', api_id, api_hash,proxy=_proxy,connection=_con)

# client = TelegramClient(
#     'anon', api_id, api_hash,
#     connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
#     proxy=('50.7.42.106', 443, '1603010200010001')
# )
# messages=[]

def send_message(message,channal):
    async def main():
        # Getting information about yourself
        me = await client.get_me()
        # You can print the message history of any chat:
        await client.send_message(channal, message)

    with client:
        client.loop.run_until_complete(main())



def get_proxy(messages,channal):
    async def main():
        # Getting information about yourself
        me = await client.get_me()
        counter =0 
        # You can print the message history of any chat:
        async for message in client.iter_messages(channal):
            print(message.id, message.text)
            messages.append(message.text)
            counter = counter +1
            if counter == 4:
                break

            # You can download media from messages, too!
            # The method will return the path where the file was saved.
        

    with client:
        client.loop.run_until_complete(main())

messages=[]
# channal ="https://t.me/DeamNet_proxy"
# get_proxy(messages,channal)
