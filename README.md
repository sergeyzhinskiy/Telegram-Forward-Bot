# Telegram-Forward-Bot
Automated bot for sending content between Telegram channels with the addition of a signature
# Telegram Forward Bot 🔄

Автоматизированный бот для пересылки контента между Telegram-каналами с добавлением подписи. Поддерживает текстовые сообщения, фото и документы.

## 🔍 Особенности функционала
- **Кросс-канальная пересылка**  
  Автоматическая ретрансляция контента из источников в целевые каналы
- **Кастомная подпись**  
  Добавление уникальной подписи ко всем пересланным сообщениям
- **Гибкое управление**  
  Интерактивное меню для управления настройками
- **Поддержка медиа**  
  Пересылка фото и документов с сохранением исходного качества
- **Очистка текста**  
  Автоматическое удаление ссылок и упоминаний из пересылаемых сообщений
- **Логирование операций**  
  Детальное отслеживание всех действий в лог-файле

```text

## 💡 Ключевые преимущества решения
- **Экономия времени** - Автоматизация рутинного постинга
- **Консистентность** - Единый стиль сообщений с брендированной подписью
- **Масштабируемость** - Работа с неограниченным количеством каналов
- **Простота управления** - Интуитивное меню без технических навыков

Проект идеально подходит для:
- Маркетологов, ведущих несколько каналов
- Новостных агрегаторов
- Комьюнити-менеджеров
- Партнерских программ
- Инфобизнес-проектов
```

## ⚙️ Технические требования
- Python 3.10+
- Telethon 1.34+
- dotenv
- Доступ к Telegram API

## 🚀 Быстрый старт

### 1. Установка зависимостей
```bash
pip install telethon python-dotenv
```
**2. Настройка окружения**
Создайте файл .env со следующими параметрами:

```ini
API_ID=ваш_telegram_api_id
API_HASH=ваш_telegram_api_hash
BOT_TOKEN=токен_вашего_botfather
SESSION_STRING=строка_сессии_telethon
```
**3. Создание файлов конфигурации**
```bash
touch sources.txt targets.txt signature.txt
```

**4. Запуск бота**
```bash
python bot-6.py
```
**🛠 Конфигурация файлов**

sources.txt
Список каналов-доноров (по одному на строку):

```text
@channel1
@channel2
https://t.me/channel3
```
targets.txt

Список целевых каналов:

```text
@target_channel1
@my_private_channel
```
signature.txt
Текстовая подпись для всех сообщений:

```text
📢 Подписывайтесь на @NewsChannel!
```
**🎮 Управление ботом**

Администраторские команды:
/start - Главное меню управления

/add_source - Добавить канал-источник

/add_target - Добавить целевой канал

/set_signature - Изменить подпись

/check_status - Проверить статус бота

Интерактивное меню:
```plaintext
🤖 Бот для автоматической пересылки сообщений

🔗 Источников: 3
📌 Приемников: 2
✏️ Подпись: Хочешь такой же бот? @Creator

[📝 Добавить донора] [📝 Добавить канал]
[⚙️ Подпись] [🔄 Проверить]
```
**🔄 Принцип работы**

Бот мониторит указанные каналы-источники

При появлении нового сообщения:

Текст очищается от ссылок и упоминаний

Добавляется кастомная подпись

Контент пересылается во все целевые каналы

**Поддерживаемые типы контента:**


Текстовые сообщения

Фотографии (с подписью)

Документы (PDF, ZIP и др.)

**📂 Структура проекта**
```text
├── bot-6.py             # Основной скрипт бота
├── .env                 # Конфигурация окружения (не в репозитории)
├── sources.txt          # Список каналов-источников
├── targets.txt          # Список целевых каналов
├── signature.txt        # Текст подписи
├── bot.log              # Лог-файл операций
└── README.md            # Документация
```
**⚠️ Важные особенности**

Права доступа:
Бот должен быть администратором в целевых каналах

Ограничения Telegram:

Пересылка из каналов с ограниченным доступом невозможна

Лимит на отправку сообщений (∼30 сообщений/сек)


**💡 Возможные доработки**

