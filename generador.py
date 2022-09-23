from math import ceil
from operator import mod
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

### Cada clase pertenece a un método de generación de números pseudoaleatorios
### Comenatarios solo en la primera clase, las demás son similares, salvo algunas especifícaciones

class CuadradosMedios:
    def __init__(self) -> None:
        ### Metodos para construir la interfaz con Tkinter
        self.root = Tk()
        self.root.minsize(width=275, height=100)
        self.root.title('Cuadrados medios')

        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(side='top', fill=BOTH)

        ### Metodos para pedir los datos necesarios al usuario
        self.seed = simpledialog.askinteger(title='Semilla', prompt='Semilla')
        self.iter = simpledialog.askinteger(title='Iteraciones', prompt='Iteraciones')
        ttk.Label(self.frame, text='Semilla: ' + str(self.seed)).pack(anchor='w')
        self.digits = len(str(self.seed))
        ttk.Label(self.frame, text='Digitos: ' + str(self.digits)).pack(anchor='w')
        ttk.Label(self.frame, text='Iteraciones: ' + str(self.iter)).pack(anchor='w')
        ttk.Button(self.frame, text='Calcular', command=self.calcular).pack(pady=10)

        ### Metodos para construir la tabla
        self.table = ttk.Treeview(self.frame)
        self.table['columns'] = ('#', 'N', 'Nm', 'R')
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('#', width=30, anchor=CENTER)
        self.table.column('N', width=75, anchor=CENTER)
        self.table.column('Nm', width=75, anchor=CENTER)
        self.table.column('R', width=75, anchor=CENTER)
        self.table.heading('#', text='#', anchor=CENTER)
        self.table.heading('N', text='Cuadrado', anchor=CENTER)
        self.table.heading('Nm', text='N', anchor=CENTER)
        self.table.heading('R', text='r', anchor=CENTER)

        self.root.mainloop()

    def calcular(self): ### Algoritmo de generacion 
        n = self.seed
        for i in range(self.iter):
            n2 = n**2
            if len(str(n2)) < self.digits*2:
                k = self.digits*2 - len(str(n2))
                for j in range(k):
                    n2 = '0' + str(n2)
            low = len(str(n2))//2 - self.digits//2
            high = len(str(n2))//2 + ceil(self.digits/2)
            n = int(str(n2)[low : high])
            r = n/10**self.digits

            self.table.insert(parent='', index='end', iid=i, values=(i, n2, n, r))

        self.table.pack()

class ProductosMedios:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.minsize(width=275, height=100)
        self.root.title('Productos medios')

        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(side=TOP, fill=BOTH)

        self.seed1, self.seed2 = self.semillas()

        ttk.Label(self.frame, text='Semilla 1: ' + str(self.seed1)).pack(anchor='w')
        ttk.Label(self.frame, text='Semilla 2: ' + str(self.seed2)).pack(anchor='w')
        self.digits = len(str(self.seed1))
        ttk.Label(self.frame, text='Digitos: ' + str(self.digits)).pack(anchor='w')
        self.iter = simpledialog.askinteger(title='Iteraciones', prompt='Iteraciones')
        ttk.Label(self.frame, text='Iteraciones: ' + str(self.iter)).pack(anchor='w')
        ttk.Button(self.frame, text='Calcular', command=self.calcular).pack(pady=10)

        self.table = ttk.Treeview(self.frame)
        self.table['columns'] = ('#', 'N1', 'N2', 'N1*N2', 'Nm', 'R')
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('#', width=30, anchor=CENTER)
        self.table.column('N1', width=75, anchor=CENTER)
        self.table.column('N2', width=75, anchor=CENTER)
        self.table.column('N1*N2', width=75, anchor=CENTER)
        self.table.column('Nm', width=75, anchor=CENTER)
        self.table.column('R', width=75, anchor=CENTER)
        self.table.heading('#', text='#', anchor=CENTER)
        self.table.heading('N1', text='N1', anchor=CENTER)
        self.table.heading('N2', text='N2', anchor=CENTER)
        self.table.heading('N1*N2', text='Producto', anchor=CENTER)
        self.table.heading('Nm', text='N', anchor=CENTER)
        self.table.heading('R', text='r', anchor=CENTER)

        self.root.mainloop()
    
    def semillas(self):
        while True:
            seed1 = simpledialog.askinteger(title='Semilla 1', prompt='Semilla 1')
            seed2 = simpledialog.askinteger(title='Semilla 2', prompt='Semilla 2')
            if len(str(seed1)) != len(str(seed2)):
                messagebox.showerror(title='Error', message='Las semillas deben tener la misma cantidad de dígitos')
            elif len(str(seed1)) < 4 or len(str(seed2)) < 4:
                messagebox.showerror(title='Error', message='Las semillas deben tener al menos 4 digitos')
            else:
                break

        return seed1, seed2

    def calcular(self):
        n1 = self.seed1
        n2 = self.seed2
        for i in range(self.iter):
            prod = n1*n2
            low = len(str(prod))//2 - self.digits//2
            high = len(str(prod))//2 + ceil(self.digits/2)
            oldn1 = n1
            n1 = n2
            n2 = int(str(prod)[low : high])
            r = n2/10**self.digits

            self.table.insert(parent='', index='end', iid=i, values=(i, oldn1, n1, prod, n2, r))
            
        self.table.pack()

