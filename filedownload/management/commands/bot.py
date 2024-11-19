from django.core.management.base import BaseCommand
from django.conf import settings
from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
import telegram.ext.filters as filters
import os

from htmlproject.filedownload.models import Libr

library = [i[:len(i) - 4] for i in os.listdir() if (i[len(i) - 4:] == ".pdf")]

token = "6830769935:AAHaGnUj-nblOoBeM4eaDT0dopjCN5lNhw0"
bot = Updater(token, use_context=True)

def nospaces(string):
    return string.replace(" ", "")

def welcoming(update: Update, context: CallbackContext):
    update.message.reply_text("Privet")
    update.message.reply_text("kuku")
    books = Libr.objects.order_by('id')
    for el in books:
        update.message.reply_text(el.title)
    print("start")

def choosefile(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    i = update.message.text
    print(len(library))
    if (i.isnumeric() and float(i) == int(i) and int(i) >= 1 and int(i) <= len(library)):
        i = int(i)
        document = open(library[i - 1]+".pdf", "rb")
        context.bot.send_document(chat_id, document)
        update.message.reply_text("Uploading complete, you may download now")
        return
    else:
        for ind in range(len(library)):
            if nospaces(i.lower()) == nospaces(library[ind].lower()):
                document = open(library[ind] + ".pdf", "rb")
                context.bot.send_document(chat_id, document)
                update.message.reply_text("Uploading complete, you may download now")
                return
        update.message.reply_text("Invalid input data")

def upload(update: Update, context: CallbackContext):
    update.message.reply_text("Please, specify the number or full name of the book(as it is mentioned on the list)")
    bot.dispatcher.add_handler(MessageHandler(filters.Filters.text, choosefile))

def listbooks(update: Update, context: CallbackContext):
    s = ""
    for i in range(len(library)):
        s = s + str(i + 1) + ". " + library[i] + "\n"
    update.message.reply_text(s)

def download(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    filename = update.message.document.file_name
    file = update.message.effective_attachment.get_file()
    file.download(filename)
    library.append(filename[:len(filename) - 4])
    update.message.reply_text("Book has been added successfully")

class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        bot.dispatcher.add_handler(CommandHandler("upload", upload))
        bot.dispatcher.add_handler(CommandHandler("list", listbooks))
        bot.dispatcher.add_handler(CommandHandler("start", welcoming))
        bot.dispatcher.add_handler(MessageHandler(filters.Filters.document, download))
        books = Libr.objects.order_by('id')
        print(books)
        bot.start_polling()