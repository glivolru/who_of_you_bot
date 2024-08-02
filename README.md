# WhoBot

## Описание

WhoBot - это Telegram-бот, который создает забавные и интересные опросы для чата друзей или личных сообщений.

## Функциональность

- Делает забавные опросы для чата друзей или для ЛС

## Технологии использованные в проекте

- python-telegram-bot
- openai

## Установка и настройка

### Требования

- Python 3.6 или выше
- Учетная запись Telegram и созданный бот с токеном доступа (получить токен можно у [BotFather](https://core.telegram.org/bots#botfather))
- OpenAI API ключ (можно получить на [OpenAI](https://beta.openai.com/signup/))

### Установка

1. Клонируйте репозиторий или скачайте код.

2. Установите зависимости:

    ```bash
    pip install python-telegram-bot openai
    ```

3. Настройте переменные окружения для токенов. Создайте файл `.env` в корневой папке проекта и добавьте в него следующие строки:

    ```env
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    OPENAI_API_KEY=your_openai_api_key
    ```

### Запуск

1. Запустите скрипт:

    ```bash
    python bot.py
    ```

2. Отправьте команду `/question` вашему боту в Telegram, чтобы получить случайный вопрос.

---

# WhoBot

## Description

WhoBot is a Telegram bot that creates fun and interesting polls for a friends' chat or personal messages.

## Functionality

- Creates fun polls for a friends, chat or personal messages

## Technologies Used

- python-telegram-bot
- openai

## Installation and Setup

### Requirements

- Python 3.6 or higher
- A Telegram account and a created bot with an access token (get the token from [BotFather](https://core.telegram.org/bots#botfather))
- OpenAI API key (you can get it at [OpenAI](https://beta.openai.com/signup/))

### Installation

1. Clone the repository or download the code.

2. Install the dependencies:

    ```bash
    pip install python-telegram-bot openai
    ```

3. Set up environment variables for the tokens. Create a `.env` file in the root folder of the project and add the following lines:

    ```env
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    OPENAI_API_KEY=your_openai_api_key
    ```

### Running

1. Run the script:

    ```bash
    python bot.py
    ```

2. Send the `/question` command to your bot in Telegram to receive a random question.