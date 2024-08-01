import logging

from aiogram import Bot, Dispatcher
from aiogram import Router
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from app.handlers import handlers_router
from app.middlewares import register_main_middlewares
from data import config


async def __on_startup(router: Router) -> None:
    router.include_router(handlers_router)
    register_main_middlewares(router)

    logging.info('Bot starts')


async def __on_shutdown(router: Router) -> None:
    logging.info('Bot shutdown')


async def run_bot() -> None:
    """
    Run telegram bot (start polling)
    """
    session = AiohttpSession(proxy=None)
    try:
        bot: Bot = Bot(
            token=config.bot_token.get_secret_value(),
            session=session,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )

        dp = Dispatcher(storage=MemoryStorage())
        dp.startup.register(__on_startup)
        dp.shutdown.register(__on_shutdown)

        await bot.delete_webhook(drop_pending_updates=True)
        return await dp.start_polling(bot)

    except Exception as exception:
        logging.error(exception)
        await session.close()
