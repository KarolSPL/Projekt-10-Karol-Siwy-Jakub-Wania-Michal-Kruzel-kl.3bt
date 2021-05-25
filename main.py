# Projekt 10 Karol Siwy Jakub Wania Michal Kruzel kl.3bt
import ipaddress # importuje bibliotekę ipaddress
from guizero import App, Text, TextBox, PushButton, error # importuje bibliotekę guizero

app = App(title='Projekt 10 Karol Siwy Jakub Wania Michal Kruzel kl.3bt', height=600, width=700) # nazwa programu


def program(): # kod programu
    if TextBox1.value == "" or TextBox2.value == "":
        error("Input error", "Błąd. Wpisano niepoprawną wartość lub nie uzupełniono pola tekstowego. Adres IP i maska składa się z cyfr oddzielonych kropkami.") # błąd

    IP = TextBox1.value # adres IP
    MASK = TextBox2.value # adres maski

    host = ipaddress.IPv4Address(IP)
    net = ipaddress.IPv4Network(IP + '/' + MASK, False)
    TextBox3.value = IP # wyświetla adres IP
    TextBox4.value = MASK # wyświetla adres maski
    TextBox5.value = ipaddress.IPv4Address(int(host) & int(net.netmask)) # oblicza adres sieci
    TextBox6.value = net.hostmask # oblicza adres hosta
    TextBox7.value = net.broadcast_address # oblicza adres broadcast
    TextBox8.value = net.num_addresses # oblicza liczbę hostów
    TextBox9.value = net.version # oblicza wersję adresu IP


text1 = Text(app, text='Projekt 10', font='Helvetica', size=30) # tekst
text2 = Text(app, text='Wpisz adres IP (np. 192.168.32.16):', font='Helvetica', size=15) # tekst
TextBox1 = TextBox(app, width=20) # pole tekstowe
text3 = Text(app, text='Wpisz maskę (np. 255.255.0.0):', font='Helvetica', size=15) # tekst
TextBox2 = TextBox(app, width=20) # pole tekstowe
push1 = PushButton(app, program, text='Start') # przycisk
text4 = Text(app, text='Wynik:', font='Helvetica', size=30) # tekst
text5 = Text(app, text='Adres IP:', font='Helvetica', size=15) # tekst
TextBox3 = TextBox(app, width=20) # pole tekstowe
text6 = Text(app, text='Maska:', font='Helvetica', size=15) # tekst
TextBox4 = TextBox(app, width=20) # pole tekstowe
text7 = Text(app, text='Adres sieci:', font='Helvetica', size=15) # tekst
TextBox5 = TextBox(app, width=20) # pole tekstowe
text8 = Text(app, text='Host:', font='Helvetica', size=15) # tekst
TextBox6 = TextBox(app, width=20) # pole tekstowe
text9 = Text(app, text='Adres Broadcast:', font='Helvetica', size=15) # tekst
TextBox7 = TextBox(app, width=20) # pole tekstowe
text10 = Text(app, text='Liczba hostów w sieci:', font='Helvetica', size=15) # tekst
TextBox8 = TextBox(app, width=20) # pole tekstowe
text11 = Text(app, text='Wersja adresu IP:', font='Helvetica', size=15) # tekst
TextBox9 = TextBox(app, width=20) # pole tekstowe

app.display() # wyświetla aplikację guizero

