import telebot
import random
from telebot import types

tags = [
    "#cryptomining",
    "#binance",
    "#trading",
    "#binaryoptions",
    "#cryptocurrencies",
    "#investor",
    "#seetcoin",
    "#eth",
    "#coinbase",
    "#usdt",
    "#arbitration",
    "#ripple",
    "#cryptoinvestor",
    "#binancefuture",
    "#altcoins",
    "#tradings",
    "#cryptonews",
    "#finance",
    "#cryptoworld",
    "#nft",
    "#crypto",
    "#altcoin",
    "#trader",
    "#cryptoo",
    "#bitcoinmining",
    "#bitcointrading",
    "#bitcoin",
    "#arbitratium",
    "#ethereum",
    "#btc",
    "#bitcoincash",
    "#litecoin",
    "#cash",
    "#nftcommunity",
    "#cryptotradding",
    "#opensea",
    "#btctoday",
    "#mining",
    "#nfts",
    "#cryptotok",
    "#dogecoin",
    "#bbtc",
    "#buycrypto",
    "#tokens",
    "#tether",
    "#cryptobtc",
    "#trade",
    "#investing",
    "#forex",
    "#trustwallet",
    "#exodus",
    "#cryptogo",
    "#cryptocoin",
    "#bnb",
    "#stocks",
    "#arbitrage",
    "#blockchain",
    "#invest",
    "#solana",
    "#cryptoeth",
    "#btcnews",
    "#cryptocurrency",
    "#xrpcommunity",
    "#cryptonft",
    "#cryptook",
    "#cryptoinvesting",
    "#elon",
    "#bitcoinhodl",
    "#musk",
    "#elonmusk",
    "#cryptomarkets",
    "#bitcoinnews",
    "#muskelon",
    "#bitcoinrevolution",
    "#elon_musk"

]

bot = telebot.TeleBot("6252342587:AAFi3-J3y3q7hYkUm5PUaQMYmAqhOkfjX9U", parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    allowed_usernames = ["Kirill_Dmitriev_67", "keatmanN", "ymix9", "Afex2281"]
    if message.from_user.username in allowed_usernames:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("tags")
        markup.add(btn1)
        bot.send_message(5698977608, text="Новый юзер - @" + message.from_user.username 
                         + "\nДоступ разрешен")
        bot.send_message(message.chat.id, text="ку, {0.first_name}".format(message.from_user), reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Доступ запрещен")
        bot.send_message(5698977608, text="Новый юзер - @" + message.from_user.username + "\nДоступ Запрещен")

@bot.message_handler(content_types=['text'])
def func(message):
    allowed_usernames = ["Kirill_Dmitriev_67", "keatmanN", "ymix9", "Afex2281"]
    if message.from_user.username in allowed_usernames:
        if message.text == "tags":
            # Shuffle the tags list to get a random order
            random.shuffle(tags)

            result_text = ""

            # Divide the shuffled tags into chunks of 5 to form each line
            for i in range(0, 30, 5):
                # Get the current chunk of 5 words
                current_chunk = tags[i:i + 5]

                # Join the words in the current chunk into a single line separated by spaces
                formatted_line = " ".join(current_chunk)

                # Add the current line to the result text
                result_text += f"<code>{formatted_line}\n</code>\n"

            bot.send_message(message.chat.id, result_text, parse_mode="HTML")

    else:
        bot.send_message(message.chat.id, text="Доступ запрещен")


bot.infinity_polling()
