from aiogram import Router

from .admin import admin_router
from .other import other_router
from .user import user_router

handlers_router = Router()


@handlers_router.startup()
async def __handlers_router_startup(router: Router) -> None:
    router.include_routers(
        admin_router,
        user_router,
        other_router
    )
