import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# 📌 Cargar variables de entorno
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# 📌 Configurar logs
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

# 📌 Función para manejar /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("¡Hola! Soy tu bot de Telegram en Railway. 🚀")

# 📌 Función para manejar mensajes de texto
async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f"Recibí tu mensaje: {update.message.text}")

# 📌 Función principal
def main():
    # ✅ Cambiar Updater por Application.builder()
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # 📌 Agregar comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 📌 Iniciar el bot
    application.run_polling()

if __name__ == "__main__":
    main()
