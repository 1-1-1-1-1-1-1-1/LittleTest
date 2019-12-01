import telebot

bot = telebot.TeleBot('707207156:AAErS3Wvvf0tjaU8nwhZJHu-UcFHipdM-b8')

@bot.message_handler (commands = ['start'])
def start_message(message):
    c = message.chat
    bot.send_message (c.id, '''Текущее имя этого чата: {} {}
    Тип чата: {}
    id чата: {}'''.format(c.first_name, c.last_name, c.type, c.id))

bot.polling (none_stop = True)
