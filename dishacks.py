import random
from unittest import result
import colorama
from colorama import Fore, Style, Back
from time import sleep
import dhooks
from dhooks import Webhook
import string
import base64
import requests

colorama.init(autoreset=True)

print(Fore.BLUE + """

                                    --   _______   __       _______. __    __       ___       ______  __  ___ 
                                    --  |       \ |  |     /       ||  |  |  |     /   \     /      ||  |/  / 
                                    --  |  .--.  ||  |    |   (----`|  |__|  |    /  ^  \   |  ,----'|  '  /  
                                    --  |  |  |  ||  |     \   \    |   __   |   /  /_\  \  |  |     |    <   
                                    --  |  '--'  ||  | .----)   |   |  |  |  |  /  _____  \ |  `----.|  .  \  
                                    --  |_______/ |__| |_______/    |__|  |__| /__/     \__\ \______||__|\__\ 
--       By lil keep
         Discord : https://discord.gg/3Bm3X7zAhW                                                                  

""")

print(Fore.RED + """         
     _______________________________________________
    |                                               |
    | [1] : Webhook spammer                         |
    |                                               |
    | [2] : Nitro generator                         |
    |                                               |
    | [3] : Webhook fast spammer                    |
    |                                               |
    | [4] : multi spammmer                          |
    |                                               |
    | [5]: token gen                                |
    |                                               |
    | [6]: infinity token gen                       |
    |                                               |
    | [7]: first token part                         |
    |                                               |
    | [8]: token bruteforceur                       |
    |                                               |
    | [9] Account checker                           |
    |_______________________________________________|
""")

choix = input("[?]: ")

if choix == "1":

    url = input("[WEBHOOK]: ")
    hook = Webhook(url)
    mess = input("[MESSAGE]: ")

    while True:
        hook.send(mess)
        print(Fore.RED + "[SENDED] " + mess)

if choix == "2":

    num = int(input("[NUMBER]: "))

    g = ""

    for i in range(num):

        g = "[+] https://discord.gift/" + "".join(random.choices(string.ascii_letters + string.digits, k=24))
        print(Fore.BLUE + '"' +  g + '"')
        sleep(0.50)

        with open("nitros.txt", "a") as file:
            file.write(g + "\n")

    input("press enter for leave...")

if choix == "3":

    c = int(input("[THREAD]: "))
    w = input("[WEBHOOK]: ")
    for i in range(c):
        hook = Webhook(w)
        print(Fore.RED + "thread...")
    
    mess = input("[MESSAGE]: ")

    while True:
        hook.send(mess)
        print(Fore.BLUE + "[SENDED] " + mess)

if choix == "4":

    c = input("1 : Spam random words\n2 : Spam your words\n\n\n[?]: ")

    if c == "1":

        print(Fore.RED + "multi spammer")

        url1 = input("url : ")
        url2 = input("url : ")
        url3 = input("url : ")
        url4 = input("url : ")
        url5 = input("url : ")
        url6 = input("url : ")
        url7 = input("url : ")
        url8 = input("url : ")
        url9 = input("url : ")
        url10 = input("url : ")

        hook1 = Webhook(url1)
        hook2 = Webhook(url2)
        hook3 = Webhook(url3)
        hook4 = Webhook(url4)
        hook5 = Webhook(url5)
        hook6 = Webhook(url6)
        hook7 = Webhook(url7)
        hook8 = Webhook(url8)
        hook9 = Webhook(url9)
        hook10 = Webhook(url10)

        c = input("start the spam ? (y/n): ")

        if c == "y":
            gen = "abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


            while True:
                gene = ""

                for i in range(100):

                    gene = f"{gene}{random.choice(gen)}"
                
                hook1.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook2.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook3.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook4.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook5.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook6.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook7.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook8.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook9.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook10.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook1.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook2.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook3.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook4.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook5.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook6.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook7.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook8.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook9.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook10.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook1.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook2.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook3.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook4.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook5.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook6.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook7.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook8.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook9.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook10.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook1.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook2.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook3.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook4.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook5.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook6.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook7.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook8.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook9.send(gene + "@everyone")
                print("SENDED : " + gene)
                hook10.send(gene + "@everyone")
                print("SENDED : " + gene)



        if c == "no":
            input("press enter...")

    if c == "2":

        print(Fore.RED + "multi spammer")

        url1 = input("url : ")
        url2 = input("url : ")
        url3 = input("url : ")
        url4 = input("url : ")
        url5 = input("url : ")
        url6 = input("url : ")
        url7 = input("url : ")
        url8 = input("url : ")
        url9 = input("url : ")
        url10 = input("url : ")

        hook1 = Webhook(url1)
        hook2 = Webhook(url2)
        hook3 = Webhook(url3)
        hook4 = Webhook(url4)
        hook5 = Webhook(url5)
        hook6 = Webhook(url6)
        hook7 = Webhook(url7)
        hook8 = Webhook(url8)
        hook9 = Webhook(url9)
        hook10 = Webhook(url10)

        c = input("start the spam ? (y/n): ")

        if c == "y":
            
            w = input("enter a word : ")


            while True:
                gene = ""

                
                hook1.send(w)
                print("SENDED : " + w)
                hook2.send(w)
                print("SENDED : " + w)
                hook3.send(w)
                print("SENDED : " + w)
                hook4.send(w)
                print("SENDED : " + w)
                hook5.send(w)
                print("SENDED : " + w)
                hook6.send(w)
                print("SENDED : " + w)
                hook7.send(w)
                print("SENDED : " + w)
                hook8.send(w)
                print("SENDED : " + w)
                hook9.send(w)
                print("SENDED : " + w)
                hook10.send(w)
                print("SENDED : " + w)




        if c == "no":
            input("press enter...")


if choix == "5":

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

    for i in range(100):
        first = "".join((random.choice(chars) for i in range(24)))
        second = "".join((random.choice(chars) for i in range(6)))
        third = "".join((random.choice(chars) for i in range(27)))

        result = first + "." + second + "." + third

        output = open("output.txt", "a")
        output.write(result + "\n")

    input("token generated...")


if choix == "6":

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

    while True:
        for i in range(100):
            first = "".join((random.choice(chars) for i in range(24)))
            second = "".join((random.choice(chars) for i in range(6)))
            third = "".join((random.choice(chars) for i in range(27)))

            result = first + "." + second + "." + third

            print(Fore.RED + '"' +  result + '"' + "\n")

            output = open("output.txt", "a")
            output.write('"' +  result + '"' + "\n")

if choix == "7":

    id = input("[ID]: ")
    encodedBytes = base64.b64encode(id.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print("[TOKEN FIRST PART]: " + encodedStr)
    input("")

if choix == "8":

    id = input("[ID]: ")
    encodedBytes = base64.b64encode(id.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print("[TOKEN FIRST PART]: " + encodedStr)

    g = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

    while True:

        for i in range(100):
            second = "".join((random.choice(g) for i in range(6)))
            third = "".join((random.choice(g) for i in range(27)))

            print(encodedStr + "." + second + "." + third + "\n")

            with open("searched.txt", "a") as file:
                file.write(encodedStr + "." + second + "." + third + "\n")

if choix == "9":
    input("coming soon...")