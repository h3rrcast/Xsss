import time 
import requests
import argparse


def xss(url, payload):
    xss = requests.post(url + payload)
    if payload in xss.text:
        print("Panita encontro xss el payload es:", url+payload)
    else:
        print("no es vulnerables a xss F por usted")


parse = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                description="###################### h3rcast ########################\n"\
                                " se usa asi panita: python xxxs.py --url url --P la lista de los payloads"
                                "Demo: xxxxxxxxxxxxxxxxxx\n" \
                                "contacto: @h3rcast#5596(discord)")

parse.add_argument('--url', action= 'store', dest = 'url', required = True, help = 'nea la url:')
parse.add_argument('--P', action= 'store', dest = 'payload', required = True, help = 'nea la lista de payloads:')

arguments = parse.parse_args()

url = arguments.url
lista_payload = arguments.payload

lista = open(lista_payload, 'r')

for lista in lista.read().split("\n"):
    xss(url, lista)
