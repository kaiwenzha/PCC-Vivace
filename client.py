import argparse
import socket
import random
import string
import threading, time

parser = argparse.ArgumentParser(
    description = 'Networks Project: Experiment on Different Congestion Control Protocol')
parser.add_argument('-ip', '--ip', default='127.0.0.1', help='Destination IP address')
parser.add_argument('-l', '--length', default=512, type=int, help='Length of sending messages')
parser.add_argument('-bs', '--buffer_size', default = 64, type=int, help='Buffer size (KB)')
parser.add_argument('-p', '--protocol', default='cubic', choices=['cubic', 'pcc', 'bbr'], 
    help='Congestion control protocol')
parser.add_argument('-th', '--thread_num', default = 1, type=int, help='Num of threads')

def communicate(length, ip, port, buffer_size, protocol):
    TCP_CONGESTION = getattr(socket, 'TCP_CONGESTION', 13)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.IPPROTO_TCP, TCP_CONGESTION, protocol.encode())   
    client.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1024 * buffer_size)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * buffer_size)

    client.connect((ip, port))

    rand_str = lambda n: ''.join([random.choice(string.ascii_lowercase) for i in range(n)])

    try:
        while True:
            message = rand_str(length)
            message = message.strip()
            print("Sending: {}...".format(message[:min(16,len(message))]))
            client.send(message.encode())
            data = client.recv(1024*2)
            print("Received: {}...".format(data[:min(16,len(data))]))

        client.close()
    except:
        client.close()
        print('Closed for exception')    

def main():
    args = parser.parse_args()
    
    port = 9999
    for i in range(args.thread_num):
        t = threading.Thread(target=communicate, args=(args.length, args.ip, 
            port, args.buffer_size, args.protocol))
        t.start()


if __name__ == '__main__':
    main()