from config import token
from weather import Weather, Unit
import telebot, time
import helpers.helper as helper

bot = telebot.TeleBot(token, threaded=False)


@bot.message_handler(commands=['start', 'go', 'testRun'])
def start_handler(message):
    # print(helper.tb_message_to_dict(message))
    bot.send_message(message.chat.id, "Hello, I'm a bot")


@bot.message_handler(content_types=['location'])
def location_handler(message):
    weather = Weather(Unit.CELSIUS)
    l = weather.lookup_by_latlng(message.location.latitude, message.location.longitude)
    out = ("{}, {}, {}" + u'\N{DEGREE SIGN}').format(l.location.region, l.location.country, l.condition.temp)
    bot.send_message(message.chat.id, out)


if __name__ == '__main__':
    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            print(e)
            time.sleep(15)
