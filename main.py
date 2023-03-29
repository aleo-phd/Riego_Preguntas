import telebot,random

# Coloca aquí el token de tu bot proporcionado por BotFather
TOKEN = "aqui_va_el_token"

bot = telebot.TeleBot(TOKEN)

informacion_random_1="Mi plantita qué bonita"
informacion_random_2="Ojalá rieguen mi plantita"
informacion_random_3="¿Regarán la planta por riego por goteo, por microaspersión o por microdifusión?"
informacion_random_4="¿Y si te digo que la plantas son unos filtros naturales estupendos?"
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


@bot.message_handler(func=lambda message: '¿qué cultivo es adecuado para recibir riego por goteo?, ¿por qué?' in message.text.lower())
def handle_question2(message):
    bot.reply_to(message, "Uffff esa no me la he estudiado")


@bot.message_handler(func=lambda message: '¿qué diferencia al riego por goteo, la microaspersión y a la microdifusión?' in message.text.lower())
def handle_question3(message):
    bot.reply_to(message, "¡Me pillaste! No soy ingeniero agrónomo.")


@bot.message_handler(func=lambda message: '¿a qué tipo de cultivo le viene mejor cada tipo de riego?, ¿por qué?' in message.text.lower())
def handle_question4(message):
    bot.reply_to(message, "Emmmm")


@bot.message_handler(func=lambda message: '¿qué tipo de cultivo necesita más caudal?, ¿por qué?' in message.text.lower())
def handle_question5(message):
    bot.reply_to(message, "Esa que la contesten los alumnos")


@bot.message_handler(func=lambda message: '¿qué objetivo de los ods está relacionado con el agua?, ¿qué metas tiene?' in message.text.lower())
def handle_question6(message):
    bot.reply_to(message, "Ups")


@bot.message_handler(func=lambda message: 'relacionado con el ods 7 (energía), ¿cuánto cuesta mover el agua del pozo al cultivo?' in message.text.lower())
def handle_question7(message):
    bot.reply_to(message, "Enséname la respuesta")


@bot.message_handler(func=lambda message: '¿qué volumen de agua embalsadas se usa para el regadío?' in message.text.lower())
def handle_question8(message):
    bot.reply_to(message, "Si me la hubiese estudiado, la sabría.")


@bot.message_handler(func=lambda message: '¿qué porcentaje tiene cada tipo de riego?' in message.text.lower())
def handle_question9(message):
    bot.reply_to(message, "¿Te he dicho alguna vez que primero tienes que enseñarme para que pueda aprender?")
    photo = open('foto.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)



@bot.message_handler(func=lambda message: 'del total de los cultivos, ¿cuántos son de regadío?' in message.text.lower())
def handle_question10(message):
    bot.reply_to(message, "Plantita jaja")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

def main():
    # Aquí puedes agregar cualquier tarea adicional que desees realizar antes de iniciar el bot
    print("Iniciando el bot...")
    bot.polling()


if __name__ == '__main__':
    main()
