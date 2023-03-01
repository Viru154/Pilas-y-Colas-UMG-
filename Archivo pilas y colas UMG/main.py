import tkinter as tk
import random
import time

class PilasColasUMG:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PILAS Y COLAS UMG")
        self.root.geometry("500x500")
        
        self.tiempo_pila = 0
        self.tiempo_cola = 0
        
        self.numeros_generados = []
        
        # Crear widgets
        self.btn_generar_numeros_1 = tk.Button(self.root, text="Generar por Colas", command=self.generar_numeros_1)
        self.btn_generar_numeros_1.pack(side=tk.TOP, pady=10)
        self.btn_generar_numeros_2 = tk.Button(self.root, text="Generar por Filas ", command=self.generar_numeros_2)
        self.btn_generar_numeros_2.pack(side=tk.TOP, pady=10)
        self.btn_limpiar_pantalla = tk.Button(self.root, text="Limpiar pantalla", command=self.limpiar_pantalla)
        self.btn_limpiar_pantalla.pack(side=tk.TOP, pady=10)
        self.btn_reset = tk.Button(self.root, text="Reset", command=self.reset)
        self.btn_reset.pack(side=tk.TOP, pady=10)
        
        self.txt_pila = tk.Text(self.root, height=10)
        self.txt_pila.pack(side=tk.LEFT, padx=10)
        self.txt_cola = tk.Text(self.root, height=10)
        self.txt_cola.pack(side=tk.RIGHT, padx=10)
        
        # Ejecutar GUI
        self.root.mainloop()
        
    def generar_numeros_1(self):
        # Vaciar lista de números generados y text areas
        self.numeros_generados = []
        self.txt_pila.delete("1.0", tk.END)
        self.txt_cola.delete("1.0", tk.END)
        
        # Generar números aleatorios
        inicio = time.time()
        for i in range(1000000):
            num = random.randint(-10000000, 10000000)
            self.numeros_generados.append(num)
            self.txt_pila.insert(tk.END, f"{num}\n")
        fin = time.time()
        self.tiempo_pila = fin - inicio
        
    def generar_numeros_2(self):
        # Vaciar lista de números generados y text areas
        self.numeros_generados = []
        self.txt_pila.delete("1.0", tk.END)
        self.txt_cola.delete("1.0", tk.END)
        
        # Generar números aleatorios
        inicio = time.time()
        for i in range(1000000):
            num = random.randint(-10000000, 10000000)
            self.numeros_generados.append(num)
            self.txt_cola.insert(tk.END, f"{num}\n")
        fin = time.time()
        self.tiempo_cola = fin - inicio
        
    def limpiar_pantalla(self):
        self.txt_pila.delete("1.0", tk.END)
        self.txt_cola.delete("1.0", tk.END)
        
    def reset(self):
        self.tiempo_pila = 0
        self.tiempo_cola = 0
        self.limpiar_pantalla()

if __name__ == '__main__':
    app = PilasColasUMG()
