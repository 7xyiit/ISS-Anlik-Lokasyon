import json  
import turtle
import urllib.request
import time

#Turtle kütüphanesi ile dünya enlem-boylam oluşturma. Ayrıca büyüklük ayarlama.
ekran = turtle.Screen()
ekran.setup(1280, 720)
ekran.setworldcoordinates(-180, -90, 180, 90)
ekran.bgpic("map.gif")
ekran.register_shape("iss.gif")
istasyon = turtle.Turtle()
istasyon.shape("iss.gif")
istasyon.penup()

#Anlık veri için döngüye alındı.
while True:
    adres = 'http://api.open-notify.org/iss-now.json'
    adres_json = urllib.request.urlopen(adres)
    adres_json2 = json.loads(adres_json.read())

    lokasyon = adres_json2['iss_position']
    enlem = lokasyon['latitude']
    boylam = lokasyon['longitude']
    enlem = float(enlem)
    boylam = float(boylam)

    istasyon.goto(boylam, enlem)

    time.sleep(5)