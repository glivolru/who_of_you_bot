import os
import random
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, ConversationHandler

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN_BOT')

names = []
ADDING_NAMES, REMOVING_NAMES = range(2)


def load_questions(filename='questions.txt'):
    with open(filename, 'r', encoding='utf-8') as file:
        questions = [line.strip() for line in file.readlines()]
    return questions


questions = load_questions()
used_questions = []


def get_random_question(names_list):
    global used_questions, questions
    if len(used_questions) == len(questions):
        used_questions = []
    available_questions = [q for q in questions if q not in used_questions]
    question_template = random.choice(available_questions)
    used_questions.append(question_template)

    names_str = ', '.join(names_list)
    question = f"{question_template}"
    return question


async def start(update: Update, context: CallbackContext) -> None:
    welcome_message = (
        "Привет!\n"
        "Используй следующие команды для взаимодействия с ботом:\n"
        "/addnames чтобы добавить участников опроса\n"
        "/removenames чтобы удалить участников\n"
        "/listnames чтобы показать текущий список участников\n"
        "/question чтобы задать случайный вопрос с текущим списком участников"
    )
    await update.message.reply_text(welcome_message)


async def prompt_add_names(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Введи имена для добавления, разделенные запятыми')
    return ADDING_NAMES


async def add_names(update: Update, context: CallbackContext) -> int:
    new_names = update.message.text.split(',')
    added_names = []
    for name in new_names:
        name = name.strip()
        if name and name not in names:
            names.append(name)
            added_names.append(name)

    if added_names:
        await update.message.reply_text(f'Добавлены имена: {", ".join(added_names)}')
    else:
        await update.message.reply_text('Ни одно новое имя не было добавлено')

    return ConversationHandler.END


async def prompt_remove_names(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Введи имена для удаления, разделенные запятыми')
    return REMOVING_NAMES


async def remove_names(update: Update, context: CallbackContext) -> int:
    names_to_remove = update.message.text.split(',')
    removed_names = []
    for name in names_to_remove:
        name = name.strip()
        if name in names:
            names.remove(name)
            removed_names.append(name)

    if removed_names:
        await update.message.reply_text(f'Удалены имена: {", ".join(removed_names)}')
    else:
        await update.message.reply_text('Ни одно имя не было удалено.')

    return ConversationHandler.END


async def list_names(update: Update, context: CallbackContext) -> None:
    if len(names) == 0:
        await update.message.reply_text('Список пуст')
    else:
        await update.message.reply_text('Имена: ' + ', '.join(names))


async def ask_question(update: Update, context: CallbackContext) -> None:
    if len(names) == 0:
        await update.message.reply_text('Список имен пуст. Используйте команду /addnames для добавления имен.')
        return

    question = get_random_question(names)

    await context.bot.send_poll(
        chat_id=update.effective_chat.id,
        question=question,
        options=names,
        is_anonymous=True,
        allows_multiple_answers=False
    )


def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("addnames", prompt_add_names)],
        states={
            ADDING_NAMES: [MessageHandler(filters.TEXT & ~filters.COMMAND, add_names)],
        },
        fallbacks=[]
    )

    remove_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("removenames", prompt_remove_names)],
        states={
            REMOVING_NAMES: [MessageHandler(filters.TEXT & ~filters.COMMAND, remove_names)],
        },
        fallbacks=[]
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(conv_handler)
    application.add_handler(remove_conv_handler)
    application.add_handler(CommandHandler("listnames", list_names))
    application.add_handler(CommandHandler("question", ask_question))

    application.run_polling()


if __name__ == '__main__':
    main()
