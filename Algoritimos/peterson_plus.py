import random
import threading
import time


class PetersonLockManager:
    def __init__(self):
        self.turn_queue = []
        self.threads = []

    def enter_critical_section(self, process_id):
        
        # Atraso aleatório antes de entrar na seção crítica
        time.sleep(random.uniform(0.01, 0.1))
        
        self.turn_queue.append(process_id)
        
        # Verifica se outros processos estão na seção crítica
        print(f"Processo {process_id} tentando entrar na região crítica")
        while self.turn_queue[0] != process_id:
            pass

        # Seção crítica
        print(f"Processo {process_id} entrou na região crítica")
        # Atraso aleatório dentro da seção crítica
        time.sleep(random.uniform(0.01, 0.1))

        # Saída da seção crítica
        print(f"Processo {process_id} saiu na região crítica")
        self.turn_queue.pop(0)

    def add_process(self, process_id):
        # Cria uma nova thread para o novo processo
        thread = threading.Thread(target=self.enter_critical_section, args=(process_id,))
        self.threads.append(thread)
        thread.start()

    def join_all(self):
        # Aguarda a conclusão de todas as threads
        for thread in self.threads:
            thread.join()

# Criar o gerenciador de lock de Peterson
lock_manager = PetersonLockManager()

# Adicionar processos dinamicamente
for i in range(5):
    lock_manager.add_process(i)

# Adiciona mais processos depois de algum tempo
time.sleep(1)
for i in range(5,10):
    # Atraso aleatório antes de adicionar novas threads
    time.sleep(random.uniform(0.01, 0.1))
    lock_manager.add_process(i)

# Espera todos os processos terminarem
lock_manager.join_all()
