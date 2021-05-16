import os, socket, tqdm

""" 
get files with principe of blockchain (block 1, block 2, block 3, etc...)
to not get the past file but the new
all new data is sent, then goes into a block which is concatenated
"""

def updateUploadServer():
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096 #send 4096 bytes each time step
    host = "127.0.0.1" #the ip address or hostname of the server, the receiver
    port = 9001 #the port, let's use 9001
    filename = "dns.txt"
    filesize = os.path.getsize(filename) #get the file size
    s = socket.socket() #create the client socket
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    s.send(f"{filename}{SEPARATOR}{filesize}".encode()) #send the filename and filesize
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024) #start sending the file
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE) #read the bytes from the file
            if not bytes_read:
                break #file transmitting is done break
            s.sendall(bytes_read) #we use sendall to assure transimission in busy networks
            progress.update(len(bytes_read)) #update the progress bar
    s.close() #close the socket

def getNewFile():
    #verify block (block 1, 2, 3)
    SERVER_HOST = "0.0.0.0" #peers IP address
    SERVER_PORT = 9001
    BUFFER_SIZE = 4096 #receive 4096 bytes each time
    SEPARATOR = "<SEPARATOR>"
    s = socket.socket() #create the server socket (TCP)
    s.bind((SERVER_HOST, SERVER_PORT)) #bind the socket to our local address
    s.listen(5) #5 here is the number of unaccepted connections that the system will allow before refusing new connections
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    client_socket, address = s.accept() #accept connection if there is any
    print(f"[+] {address} is connected.") #if below code is executed, that means the sender is connected
    received = client_socket.recv(BUFFER_SIZE).decode() #receive the file infos
    print(received)
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename) #remove absolute path if there is
    filesize = int(filesize) #convert to integer
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024) #start receiving the file from the socket and writing to the file stream
    with open("dossier/"+filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE) #read 1024 bytes from the socket (receive)
            if not bytes_read:    
                break #file transmitting is done
            f.write(bytes_read) #write to the file the bytes we just received
            progress.update(len(bytes_read)) #update the progress bar
    client_socket.close() #close the client socket
    s.close() #close the server socket

""" 
coming-soon
#myurl = get .onion service domain

with open("dns.txt") as url:
    url.read()
    if mydomain not in url:
        #add and update file
        #send file
    else:
"""