Добавление фильтров по ключевым словам

Поддержка отложенной публикации

Интеграция с базами данных

Автоматическая модерация контента

Статистика пересылаемых сообщений

Обработка видео и голосовых сообщений

Система черного списка

**👨‍💻 Техническая поддержка**

При возникновении проблем:

Проверьте права доступа бота

Убедитесь в правильности форматов файлов

Просмотрите логи в bot.log

**Для профессиональной поддержки:**
@Russkayamednayakompaniya

Версия: 1.0
Обновлено: 15.05.2024
Лицензия: MIT

==================================

# Telegram Forward Bot 🔄

Automated bot for forwarding content between Telegram channels with the addition of a signature. Supports text messages, photos and documents.

## 🔍 Features
- **Cross-channel forwarding**
Automatic retransmission of content from sources to target channels
- **Custom signature**
Adding a unique signature to all forwarded messages
- **Flexible management**
Interactive menu for managing settings
- **Media support**
Forwarding photos and documents while maintaining the original quality
- **Text cleaning**
Automatic removal of links and mentions from forwarded messages
- **Operation logging**
Detailed tracking of all actions in the log file

```text

## 💡 Key advantages of the solution
- **Time saving** - Automation of routine posting
- **Consistency** - Uniform message style with a branded signature
- **Scalability** - Working with an unlimited number of channels
- **Ease of management** - Intuitive menu without technical skills

The project is ideal for:
- Marketers running multiple channels
- News aggregators
- Community managers
- Affiliate programs
- Infobusiness projects
```

## ⚙️ Technical requirements
- Python 3.10+
- Telethon 1.34+
- dotenv
- Access to Telegram API

## 🚀 Quick start

### 1. Installing dependencies
```bash
pip install telethon python-dotenv
```
**2. Environment Setup**
Create a .env file with the following parameters:

```ini
API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
BOT_TOKEN=your_botfather_token
SESSION_STRING=telethon_session_string
```
**3. Creating Configuration Files**
```bash
touch sources.txt targets.txt signature.txt
```

**4. Launching the bot**
```bash
python bot-6.py
```
**🛠 File configuration**

sources.txt
List of donor channels (one per line):

```text
@channel1
@channel2
https://t.me/channel3
```
targets.txt

List of target channels:

```text
@target_channel1
@my_private_channel
```
signature.txt
Text signature for all messages:

```text
📢 Follow @NewsChannel!
```
**🎮 Bot management**

Administrator commands:

/start - Main control menu

/add_source - Add source channel

/add_target - Add target channel

/set_signature - Change signature

/check_status - Check bot status

Interactive menu:
```plaintext
🤖 Bot for automatic message forwarding

🔗 Sources: 3
📌 Receivers: 2
✏️ Signature: Want the same bot? @Creator

[📝 Add donor] [📝 Add channel]
[⚙️ Signature] [🔄 Check]
```
**🔄 How it works**

The bot monitors the specified source channels

When a new message appears:

The text is cleared of links and mentions

A custom signature is added

Content is forwarded to all target channels

**Supported content types:**

Text messages

Photos (with signature)

Documents (PDF, ZIP, etc.)

**📂 Project structure**
```text
├── bot-6.py # Main bot script
├── .env # Environment configuration (not in the repository)
├── sources.txt # List source channels
├── targets.txt # List of target channels
├── signature.txt # Signature text
├── bot.log # Operations log file
└── README.md # Documentation
```
**⚠️ Important features**

Access rights:
The bot must be an administrator in the target channels

Telegram restrictions:

Forwarding from channels with limited access is not possible

Limit on sending messages (∼30 messages/sec)

**💡 Possible improvements**

Adding filters by keywords

Support for delayed publication

Integration with databases

Automatic content moderation

Statistics of forwarded messages

Processing video and voice messages

Blacklist system list

**👨‍💻 Technical support**

If you have problems:

Check the bot's access rights

Make sure the file formats are correct

View the logs in bot.log

**For professional support:**
@Russkayamednayakompaniya

Version: 1.0
Updated: 05/15/2024
License: MIT
