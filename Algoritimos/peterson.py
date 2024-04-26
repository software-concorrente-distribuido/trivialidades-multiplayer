import random
import threading
import time


class PetersonLockManager:
    def __init__(self):
        self.num_processes = 0
        self.flag = []
        self.turn = 0
        self.threads = []

    def enter_critical_section(self, process_id):
        global turn  # Utilize a variável 'turn' compartilhada
        
        # Atraso aleatório antes de entrar na seção crítica
        time.sleep(random.uniform(0.01, 0.1))
        
        self.flag[process_id] = True
        self.turn = process_id
        
        # Verifica se outros processos estão na seção crítica
        for i in range(self.num_processes):
            if i != process_id:
                while self.flag[i] and self.turn == process_id:
                    pass

        # Acessa a Seção crítica
        print(f"Processo {process_id} entrou na região crítica")

        # Saída da seção crítica
        self.flag[process_id] = False
        print(f"Processo {process_id} saiu na região crítica")

    def add_process(self, process_id):
        self.num_processes = process_id + 1
        self.flag.extend([False] * (process_id + 1 - len(self.flag)))

        # Cria uma nova thread para o novo processo
        thread = threading.Thread(target=self.enter_critical_section, args=(process_id,))
        self.threads.append(thread)
        thread.start()

    def join_all(self):
        # Aguarda a conclusão de todas as threads
        for thread in self.threads:
            thread.join()


#Inicia o programa de teste
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
