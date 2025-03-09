import socket

FLAG_FILE = "/flag.txt"

def get_flag():
    try:
        with open(FLAG_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "ERROR: Flag file not found!"

SECRET_PHRASE = "XOR"  
XOR_KEY = 0x19  

encoded_phrase = ''.join(chr(ord(c) ^ XOR_KEY) for c in SECRET_PHRASE)

def handle_client(conn):
    conn.send(b"Enter the secret phrase (XOR decrypted): ")
    data = conn.recv(1024).strip()

    decoded_input = ''.join(chr(ord(c) ^ XOR_KEY) for c in data.decode())

    if decoded_input == SECRET_PHRASE:
        flag = get_flag()
        conn.send(f"Flag: {flag}\n".encode())
    else:
        conn.send(b"Wrong input!\n")

    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 7201))  # 포트
    server.listen(5)

    print(f"[+] Server is listening on port 7201 with XOR encoded phrase: {encoded_phrase}")

    while True:
        conn, addr = server.accept()
        print(f"[+] Connection from {addr}")
        handle_client(conn)

if __name__ == "__main__":
    main()
