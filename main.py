import ipaddress
from guizero import App, Text, TextBox, PushButton, error

app = App(title='Projekt 10 Karol Siwy Jakub Wania Michal Kruzel kl.3bt', height=600, width=700)


def program():
    if TextBox1.value == "" or TextBox2.value == "":
        error("Input error", "Błąd. Wpisano niepoprawną wartość lub nie uzupełniono pola tekstowego. Adres IP i maska składa się z cyfr oddzielonych kropkami.")

    IP = TextBox1.value
    MASK = TextBox2.value

    host = ipaddress.IPv4Address(IP)
    net = ipaddress.IPv4Network(IP + '/' + MASK, False)
    TextBox3.value = IP
    TextBox4.value = MASK
    TextBox5.value = ipaddress.IPv4Address(int(host) & int(net.netmask))
    TextBox6.value = net.hostmask
    TextBox7.value = net.broadcast_address
    TextBox8.value = net.num_addresses
    TextBox9.value = net.version


text1 = Text(app, text='Projekt 10', font='Helvetica', size=30)
text2 = Text(app, text='Wpisz adres IP (np. 192.168.32.16):', font='Helvetica', size=15)
TextBox1 = TextBox(app, width=20)
text3 = Text(app, text='Wpisz maskę (np. 255.255.0.0):', font='Helvetica', size=15)
TextBox2 = TextBox(app, width=20)
push1 = PushButton(app, program, text='Start')
text4 = Text(app, text='Wynik:', font='Helvetica', size=30)
text5 = Text(app, text='Adres IP:', font='Helvetica', size=15)
TextBox3 = TextBox(app, width=20)
text6 = Text(app, text='Maska:', font='Helvetica', size=15)
TextBox4 = TextBox(app, width=20)
text7 = Text(app, text='Adres sieci:', font='Helvetica', size=15)
TextBox5 = TextBox(app, width=20)
text8 = Text(app, text='Host:', font='Helvetica', size=15)
TextBox6 = TextBox(app, width=20)
text9 = Text(app, text='Adres Broadcast:', font='Helvetica', size=15)
TextBox7 = TextBox(app, width=20)
text10 = Text(app, text='Liczba hostów w sieci:', font='Helvetica', size=15)
TextBox8 = TextBox(app, width=20)
text11 = Text(app, text='Wersja adresu IP:', font='Helvetica', size=15)
TextBox9 = TextBox(app, width=20)

app.display()
