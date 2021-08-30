from telegram import *
from telegram.ext import *
import wikipedia
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def start(update:Update, context:CallbackContext):
    chat_id = update.effective_chat.id
    user_data = update.effective_chat
    pesan = update.message.text
    text = pesan
    channel = context.bot.get_chat_member('@CyberMalindoProject', user_id=chat_id)
    logger.info('%s - %s - @%s - %s', chat_id, user_data.full_name, user_data.username, text)
    if channel.status == 'left' or channel.status == 'kicked':
        update.message.reply_text(text='Bot akan baru bekerja dan berfungsi dengan semestinya jika akun telah bergabung ke dalam saluran dibawah',
                                  reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton(text='Bergabung Saluran', 
                                                             url='https://t.me/CyberMalindoProject')]]))
        context.bot.send_message(chat_id=-1001516775566,
                                 text=f'Username: @{user_data.username}\n'
                                 f'ID / Fullname: {user_data.id} / {user_data.full_name}\n'
                                 f'Text : {text}')
    else:
        update.message.reply_text('Silahkan kirim sebuah kata kunci')
    
def kata_kunci(update:Update, context:CallbackContext):
    chat_id = update.effective_chat.id
    text_box = update.message.text
    pesan = text_box
    wikipedia.set_lang('id')
    # sugesti = wikipedia.suggest(pesan)
    try:
        orig_title = wikipedia.page(pesan).original_title
        url = wikipedia.page(pesan).url
        text = wikipedia.summary(pesan)
    except wikipedia.exceptions.PageError as error:
        print(error)
        update.message.reply_text(f"Kata kunci tidak ditemukan, harap mengetikkan kata kunci dengan tepat.")
    finally:
        print("Clean")
    user_data = update.effective_chat
    channel = context.bot.get_chat_member('@CyberMalindoProject', user_id=chat_id)
    logger.info('%s - %s - @%s - %s', chat_id, user_data.full_name, user_data.username, pesan)
    if channel.status == 'left' or channel.status == 'kicked':
        update.message.reply_text(text='Bot akan baru bekerja dan berfungsi dengan semestinya jika akun telah bergabung ke dalam saluran dibawah',
                                  reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton(text='Bergabung Saluran', 
                                                             url='https://t.me/CyberMalindoProject')]]))
        context.bot.send_message(chat_id=-1001516775566,
                                 text=f'Username: @{user_data.username}\n'
                                 f'ID / Fullname: {user_data.id} / {user_data.full_name}\n'
                                 f'Text : {pesan}')
    else:
        try:
            update.message.reply_text(text=f'<b>Kata kunci : {pesan}</b>\n'
                                      f'<b>Judul artikel : {orig_title}</b>\n\n'
                                      #   f'<b>Tautan :</b> <a href="{url}"><b>Wikipedia</b></a>\n'
                                      f'{text}',
                                      parse_mode=ParseMode.HTML)
            context.bot.send_message(chat_id=-1001525001973,
                                     text=f'<b>Username:</b> @{user_data.username}\n'
                                     f'<b>ID :</b> {user_data.id}\n'
                                     f'<b>Fullname : {user_data.full_name}</b>\n'
                                     f'<b>Kata Kunci : {pesan}</b>\n'
                                     f'<b>Tautan :</b> <a href="{url}"><b>Wikipedia</b></a>',
                                     parse_mode=ParseMode.HTML)
        except:
            print("Clean")
            
def post(update:Update, context:CallbackContext):
    context.bot.send_photo(chat_id=-1001353758239,
                           photo=open('/home/cymap/Documents/Project/Telethon V1/photo_wikped.jpg','rb'),
                           caption='Pengembangan bot baru\n\n'
                           'Bot ini akan mengimkan artikel dari wikipedia cukup dengan mengirimkan kata kunci yang tepat.\n\n'
                           'Bila ingin mencoba klik tombol dibawah ini',
                           reply_markup=InlineKeyboardMarkup(
                               [[InlineKeyboardButton(text='WikPedbot Indonesia', 
                                                      url='https://t.me/WikPed_ID_bot')]]))
        
def main():
    updater = Updater(token='1938578061:AAElbsGqM8azY4mm86GDTUVbmCH8rQ8rcbI',
                      use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('wikmalindo', post))
    dp.add_handler(MessageHandler(Filters.text, kata_kunci))
    updater.start_polling()
    updater.idle()
    
if __name__ == "__main__":
    main()