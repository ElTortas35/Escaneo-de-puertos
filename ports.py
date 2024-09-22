import socket
import pyfiglet
import socket

User = socket.gethostname()

IP = socket.gethostbyname(User)

Text = "SCANNER"
result = pyfiglet.figlet_format(Text,font='small')
print(f"""
-----------------------------------
{result}

Version. 0.3
Hecho por el Tortas
------------------------------------
""")
print("Su usted no sabe su ip es esta:", IP)

N = int(input("DESDE QUE PUERTO QUIERE ESCANEAR:"))

puerto = range(N)
I = input("INGRESE SU IP PARA ESCANEAR LOS PUERTOS:")

Host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


for puerto in puerto:
        L = Host.connect_ex((I,puerto))
        if L ==0:
                print("Puerto:", puerto,"Abierto")
        else:
                print("Puerto:", puerto,"Cerrado")

Host.close()
