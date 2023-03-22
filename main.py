import telebot,random

# Coloca aquí el token de tu bot proporcionado por BotFather
TOKEN = "aqui_va_el_token"

bot = telebot.TeleBot(TOKEN)

informacion_random_1="Mi gato"
informacion_random_2="Mi perro"
informacion_random_3="Mi cacatua"
informacion_random_4="Mi ballena"
informacion_random = [informacion_random_1,
                      informacion_random_2, informacion_random_3, informacion_random_4]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola! Soy tu bot.")


@bot.message_handler(commands=['informacion_random'])
def send_informacion_random(message):
    bot.reply_to(message, random.choice(informacion_random))
    random.shuffle(informacion_random)


@bot.message_handler(func=lambda message: 'hola' in message.text.lower())
def handle_hello(message):
    bot.reply_to(message, "Hola! ¿Cómo estás?")

@bot.message_handler(func=lambda message: '¿qué es el riego por goteo?' in message.text.lower())
def handle_question1(message):
    bot.reply_to(message, "Jaja no lo sé")


@bot.message_handler(func=lambda message: '¿qué especie es adecuada para recibir riego por goteo?' in message.text.lower())
def handle_question2(message):
    bot.reply_to(message, "Uffff esa no me la he estudiado")


@bot.message_handler(func=lambda message: '¿por qué esta especie es adecuada para recibir riego por goteo?' in message.text.lower())
def handle_question3(message):
    bot.reply_to(message, "¡Me pillaste! No soy ingeniero agrícola.")


@bot.message_handler(func=lambda message: '¿qué es el riego de alta frecuencia?' in message.text.lower())
def handle_question4(message):
    bot.reply_to(message, "Emmmm")


@bot.message_handler(func=lambda message: '¿qué diferencia al riego por goteo del riego de alta frecuencia?' in message.text.lower())
def handle_question5(message):
    bot.reply_to(message, "Esa que la contesten los alumnos")


@bot.message_handler(func=lambda message: '¿cómo ayuda el riego por goteo al medio ambiente?' in message.text.lower())
def handle_question1(message):
    bot.reply_to(message, "Ups")


@bot.message_handler(func=lambda message: '¿a qué hora del día debería realizarse el riego por goteo y por qué?' in message.text.lower())
def handle_question1(message):
    bot.reply_to(message, "Ups")


@bot.message_handler(func=lambda message: '¿es conveniente regar de más las plantas y por qué?' in message.text.lower())
def handle_question1(message):
    bot.reply_to(message, "Ups")


@bot.message_handler(func=lambda message: '¿utilizar agua de lluvia podría ser beneficioso a la hora de regar y por qué?' in message.text.lower())
def handle_question1(message):
    bot.reply_to(message, "Ups")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

def main():
    # Aquí puedes agregar cualquier tarea adicional que desees realizar antes de iniciar el bot
    print("Iniciando el bot...")
    bot.polling()


if __name__ == '__main__':
    main()