class MultiplicadorConstante:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.minsize(width=300, height=100)
        self.root.title('Multiplicador constante')

        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(side=TOP, fill=BOTH)

        self.seed, self.const = self.semillas()

        ttk.Label(self.frame, text='Semilla 1: ' + str(self.seed)).pack(anchor='w')
        ttk.Label(self.frame, text='Constante: ' + str(self.const)).pack(anchor='w')
        self.digits = len(str(self.seed))
        ttk.Label(self.frame, text='Digitos: ' + str(self.digits)).pack(anchor='w')
        self.iter = simpledialog.askinteger(title='Iteraciones', prompt='Iteraciones')
        ttk.Label(self.frame, text='Iteraciones: ' + str(self.iter)).pack(anchor='w')
        ttk.Button(self.frame, text='Calcular', command=self.calcular).pack(pady=10)

        self.table = ttk.Treeview(self.frame)
        self.table['columns'] = ('#', 'N1', 'A', 'N1*A', 'Nm', 'R')
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('#', width=30, anchor=CENTER)
        self.table.column('N1', width=75, anchor=CENTER)
        self.table.column('A', width=75, anchor=CENTER)
        self.table.column('N1*A', width=75, anchor=CENTER)
        self.table.column('Nm', width=75, anchor=CENTER)
        self.table.column('R', width=75, anchor=CENTER)
        self.table.heading('#', text='#', anchor=CENTER)
        self.table.heading('N1', text='N0', anchor=CENTER)
        self.table.heading('A', text='a', anchor=CENTER)
        self.table.heading('N1*A', text='Producto', anchor=CENTER)
        self.table.heading('Nm', text='N', anchor=CENTER)
        self.table.heading('R', text='r', anchor=CENTER)

        self.root.mainloop()

    def semillas(self):
        while True:
            seed = simpledialog.askinteger(title='Semilla 1', prompt='Semilla 1')
            const = simpledialog.askinteger(title='Constante', prompt='Constante')
            if len(str(seed)) != len(str(const)):
                messagebox.showerror(title='Error', message='Los numeros deben tener la misma cantidad de dígitos')
            elif len(str(seed)) < 4 or len(str(const)) < 4:
                messagebox.showerror(title='Error', message='Los numeros deben tener al menos 4 digitos')
            else:
                break

        return seed, const

    def calcular(self):
        n = self.seed
        a = self.const
        for i in range(self.iter):
            prod = n*a
            low = len(str(prod))//2 - self.digits//2
            high = len(str(prod))//2 + ceil(self.digits/2)
            oldn = n
            n = int(str(prod)[low : high])
            r = n/10**self.digits
            
            self.table.insert(parent='', index='end', iid=i, values=(i, oldn, a, prod, n, r))
            
        self.table.pack()

