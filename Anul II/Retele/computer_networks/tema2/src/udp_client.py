# UDP client
import socket
import logging
import argparse
import re

from util import calculeaza_checksum, construieste_mesaj_raw

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

def send_message(address, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        logging.info('Trimitem mesajul "%s" catre %s:%d', message, address[0], address[1])
        sock.sendto(message.encode('utf-8'), address)

        logging.info('Asteptam un raspuns...')
        data, server = sock.recvfrom(4096)
        client_port, content = re.split(r':', data)
        logging.info('Content primit: "%s"', content)

        client_ip = socket.gethostbyname(socket.gethostname())
        mesaj_binar = construieste_mesaj_raw(server[0], client_ip, server[1], int(client_port), data)
        valoare_numerica = calculeaza_checksum(mesaj_binar)
        logging.info('Checksum calculat: %s', str(hex(valoare_numerica)))

    finally:
        logging.info('closing socket')
        sock.close()


def main():
    parser = argparse.ArgumentParser(description='Client UDP',
                                 formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--server', '-s', dest='server', action='store',
                        required=True, help='Adresa IP a serverului')
    parser.add_argument('--port', '-p', dest='port', action='store', type=int,
                        required=True, help='Portul serverului.')
    parser.add_argument('--mesaj', '-m', dest='mesaj', action='store',
                        default="", help='Mesaj de trimis prin UDP')
    args = parser.parse_args()
    server_address = (args.server, args.port)

    send_message(server_address, args.mesaj)


if __name__ == '__main__':
    main()