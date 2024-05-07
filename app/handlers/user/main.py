import logging

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, URLInputFile

from data import Messages
from tiktok import TikTok

user_router = Router()


@user_router.message(CommandStart())
async def __start(message: Message) -> None:
    await message.answer(Messages.START)


@user_router.message(Command('help'))
async def __help(message: Message) -> None:
    await __start(message)


# https://(vm/vt).tiktok.com/******/
@user_router.message(F.text.regexp(r'^.*https:\/\/(?:|vt|vm)?\.?tiktok\.com\/((?:.*\b(\d+))|\w+)./*'))
async def __get_video_message(message: Message) -> None:
    await message.answer(Messages.PLEASE_WAIT)
    content_saver = TikTok()
    try:
        video = await content_saver.get_content_from_shared_link(message.text)
        await message.answer_video(URLInputFile(video[0]))
    except Exception as exception:
        logging.error(exception)
        await message.answer(Messages.ERROR)


@user_router.message()
async def __not_link_message(message: Message) -> None:
    await message.answer(Messages.NOT_LINK)
