
# -*- coding: utf-8 -*-
import urllib.request
import html2text
import time
import hashlib
import requests

grupoacopiar="https://t.me/s/XXXXXXXXXXXXXXX"
nombreamostrar="Nombre del grupo"

def enviar_a_telegram(bot_message):
    bot_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    bot_chatid = '-XXXXXXXXX'
    envio_mensaje = 'https://api.telegram.org/botXXXXXXXXXX:' + bot_token + '/sendMessage?chat_id=' + bot_chatid + '&parse_mode=Markdown&text=' + bot_message
    respuesta = requests.get(envio_mensaje)
    return respuesta.json()

antiguohash = "e"
hashahora = "e"

while True:
    antiguohash = hashahora
    print("Obteniendo datos del grupo de telegram")
    apiurl = urllib.request.urlopen(grupoacopiar)
    reading = str(apiurl.read())
    lista = list(reading.split('<div class="tgme_widget_message_bubble">')) 
    longitud = len(lista) - 1 
    elemento = lista[longitud].split('class="tgme_widget_message_text js-message_text" dir="auto">')[1] 
    h = html2text.HTML2Text()
    # Ignore converting links from HTML
    h.ignore_links = False
    mensaje = "🌟 " + nombreamostrar + " 🌟"
    cnull = 0
    for linea in h.handle(elemento).split("_"):
        if "*" in linea:
            cnull = cnull + 1
        else:
            mensaje = mensaje + linea.split("_")[0]

    mensaje = mensaje.replace("\n", "").replace("\n\n", "").replace("\n", "").split("[!")[0].split("[ ")[0].replace("?q=%23", "")
    print("[?] Último mensaje / Last message: ")
    print(mensaje)
    mensajeparahash = elemento.split("<")[0]
    print("Mensaje para hash:", mensajeparahash)
    hashahora = hashlib.md5(mensajeparahash.encode()).hexdigest()
    print("[i] Hash actual:", hashahora)
    print("[i] Último hash:", antiguohash)
    
    if hashahora != antiguohash :
        print("[+] Detectado mensaje nuevo !!! - New message detected !!!")
        resultado = mensaje
        if "$" in mensaje:
            test = enviar_a_telegram(resultado)
            print(test)
            print(resultado)
        if "#" in mensaje:
            test = enviar_a_telegram(resultado)
            print(test)
            print(resultado)

    time.sleep(300)
