import logging

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, URLInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from data import Messages
from tiktok import TikTok, ContentType
from utils import split_array_into_groups

user_router = Router()


@user_router.message(CommandStart())
async def __start(message: Message) -> None:
    await message.answer(Messages.START)


@user_router.message(Command('help'))
async def __help(message: Message) -> None:
    await __start(message)


@user_router.message(F.text.regexp(
    r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*'))
async def __get_media_message(message: Message) -> None:
    try:
        await message.answer(Messages.MEDIA_FIND)

        tiktok = TikTok(message.text).get_content
        await tiktok.make_content()

        if await tiktok.content_type == ContentType.NONE:
            await message.answer(Messages.ERROR)
            return None

        await message.answer(Messages.MEDIA_SUCCESS)

        if await tiktok.is_video:
            video = await tiktok.video
            await message.answer_video(URLInputFile(video.media))

        elif await tiktok.is_photos:
            photos = await tiktok.photos
            photos_groups = split_array_into_groups(photos.media, 10)

            for photos_group in photos_groups:
                media_group = MediaGroupBuilder()
                for photo in photos_group:
                    media_group.add_photo(media=URLInputFile(photo))

                await message.answer_media_group(media=media_group.build())
            await message.answer(Messages.ALL_PHOTOS_SENT)
    except Exception as exception:
        logging.error(exception)
        await message.answer(Messages.ERROR)


@user_router.message()
async def __not_link_message(message: Message) -> None:
    await message.answer(Messages.NOT_LINK)
