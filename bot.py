import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# 📌 Cargar variables de entorno
load_dotenv()

# 📌 Obtener el token del bot desde el archivo .env
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# 📌 Configurar el sistema de logs
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

# 📌 Función de inicio del bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("¡Hola! Soy tu bot de Telegram en Railway. 🚀")

# 📌 Función para manejar mensajes de texto
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Recibí tu mensaje: {update.message.text}")

def main():
    # 📌 Configurar el bot con el token
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)

    # 📌 Obtener el dispatcher
    dp = updater.dispatcher

    # 📌 Agregar comandos al bot
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("echo", echo))

    # 📌 Iniciar el bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
