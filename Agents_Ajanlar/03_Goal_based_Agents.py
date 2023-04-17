#Basit bir "yem avı" oyununu ele alalım.
# Bu oyunda, ajanımız yiyecekleri toplamalı 
# ve mümkün olduğunca yüksek bir puan elde etmeye çalışmalıdır. 
# Ajanımızın amacı, en kısa sürede mümkün olduğunca fazla yiyeceği toplamaktır.

import random

#Oyun alanının Boyutu
WIDTH=20
HEIGHT=10

#Yiyeceklerin toplam boyutu.
FOOD_POINTS=10

#Ajanın konumunu ve puanını tutan değişkenler
agent_x=0
agent_y=0
agent_score=0

#Yiyeceklerin konumlarını ve puanlarını tutan liste
foods=[]

#yiyecekleri rastgele bir konumda oluşturmak için bir yardımcı fonksiyon oluşturuluyor
def create_food():
    #Rastgele x ve y kordinatları seç
    food_x=random.randint(0,WIDTH-1)
    food_y=random.randint(0,HEIGHT-1)
    
    
    #Oluiturulan yiyeceğin puanı
    food_points=random.randint(1,FOOD_POINTS)
    
    return (food_x,food_y,food_points)

#Daha sonra, oyuna başlamak için ajanımızı ilk konumuna yerleştirip yiyecekleri oluşturuluyor

#Ajanın ilk konumu
agent_x=random.randint(0,WIDTH-1)
agent_y=random.randint(0,HEIGHT-1)

#İlk yiyecek oluituruluyor
foods.append(create_food())

#Oyun döngümüz, ajanın her turda bir adım atması,
# yiyecekleri toplaması ve puanını güncellemesi gereken bir döngü oluituruluyor. 
# Ayrıca, ajanın hareket etmesini sağlamak için bir dizi hareket fonksiyonu da yazılıyor
def move_left():#Sola Taşıma fonksiyonu
    global agent_x
    
    if agent_x>0:
        agent_x-=1


def move_right():
    global agent_x
    
    if agent_x<WIDTH-1:
        agent_x +=1
        
        
def move_up():#Yukarı taşıma:
    global agent_y
    
    if agent_y>0:
        agent_y-=1
        
def move_down():#Aşağı taşıma :
    global agent_y
    
    if agent_y< HEIGHT-1:
        agent_y+=1
        
#Oyun Döngüsü

while True:
    #Ajanın konumunu yazdır
    print("Ajanın konumu:({},{})".format(agent_x,agent_y))
    
    
    #Yiyecekleri yazdır
    print("Yiyecekler:")
    
    #Yiyecekler yazdırılıyor
    for i,food in enumerate(foods):
        print("{}. Konum: ({}, {}), Puan: {}/n".format(i+1, food[0], food[1], food[2]))
    
    #Ajanın hareketi alınıyor
    action=input("Sol(s),sağ(d),yukarı(y) veya aşağı tuiuna basarak ajamı hareket ettirin: ")
    
    
    #Hareket fonksiyonu çağırılıyor
    if action=="s":
        move_left()
        
    elif action=="d":
        move_right()
        
    elif action=="y":
        move_up()
        
    elif action=="a":
        move_down()
        
    #Ajanın yiyeceği toplayıp toplanmadığını kontrol ediliyor.
    for food in foods:
        if agent_x==foods[0] and agent_y==food[1]:
            agent_score+=food[2]
            print("Ajan bir yiyecek topladı! Toplam puan:{}".format(agent_score))
            
            #yiyecekler kaldırılıyor
            foods.remove(food)
            foods.append(create_food())
            break
        
    else:
        print("Ajan hiçbir yiyecek toplayamadı.")
        
    #oYUN sONLANDIRILIYOR
    if len(food)==0:
        print("oyun bitti! Toplam Puan:{}".format(agent_score))
        break