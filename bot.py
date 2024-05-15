token = 'MTIzNjU3OTM4OTYzMDU3ODY4OA.Gvgxnj.ZTteVIcrkjUM7B-QF45zCzQz84-KuLf8IHpTIc'

import discord

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send(f"Yahoo, selamat datang!, {client.user}. Ada yang bisa aku bantuuu?")
    elif message.content.startswith('$bye'):
        await message.channel.send("Dadang!, sampai jumpa kembali, wahai teman online ku.")
    else:
        await message.channel.send(message.content)

client.run(token)
