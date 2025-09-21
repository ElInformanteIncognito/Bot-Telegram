import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ------------------------------
# PON TU TOKEN AQUÍ
TOKEN = "8350003914:AAF8US3eE_moPR98Pvao-ig5ShllWyZKvKs"
# ------------------------------

# Función para /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot informativo.")

# Función para /info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Este bot te da información de noticias y alertas del país.")

# Función para /noticias (ejemplo de scraping)
async def get_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = "https://example.com/noticias"  # Cambia esta URL por la real
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Ejemplo: titulares en etiquetas <h2>
        titulares = [h2.text for h2 in soup.find_all("h2")][:5]
        mensaje = "\n".join(titulares) if titulares else "No se encontraron noticias."
        await update.message.reply_text(mensaje)
    except Exception as e:
        await update.message.reply_text(f"Ocurrió un error al obtener noticias: {e}")

# Función principal para inicializar el bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Agregar comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("noticias", get_news))
    
    # Ejecutar bot
    print("Bot iniciado...")
    app.run_polling()

# Iniciar bot
if __name__ == "__main__":
    main()
