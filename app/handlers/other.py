from aiogram import Router
from aiogram.types import Message

other_router = Router()


@other_router.message()
async def echo_message(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But message not supported
        await message.answer("Not valid")
