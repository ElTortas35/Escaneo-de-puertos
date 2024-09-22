import socket
import pyfiglet

Text = "SCANNER"
result = pyfiglet.figlet_format(Text,font='small')
print(f"""
-----------------------------------
{result}

Version. 0.2
Hecho por el Tortas
------------------------------------
""")

N = int(input("DESDE QUE PUERTO QUIERE ESCANEAR:"))

puerto = range(N)
I = input("INGRESE LA IP:")

Host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


for puerto in puerto:
        L = Host.connect_ex((I,puerto))
        if L ==0:
                print("Puerto:", puerto,"Abierto")
        else:
                print("Puerto:", puerto,"Cerrado")

Host.close()
