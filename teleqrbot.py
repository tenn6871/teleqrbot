from telegram.ext import Updater, MessageHandler, Filters
import qrcode

up = Updater(token='KEY')
disp = up.dispatcher
up.start_polling()

def handler(bot, up):
  text = up.message.text
  cid = up.message.chat_id
  len(text)
  test = len(text)
  
  if '3E' in text:
    print(text)
    print(len(text))
    print(test)
    print(test[-1])
    barcode = qrcode.make(text)
    barcode.save("barcode/text.png")
    bot.send_photo(chat_id=cid, photo=open('/home//python/barcode/text.png', 'rb'))
  elif '3M' in text:
    barcode = qrcode.make(text)
    barcode.save("barcode/text.png")
    bot.send_photo(chat_id=cid, photo=open('/home//python/barcode/text.png', 'rb'))
  elif '2E' in text:
    barcode = qrcode.make(text)
    barcode.save("barcode/text.png")
    bot.send_photo(chat_id=cid, photo=open('/home//python/barcode/text.png', 'rb'))
  elif '1E' in text:
    barcode = qrcode.make(text)
    barcode.save("barcode/text.png")
    bot.send_photo(chat_id=cid, photo=open('/home//python/barcode/text.png', 'rb'))
  else:
    bot.send_message(chat_id=cid, text='다시 입력해줘')
    
echo_handler = MessageHandler(Filters.text, handler)
disp.add_handler(echo_handler)
