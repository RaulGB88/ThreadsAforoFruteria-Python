import threading
import random

global lock
global total_clientes

# Autor: Raul Granel Blasco 

def aforo_fruteria():

    global total_clientes

    maximo_clientes = 4

    lock.acquire()

    print(f"Aforo de clientes en la frutería...: {total_clientes}")

    if(total_clientes >= maximo_clientes):
        print(f"Está esperando... (Aforo actual {total_clientes})")
        total_clientes -= 1
        print(f"Sale de la frutería... (Aforo actual {total_clientes})\n")
        
    else:
        for i in range(maximo_clientes-total_clientes):
            total_clientes += 1
            print(f"Entra en la frutería... (Aforo actual {total_clientes})")

        print(f"Está atendida... (Aforo actual {total_clientes})\n")
        
    lock.release()

def main():
    
    listThreads = list()
    
    for i in range(10):
        with lock:
            t = threading.Thread(target=aforo_fruteria, args=())
            t.start()

        listThreads.append(t)
        t.join() 
        
if __name__ == "__main__":
    total_clientes = 0
    maximo_clientes = 4
    lock = threading.Lock()
    main()
