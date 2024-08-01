Descripción del Proyecto
"TCP SYN Packet Sender with Scapy" es un script en Python que utiliza la biblioteca Scapy para enviar paquetes TCP SYN a una dirección IP específica en el puerto 80. Este tipo de script es útil para propósitos educativos, de prueba y de análisis de redes.


Configuración del Entorno

Importamos las bibliotecas necesarias: Scapy para manejar y enviar paquetes, re para la validación de la IP, y sys para manejar la salida del script y finalizarlo si es necesario.
Validación de la Dirección IP

Solicitamos al usuario que ingrese una dirección IP.
Validamos que la dirección IP proporcionada sea correcta usando Scapy. Si la IP es inválida, mostramos un mensaje de error y terminamos el script.
Configuración del Paquete

Creamos una capa IP con la dirección de destino especificada por el usuario.
Configuramos una capa TCP con un puerto de origen aleatorio y el puerto de destino en 80, que es el puerto estándar para HTTP. Además, establecemos el flag SYN, que indica el inicio de una conexión TCP.
Añadimos una carga útil (payload) de 1024 bytes con datos arbitrarios para completar el paquete.
Envío del Paquete

Combinamos las capas IP, TCP y RAW en un solo paquete.
Iniciamos un bucle que envía el paquete continuamente. Proporcionamos un mensaje para informar al usuario que el script está en ejecución y cómo detenerlo (Ctrl+C).
Manejamos interrupciones del usuario y otros posibles errores, mostrando mensajes informativos si ocurre algún problema.
Objetivo del Script
El propósito principal de este script es demostrar cómo se pueden construir y enviar paquetes TCP SYN usando Scapy. Esto es útil para:

Pruebas de Red: Verificar el comportamiento de un servidor o dispositivo en una red.
Educación: Aprender sobre el funcionamiento de los paquetes TCP y cómo interactúan en la red.
Análisis: Evaluar cómo un sistema maneja el tráfico TCP SYN, lo que puede ser útil en contextos de seguridad y diagnóstico de redes.