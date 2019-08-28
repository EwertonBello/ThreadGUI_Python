from threading import Thread
import time

class minhaThread(Thread):
    teste = True

    def __init__(self, t):
        Thread.__init__(self)
        self.t = t
        self.start()

    def run(self):
        while self.teste:
            print("Ainda rodando o loop...")
            time.sleep(self.t)
        print("Fim do loop...")

    def setTeste(self, teste):
        self.teste = teste

