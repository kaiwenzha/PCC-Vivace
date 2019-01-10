import argparse
import socket
import threading

parser = argparse.ArgumentParser(
    description = 'Networks Project: Experiment on Different Congestion Control Protocol')
parser.add_argument('-bs', '--buffer-size', default = 64, type=int, help='Buffer size (KB)')
parser.add_argument('-p', '--protocol', default='cubic', choices=['cubic', 'pcc', 'bbr'], 
    help='Congestion control protocol')
parser.add_argument('-ip', '--ip', default='127.0.0.1', help='Host IP address')

def communicate(server, conn):
    data = 'start'
    try:
        while data:
            data = conn.recv(1024*2)
            #print("Received: {}...".format(data[:min(16,len(data))]))
            data = data.upper()
            #print("Sending: {}...".format(data[:min(16,len(data))]))
            conn.send(data)
        print("Close")
        server.close()
    except:
	    server.close()
	    print('Closed for exception')

def main():

    args = parser.parse_args()
    server = socket.socket()   

    TCP_CONGESTION = getattr(socket, 'TCP_CONGESTION', 13)
    server.setsockopt(socket.IPPROTO_TCP, TCP_CONGESTION, args.protocol.encode())   
    server.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1024 * args.buffer_size)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * args.buffer_size)

    port = 9999                
    server.bind((args.ip, port))      
    server.listen(50)
    print("Waiting for connections...")

    while True:
        conn, addr = server.accept()
        print("Connected: {}".format(addr))
        thread = threading.Thread(target=communicate, args=(server,conn))
        thread.start()


if __name__ == '__main__':
    main()