class CongruencialL:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.minsize(width=300, height=100)
        self.root.title('Congruencial lineal')

        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(side=TOP, fill=BOTH)

        self.seed = simpledialog.askinteger(title='Semilla', prompt='Semilla')
        ttk.Label(self.frame, text='Semilla: ' + str(self.seed)).pack(anchor='w')
        self.consta = simpledialog.askinteger(title='Constante a', prompt='Constante a')
        ttk.Label(self.frame, text='Constante a: ' + str(self.consta)).pack(anchor='w')
        self.constc = simpledialog.askinteger(title='Constante c', prompt='Constante c')
        ttk.Label(self.frame, text='Constante c: ' + str(self.constc)).pack(anchor='w')
        self.constm = simpledialog.askinteger(title='Constante m', prompt='Constante m')
        ttk.Label(self.frame, text='Constante m: ' + str(self.constm)).pack(anchor='w')
        self.iter = simpledialog.askinteger(title='Iteraciones', prompt='Iteraciones')
        ttk.Label(self.frame, text='Iteraciones: ' + str(self.iter)).pack(anchor='w')
        ttk.Button(self.frame, text='Calcular', command=self.calcular).pack(pady=10)

        self.table = ttk.Treeview(self.frame)
        self.table['columns'] = ('#', 'N', 'R')
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('#', width=30, anchor=CENTER)
        self.table.column('N', width=75, anchor=CENTER)
        self.table.column('R', width=75, anchor=CENTER)
        self.table.heading('#', text='#', anchor=CENTER)
        self.table.heading('N', text='N', anchor=CENTER)
        self.table.heading('R', text='r', anchor=CENTER)

        self.root.mainloop()

    def calcular(self):
        n = self.seed
        a = self.consta
        c = self.constc
        m = self.constm
        for i in range(self.iter):
            res = mod(a*n+c, m)
            r = round(res/(m-1), 4)
            n = res

            self.table.insert(parent='', index='end', iid=i, values=(i, res, r))
        self.table.pack()

class CongruencialM:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.minsize(width=320, height=100)
        self.root.title('Congruencial Multiplicativo')

        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(side=TOP, fill=BOTH)

        self.seed = simpledialog.askinteger(title='Semilla', prompt='Semilla')
        ttk.Label(self.frame, text='Semilla: ' + str(self.seed)).pack(anchor='w')
        self.consta = simpledialog.askinteger(title='Constante a', prompt='Constante a')
        ttk.Label(self.frame, text='Constante a: ' + str(self.consta)).pack(anchor='w')
        self.constm = simpledialog.askinteger(title='Constante m', prompt='Constante m')
        ttk.Label(self.frame, text='Constante m: ' + str(self.constm)).pack(anchor='w')
        self.iter = simpledialog.askinteger(title='Iteraciones', prompt='Iteraciones')
        ttk.Label(self.frame, text='Iteraciones: ' + str(self.iter)).pack(anchor='w')
        ttk.Button(self.frame, text='Calcular', command=self.calcular).pack(pady=10)

        self.table = ttk.Treeview(self.frame)
        self.table['columns'] = ('#', 'N', 'R')
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('#', width=30, anchor=CENTER)
        self.table.column('N', width=75, anchor=CENTER)
        self.table.column('R', width=75, anchor=CENTER)
        self.table.heading('#', text='#', anchor=CENTER)
        self.table.heading('N', text='N', anchor=CENTER)
        self.table.heading('R', text='r', anchor=CENTER)

        self.root.mainloop()

    def calcular(self):
        n = self.seed
        a = self.consta
        m = self.constm
        for i in range(self.iter):
            res = mod(a*n, m)
            r = round(res/(m-1), 4)
            n = res

            self.table.insert(parent='', index='end', iid=i, values=(i, res, r))
        self.table.pack()

