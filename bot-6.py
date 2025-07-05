import asyncio
import logging
import os
import re
import sys
from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from dotenv import load_dotenv

# Константы
SOURCES_FILE = 'sources.txt'
TARGETS_FILE = 'targets.txt'
SIGNATURE_FILE = 'signature.txt'
ADMIN_ID = 6385514050  # Замените на ваш ID

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Загрузка переменных окружения
load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
SESSION_STRING = os.getenv('SESSION_STRING')

if not all([API_ID, API_HASH, BOT_TOKEN, SESSION_STRING]):
    logger.error("Не все переменные окружения заданы!")
    raise ValueError("Не все переменные окружения заданы!")

# Функции для работы с данными
def load_signature():
    try:
        with open(SIGNATURE_FILE, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except:
        return "Хочешь такой же бот? Обращайся - @Russkayamednayakompaniya"

def save_signature(text):
    with open(SIGNATURE_FILE, 'w', encoding='utf-8') as f:
        f.write(text)

def load_list(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except:
        return []

def save_list(items, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in items:
            f.write(f"{item}\n")

def clean_text(text):
    return re.sub(r'http\S+|t\.me\S+|@\S+', '', text).strip() if text else ""

# Основной класс бота
class ForwardBot:
    def __init__(self):
        self.client = TelegramClient(
            StringSession(SESSION_STRING),
            int(API_ID),
            API_HASH
        )
        self.bot = None
        self.sources = load_list(SOURCES_FILE)
        self.targets = load_list(TARGETS_FILE)
        self.signature = load_signature()
        
    async def start(self):
        await self.client.start(bot_token=BOT_TOKEN)
        self.bot = await self.client.get_me()
        logger.info(f"Бот запущен: @{self.bot.username}")
        
        # Регистрация обработчиков
        self.client.add_event_handler(
            self.handle_admin_command,
            events.NewMessage(pattern=r'^/start$', from_users=[ADMIN_ID])
        )
        self.client.add_event_handler(
            self.handle_new_message,
            events.NewMessage(chats=self.sources)
        )
        
        # Запуск мониторинга
        await self.client.run_until_disconnected()
    
    async def handle_admin_command(self, event):
        command = event.message.message.strip()
        
        if command == '/start':
            await self.show_main_menu(event)
            
        elif command == '/add_source':
            await event.respond("Введите @username канала-донора:")
            self.next_handler = self.add_source_handler
            
        elif command == '/add_target':
            await event.respond("Введите @username целевого канала:")
            self.next_handler = self.add_target_handler
            
        elif command == '/set_signature':
            await event.respond(f"Текущая подпись: {self.signature}\n\nВведите новую подпись:")
            self.next_handler = self.set_signature_handler
            
        elif command == '/check_status':
            await self.check_status(event)
    
    async def handle_next_message(self, event):
        if hasattr(self, 'next_handler'):
            await self.next_handler(event)
            delattr(self, 'next_handler')
    
    async def add_source_handler(self, event):
        source = event.message.message.strip()
        if not source.startswith('@'):
            source = f"@{source}"
            
        if source in self.sources:
            await event.respond("⚠️ Этот источник уже добавлен")
        else:
            self.sources.append(source)
            save_list(self.sources, SOURCES_FILE)
            await event.respond(f"✅ Добавлен источник: {source}")
        await self.show_main_menu(event)
    
    async def add_target_handler(self, event):
        target = event.message.message.strip()
        if not target.startswith('@'):
            target = f"@{target}"
            
        if target in self.targets:
            await event.respond("⚠️ Этот канал уже добавлен")
        else:
            self.targets.append(target)
            save_list(self.targets, TARGETS_FILE)
            await event.respond(f"✅ Добавлен канал: {target}")
        await self.show_main_menu(event)
    
    async def set_signature_handler(self, event):
        self.signature = event.message.message.strip()
        save_signature(self.signature)
        await event.respond(f"✅ Подпись обновлена!\nНовая подпись: {self.signature}")
        await self.show_main_menu(event)
    
    async def check_status(self, event):
        status = (
            f"📊 Статус бота:\n\n"
            f"🔗 Источников: {len(self.sources)}\n"
            f"📌 Приемников: {len(self.targets)}\n"
            f"✏️ Подпись: {self.signature}\n\n"
            f"🤖 Бот работает нормально!"
        )
        await event.respond(status)
    
    async def show_main_menu(self, event):
        buttons = [
            [Button.inline("📝 Добавить донора", b"add_source")],
            [Button.inline("📝 Добавить канал", b"add_target")],
            [Button.inline("⚙️ Подпись", b"set_signature")],
            [Button.inline("🔄 Проверить", b"check_status")]
        ]
        text = (
            "🤖 Бот для автоматической пересылки сообщений\n\n"
            f"🔗 Источников: {len(self.sources)}\n"
            f"📌 Приемников: {len(self.targets)}\n"
            f"✏️ Подпись: {self.signature}"
        )
        await event.respond(text, buttons=buttons)
    
    async def handle_callback(self, event):
        data = event.data.decode('utf-8')
        
        if data == 'add_source':
            await event.respond("Введите @username канала-донора:")
            self.next_handler = self.add_source_handler
            
        elif data == 'add_target':
            await event.respond("Введите @username целевого канала:")
            self.next_handler = self.add_target_handler
            
        elif data == 'set_signature':
            await event.respond(f"Текущая подпись: {self.signature}\n\nВведите новую подпись:")
            self.next_handler = self.set_signature_handler
            
        elif data == 'check_status':
            await self.check_status(event)
    
    async def handle_new_message(self, event):
        if not self.targets:
            return
            
        text = clean_text(event.message.text)
        final_text = f"{text}\n\n{self.signature}" if text else self.signature
        
        if event.message.media:
            for target in self.targets:
                try:
                    await event.client.send_file(
                        target,
                        event.message.media,
                        caption=final_text
                    )
                    logger.info(f"Медиа отправлено в {target}")
                except Exception as e:
                    logger.error(f"Ошибка отправки медиа в {target}: {e}")
        else:
            for target in self.targets:
                try:
                    await event.client.send_message(
                        target,
                        final_text
                    )
                    logger.info(f"Текст отправлен в {target}")
                except Exception as e:
                    logger.error(f"Ошибка отправки текста в {target}: {e}")

if __name__ == '__main__':
    # Замените на ваш ID в Telegram
    ADMIN_ID = 6385514050  # Ваш реальный ID
    
    bot = ForwardBot()
    loop = asyncio.get_event_loop()
    
    try:
        loop.run_until_complete(bot.start())
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
    finally:
        logger.info("Приложение полностью остановлено")
        sys.exit(0)