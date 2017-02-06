from socket import *
import sys

if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)

PORT = 8888
kb = 1024

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('', PORT))
tcpSerSock.listen(4)

while True:
    # Start receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()

    print('Received a connection from:', addr)
    message = tcpCliSock.recv(kb).decode()
    print(message)

    # Extract the filename from the given message
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print(filename)

    fileExist = False
    filetouse = "/" + filename
    print(filetouse)

    try:
        # Check whether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.read()
        fileExist = "true"

        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n".encode())

        response = ""
        for line in outputdata:
            response += line

        tcpCliSock.send(response.encode())

        print('Read from cache')

        # Error handling for file not found in cache
    except IOError:
        if not fileExist:
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace("www.", "", 1)
            print(hostn)
            try:
                # Connect to the socket to port 80
                c.connect((hostn, 80))

                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                fileobj = c.makefile('rwb', 0)
                fileobj.write("GET http://{} HTTP/1.0\n\n".format(filename).encode())

                # Read the response into buffer
                buff = fileobj.read()

                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename, "wb")
                tmpFile.write(buff)

                tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
                tcpCliSock.send("Content-Type:text/html\r\n".encode())
                tcpCliSock.send(buff)
                tcpCliSock.send("\r\n".encode())

                c.close()
                tcpCliSock.close()

            except:
                print("Illegal request")
                c.close()
        else:
            # HTTP response message for file not found
            print("file {} not found.".format(filetouse))
            tcpCliSock.send("HTTP/1.0 404 Not Found".encode())
    # Close the client and the server sockets
    tcpCliSock.close()
tcpSerSock.close()