class CongruencialA:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.minsize(width=310, height=100)
        self.root.title('Congruencial aditivo')

        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(side=TOP, fill=BOTH)

        self.sec = self.secuencia()
        ttk.Label(self.frame, text='Secuencia: ' + str(self.sec)).pack(anchor='w')
        self.constm = simpledialog.askinteger(title='Constante m', prompt='Constante m')
        ttk.Label(self.frame, text='Constante m: ' + str(self.constm)).pack(anchor='w')
        self.iter = simpledialog.askinteger(title='Iteraciones', prompt='Iteraciones')
        ttk.Label(self.frame, text='Iteraciones: ' + str(self.iter)).pack(anchor='w')
        ttk.Button(self.frame, text='Calcular', command=self.calcular).pack(pady=10)

        self.table = ttk.Treeview(self.frame)
        self.table['columns'] = ('#', 'N', 'R')
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('#', width=30, anchor=CENTER)
        self.table.column('N', width=75, anchor=CENTER)
        self.table.column('R', width=75, anchor=CENTER)
        self.table.heading('#', text='#', anchor=CENTER)
        self.table.heading('N', text='N', anchor=CENTER)
        self.table.heading('R', text='r', anchor=CENTER)

        self.root.mainloop()

    def secuencia(self):
        while True:
            cad = simpledialog.askstring(title='Secuencia', prompt='Numeros separados por coma')
            if '.' in cad:
                messagebox.showerror(title='Error', message='Use solo comas')
            else:
                break
        sec = cad.split(sep=',')
        return sec

    def calcular(self):
        secuencia = self.sec
        slenght = len(secuencia)
        for i in range(self.iter):
            n = mod(int(secuencia[i]) + int(secuencia[slenght-1]), self.constm)
            secuencia.append(n)
            slenght+=1
            r = round(n/(self.constm-1), 4)

            self.table.insert(parent='', index='end', iid=i, values=(i, n, r))
        self.table.pack()

class CongrurncialC:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.minsize(width=300, height=100)
        self.root.title('Congruencial cuadratico')

        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(side=TOP, fill=BOTH)

        self.seed = simpledialog.askinteger(title='Semilla', prompt='Semilla')
        ttk.Label(self.frame, text='Semilla: ' + str(self.seed)).pack(anchor='w')
        self.consta = simpledialog.askinteger(title='Constante a', prompt='Constante a')
        ttk.Label(self.frame, text='Constante a: ' + str(self.consta)).pack(anchor='w')
        self.constb = simpledialog.askinteger(title='Constante b', prompt='Constante b')
        ttk.Label(self.frame, text='Constante b: ' + str(self.constb)).pack(anchor='w')
        self.constc = simpledialog.askinteger(title='Constante c', prompt='Constante c')
        ttk.Label(self.frame, text='Constante c: ' + str(self.constc)).pack(anchor='w')
        self.constm = simpledialog.askinteger(title='Constante m', prompt='Constante m')
        ttk.Label(self.frame, text='Constante m: ' + str(self.constm)).pack(anchor='w')
        self.iter = simpledialog.askinteger(title='Iteraciones', prompt='Iteraciones')
        ttk.Label(self.frame, text='Iteraciones: ' + str(self.iter)).pack(anchor='w')
        ttk.Button(self.frame, text='Calcular', command=self.calcular).pack(pady=10)

        self.table = ttk.Treeview(self.frame)
        self.table['columns'] = ('#', 'N', 'R')
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('#', width=30, anchor=CENTER)
        self.table.column('N', width=75, anchor=CENTER)
        self.table.column('R', width=75, anchor=CENTER)
        self.table.heading('#', text='#', anchor=CENTER)
        self.table.heading('N', text='N', anchor=CENTER)
        self.table.heading('R', text='r', anchor=CENTER)

        self.root.mainloop()

    def calcular(self):
        n = self.seed
        a = self.consta
        b = self.constb
        c = self.constc
        m = self.constm
        for i in range(self.iter):
            n = mod((a*n**2 + b*n + c), m)
            r = round(n/(m-1), 4)
            
            self.table.insert(parent='', index='end', iid=i, values=(i, n, r))

        self.table.pack()

### Aplicacion principal
root = Tk()
root.minsize(width=310, height=100)
root.title('Números pseudoaleatorios')
frame = ttk.Frame(root, padding=30)
frame.pack()

### Botones de la app principal que invocan cada clase
m1 = ttk.Button(frame, text='Cuadrados medios', command=CuadradosMedios, width=25).pack()
m2 = ttk.Button(frame, text='Productos medios', command=ProductosMedios, width=25).pack()
m3 = ttk.Button(frame, text='Multiplicador constante', command=MultiplicadorConstante, width=25).pack()
m4 = ttk.Button(frame, text='Congruencial lineal', command=CongruencialL, width=25).pack()
m5 = ttk.Button(frame, text='Congruencial multiplicativo', command=CongruencialM, width=25).pack()
m6 = ttk.Button(frame, text='Congruencial aditivo', command=CongruencialA, width=25).pack()
m7 = ttk.Button(frame, text='Congruencial cuadratico', command=CongrurncialC, width=25).pack()
root.mainloop()