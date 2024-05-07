from abc import ABC
from dataclasses import dataclass
from typing import Final


@dataclass
class Messages(ABC):
    START: Final = ('<b>🌟 Привет! Добро пожаловать в нашего бота, который'
                    'поможет тебе сохранить видео из тиктока!</b>\n\n'
                    '🎥 Просто отправь мне ссылку на видео, и я помогу тебе сохранить его.\n'
                    '⚡️ Воспользуйся удобным функционалом бота и наслаждайся просмотром любимых видео!\n\n'
                    '✨ <b>Автор проекта - @InDigitalE8! 🤵🏻</b>')
    PLEASE_WAIT: Final = 'Понял, начинаю скачивать! 😉'
    ERROR: Final = 'Упс, произошла ошибка :('
    NOT_LINK: Final = "Я видео по ссылке скачиваю, походу это не то, друг"
