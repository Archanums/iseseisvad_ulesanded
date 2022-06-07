import socket, sys, time # Imprdib mooduli


s=socket.socket() # Loob socket objekti
host=socket.gethostname() # Hosti nimi loob
port=8080 # Port
s.bind((host,port)) # Bindi host ja port
print('') # Prindib rea
print(host)
print("")
print('[+] Server started on port ' + str(port)) # Prindib serveri pordi
print('')  # Prindib rea
print('server is waiting for connection...') # Prindib serveri ühendamise ootamise teate
print('')  # Prindib rea
s.listen(1) # Loob serveri kuulamise
c, addr = s.accept() # Aksepteerib kliendi
print('[+] Got connection from ' + str(addr)) # Prindib kliendi aadressi
print('')  # Prindib rea
while 1:
    message = input(str('>> ')) # Küsib sõnumit
    message = message.encode() # Kodeerib sõnumi
    c.send(message) # Saadab kliendile sõnumi
    print('[+] Message sent') # Prindib sõnumi saatmise teate
    print('')  # Prindib rea
    incoming_message = c.recv(1024) # saab kliendilt sõnumit
    incoming_message = incoming_message.decode() # Dekodeerib sõnum
    print('[+] Message received: ' + incoming_message) # Prindib sõnumi
    print('')  # Prindib rea