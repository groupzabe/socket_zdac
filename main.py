import socket

def discover_device():
    # Cria um socket UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Configura o socket para broadcast
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Define a porta e o endereço para envio do broadcast
    broadcast_address = ('<broadcast>', 12345)

    # Envio de mensagem de broadcast
    udp_socket.sendto(b"DISCOVER_DEVICE", broadcast_address)

    # Configura o socket para receber respostas
    udp_socket.settimeout(5)  # Tempo limite de 5 segundos
    try:
        while True:
            data, addr = udp_socket.recvfrom(1024)
            print("Dispositivo encontrado:", data.decode(), "Endereço IP:", addr[0])
    except socket.timeout:
        print("Busca de dispositivos concluída.")

    # Fecha o socket
    udp_socket.close()

if __name__ == "__main__":
    discover_device()
