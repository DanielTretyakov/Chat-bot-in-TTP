from transitions import Machine
import telebot

TOKEN = '6800264360:AAHTmlCeMly0hxKb1AB0vYCrihcqcpCpBNo'
bot = telebot.TeleBot(TOKEN)


class User(object):
    def __init__(self, name):
        self.name = name
        self.machine = Machine(model=self, states=['main_menu', 'women_single', 'men_single', 'next_men',
                                                   'next_women'], initial='main_menu')
        self.machine.add_transition(trigger='welcome', source='*', dest='main_menu')
        self.machine.add_transition(trigger='women_single', source='main_menu', dest='women_single')
        self.machine.add_transition(trigger='men_single', source='main_menu', dest='men_single')
        self.machine.add_transition(trigger='next_men', source='men_single', dest='next_men')
        self.machine.add_transition(trigger='next_women', source='women_single', dest='next_women')


@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = message.chat.id
    bot.send_message(user_id, "Здравствуйте, я чат-бот помощник по актуальным результатам турнира YENISEY 2023"
                              " по настольному теннису в городе Красноярск. Для взаимодействия со мной "
                              "используй следующие команды:\n"
                              "\n /men_single - результаты мужского одиночного разряда\n"
                              "/women_single - результаты женского одиночного разряда\n")


@bot.message_handler(commands=['women_single'])
def women_single(message):
    user_id = message.chat.id
    bot.send_message(user_id, " Результаты женщин в одиночной разряде:\n\n1 место - Непоп Мария\n"
                              "2 место - Савченкова Дарья\n3 место - Елисеева Елена/Батыршина Елена\n\n"
                              "/next_women - показать 4 и 5 место\n\n"
                              "Для возврата в главное меню используйте /start")


@bot.message_handler(commands=['next_women'])
def next_women(message):
    user_id = message.chat.id
    bot.send_message(user_id, "\n4 место - Черненко Екатерина"
                              "\n5 место - Черненко Мария"      
                              "\nДля возврата в главное меню используйте /start")


@bot.message_handler(commands=['men_single'])
def men_single(message):
    user_id = message.chat.id
    bot.send_message(user_id, " Результаты мужчин в одиночной разряде:\n\n1 место - Самигуллин Сергей\n"
                              "2 место - Туйчиев Данис\n3 место - Осипов Андрей/Георгиев Александр\n\n"
                              "/next_men - показать 4 и 5 место\n\n"
                              "Для возврата в главное меню используйте /start")


@bot.message_handler(commands=['next_men'])
def next_men(message):
    user_id = message.chat.id
    bot.send_message(user_id, "\n4 место - Власов Дмитрий"                  
                              "\n5 место - Коротаев Егор"                       
                              "\nДля возврата в главное меню используйте /start")


bot.polling(none_stop=True)
