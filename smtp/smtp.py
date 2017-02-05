from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
senderDomain = "alumni.ubc.ca"
sender = "erik.dolinsky@{}".format(senderDomain)
recipent = "g7c9@ece.ubc.ca"
kB = 1024

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'mx1.ece.ubc.ca'

# Create socket called clientSocket and establish a TCP connection with mailserver

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))

recv = clientSocket.recv(kB).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO {}\r\n'.format(senderDomain)
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(kB).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: {}\r\n'.format(sender)
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(kB).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
mailToCommand = 'RCPT TO: {}\r\n'.format(recipent)
clientSocket.send(mailToCommand.encode())
recv3 = clientSocket.recv(kB).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(kB).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(kB).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(kB).decode()
print(recv6)
if recv6[:3] != '221':
    print('221 reply not received from server.')

clientSocket.close()
