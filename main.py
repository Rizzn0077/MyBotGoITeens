import os
from settings import *
from aiogram import *
from pytube import YouTube

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, """▰|!⨠ Hello, I am YTLoader. I will download a Youtube video from the URL pasted.
    ▰|!⨠ NOTE: I currently can convert videos only into MP4.
    ▰|!⨠ Paste the URL to start downloading.""")


@dp.message_handler()
async def download_message(message: types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://youtu.be/' or 'https://www.youtube.com/':
        await bot.send_message(chat_id, f"""▰|!⨠ Processing: {yt.title}..""")
    await download_video(url, message, bot)


async def download_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4")
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", 'rb') as video:
        await bot.send_video(message.chat.id, video, caption="*▱ Here is your video. *", parse_mode="Markdown")
        os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")


if __name__ == "__main__":
    executor.start_polling(dp)
