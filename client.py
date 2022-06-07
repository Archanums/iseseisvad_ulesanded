import socket,sys,time


s=socket.socket() # Loob socket objekti
host=input('Enter host: ') # sisesta hosti nimi
port=8080 # määrab pordi
s.connect((host,port)) # ühendab hostiga
print('Connected to ' + host + ' on port ' + str(port)) # Prindib ühenduse teate
while 1:
    incoming_message = s.recv(1024) # saab kliendilt sõnumi
    incoming_message = incoming_message.decode() # Dekodeerib sõnum
    print('[+] Message received: ' + incoming_message) # Prindib sõnumi
    print('')  # Prindib rea
    message = input(str('>> ')) # Küsib klientilt sõnumit
    message = message.encode() # Kodeerib sõnumi
    s.send(message) # Saadab kliendi sõnumi
    print('[+] Message sent') # Prindib sõnumi saatmise teate
    print('')  # Prindib rea