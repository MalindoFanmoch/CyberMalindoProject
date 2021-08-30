from deep_translator import GoogleTranslator
from telegram import *
from telegram.ext import *
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

Penerjemah = '1971999313:AAHb-QxwJWUW_wjWoLLYdLwMSHnxwPOn4ew'

def start(update:Update, context:CallbackContext):
    username = update.effective_chat.username
    chat_id = update.effective_chat.id
    msg = update.message.text
    logger.info('%s - %s - @%s - %s', chat_id, update.message.from_user.full_name, username, msg)
    trans = GoogleTranslator(source='auto', target='id').translate(msg)
    channel = context.bot.get_chat_member('@CyberMalindoProject', update.message.from_user.id)
    if channel.status == 'left' or channel.status == 'kicked':
        update.message.reply_text(text='Bot akan baru bekerja dan berfungsi dengan semestinya jika akun telah bergabung ke dalam saluran dibawah.',
                                  reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton(text='Bergabung', 
                                                             url='https://t.me/CyberMalindoProject')]]))
    else:
        update.message.reply_text('Silahkan kirim sebuah kata atau kalimat bahasa apapun yang akan diterjemahkan.')

def terjemahan(update:Update, context:CallbackContext):
    username = update.effective_chat.username
    chat_id = update.effective_chat.id
    Pesan = update.message.text
    pesan = Pesan
    logger.info('%s - %s - @%s - %s', chat_id, update.message.from_user.full_name, username, pesan)
    trans = GoogleTranslator(source='auto', target='id').translate(pesan)
    channel = context.bot.get_chat_member('@CyberMalindoProject', chat_id)
    if channel.status == 'left' or channel.status == 'kicked':
        update.message.reply_text(text='Bot akan baru bekerja dan berfungsi dengan semestinya jika akun telah bergabung ke dalam saluran dibawah.',
                                  reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton(text='Bergabung', 
                                                             url='https://t.me/CyberMalindoProject')]]))
    else:
        context.bot.send_chat_action(chat_id, action=ChatAction.TYPING)
        update.message.reply_text(text=f'{trans}')
        context.bot.send_message(chat_id=-1001500415829,
                                 text=f'<b>Kata/Kalimat :</b>\n'
                                 f'{str(pesan)}\n'
                                 f'<b>Terjemahan :</b>\n'
                                 f'{trans}\n'
                                 f'<b>Full name :</b> {update.message.from_user.full_name}\n'
                                 f'<b>Username :</b> @{username}\n'
                                 f'<b>Chat ID :</b> {update.message.from_user.id}',
                                 parse_mode=ParseMode.HTML)

def main():
    updater = Updater(token=Penerjemah, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, terjemahan))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()

# from deep_translator import GoogleTranslator
# trasn = GoogleTranslator(source='id', target='en', proxies=None).translate('Lemari')
# print(trasn)