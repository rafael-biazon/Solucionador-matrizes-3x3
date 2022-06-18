from tkinter import *
from PIL import ImageTk, Image
from Complex import *
from Matrix3x3 import *

def main():
    root = Tk()
    root.title("Solucionador de matrizes")
    root.iconbitmap("./Imagens/icone.ico")

    label1 = Label(root, width=120, borderwidth=5, text="Se esse programa te ajudar, considere uma doação no pix: rbhs100@gmail.com . Qualquer quantia é de grande ajuda")
    label1.grid(row=0, column=0, columnspan=5)
    label2 = Label(root, width=120, borderwidth=5, text="Formato da equação/matriz: [Matriz dos resultados/fontes] = [Matriz 'das impedâncias' (a + linha + coluna)] [Matriz das incógnitas]")
    label2.grid(row=1, column=0, columnspan=5)
    img = ImageTk.PhotoImage(Image.open("./Imagens/matriz_formato_2.jpg"))
    panel = Label(root, image=img).grid(row=2, column=0, columnspan=15)

    class scanEntry:
        def __init__(self, row, column, variable, arg1, arg2):
            self.row = row
            self.column = column
            self.variable = variable
            self.arg1 = arg1
            self.arg2 = arg2
            self.titulo = Entry(root, width=20, borderwidth=5)
            self.titulo.grid(row=self.row, column=self.column, padx=2, pady=2)
            self.titulo.insert(0, f"{self.arg1} do {self.variable}")
            self.titulo2 = Entry(root, width=24, borderwidth=5)
            self.titulo2.grid(row=self.row, column=self.column+1, padx=2, pady=2)
            self.titulo2.insert(0, f"{self.arg2} do {self.variable}")
            
    class buttonSwitchFormat:
        def __init__(self):
            self.arg1 = f"raio"
            self.arg2 = f"ângulo em graus"
            self.format = f"Polar"

        def returnButton(self, row, column, variable):
            self.row = row
            self.column = column
            self.variable = variable
            self.title = scanEntry(self.row+1, self.column, self.variable, self.arg1, self.arg2)        
            return Button(root, width=35, borderwidth=5, text=f"Formato atual: {self.arg1} + {self.arg2}", command = self.switchFormat).grid(row=self.row, column=self.column, columnspan=2)
        
        def switchFormat(self): 
            if self.arg1 == f"raio" and self.arg2 == f"ângulo em graus":
                self.arg1 = f"real"
                self.arg2 = f"imaginário"
                self.format = f"Rectangular"
            elif self.arg1 == f"real" and self.arg2 == f"imaginário":
                self.arg1 = f"raio"
                self.arg2 = f"ângulo em graus"
                self.format = f"Polar"
            self.returnButton(self.row, self.column, self.variable)
            #debug:
            #print(f"self.arg1 = {self.arg1}")
            #print(f"self.arg2 = {self.arg2}")
            #print(f"self.format = {self.format}")
            #print(f"self.row = {self.row}")
            #print(f"self.column = {self.column}")        

    class matrixElement:
        def __init__(self, row, column, variable):
            self.row = row
            self.column = column
            self.variable = variable
            self.button = buttonSwitchFormat()
            #print(f"self.button.get_arg2() = {}")
            #self.arg1 = getattr(self.button, 'arg1')
            #self.arg2 = self.button.get_arg2()
            
        def run(self):
            self.button.returnButton(self.row, self.column, self.variable)
            self.arg1 = getattr(self.button, 'arg1')
            self.arg2 = getattr(self.button, 'arg2')
            #debug:
            #print(f"self.button.get_arg1() = {self.arg1}")
            #print(f"self.button.get_arg1() = {self.arg2}")
            #self.title = scanEntry(self.row+1, self.column, self.variable, self.arg1, self.arg2)

        def get_entry(self):
            return self.button.title.titulo.get()
        
        def get_entry2(self):
            return self.button.title.titulo2.get()

        def get_format(self):
            return self.button.format

    #defining matrix elements from entries
    r1 = matrixElement(3, 0, "r1")
    r1.run()
    r2 = matrixElement(5, 0, "r2")
    r2.run()
    r3 = matrixElement(7, 0, "r3")
    r3.run()
    a11 = matrixElement(3, 2, "a11")
    a11.run()
    a12 = matrixElement(3, 4, "a12")
    a12.run()
    a13 = matrixElement(3, 6, "a13")
    a13.run()
    a21 = matrixElement(5, 2, "a21")
    a21.run()
    a22 = matrixElement(5, 4, "a22")
    a22.run()
    a23 = matrixElement(5, 6, "a23")
    a23.run()
    a31 = matrixElement(7, 2, "a31")
    a31.run()
    a32 = matrixElement(7, 4, "a32")
    a32.run()
    a33 = matrixElement(7, 6, "a33")
    a33.run()

    class Calcular:
        def __init__(self, r1, r2, r3, a11, a12, a13, a21, a22, a23, a31, a32, a33):
            
            self.nR1 = Complex(r1.get_format(), float(r1.get_entry()), float(r1.get_entry2()))
            self.nR2 = Complex(r2.get_format(), float(r2.get_entry()), float(r2.get_entry2()))
            self.nR3 = Complex(r3.get_format(), float(r3.get_entry()), float(r3.get_entry2()))
            self.nA11 = Complex(a11.get_format(), float(a11.get_entry()), float(a11.get_entry2()))
            self.nA12 = Complex(a12.get_format(), float(a12.get_entry()), float(a12.get_entry2()))
            self.nA13 = Complex(a13.get_format(), float(a13.get_entry()), float(a13.get_entry2()))
            self.nA21 = Complex(a21.get_format(), float(a21.get_entry()), float(a21.get_entry2()))
            self.nA22 = Complex(a22.get_format(), float(a22.get_entry()), float(a22.get_entry2()))
            self.nA23 = Complex(a23.get_format(), float(a23.get_entry()), float(a23.get_entry2()))
            self.nA31 = Complex(a31.get_format(), float(a31.get_entry()), float(a31.get_entry2()))
            self.nA32 = Complex(a32.get_format(), float(a32.get_entry()), float(a32.get_entry2()))
            self.nA33 = Complex(a33.get_format(), float(a33.get_entry()), float(a33.get_entry2()))

            #debugging obtained matrix elements
            """
            print(f"self.nR1.info() = {self.nR1.info()}")
            print(f"self.nR2.info() = {self.nR2.info()}")
            print(f"self.nR3.info() = {self.nR3.info()}")
            print(f"self.nA11.info() = {self.nA11.info()}")
            print(f"self.nA12.info() = {self.nA12.info()}")
            print(f"self.nA13.info() = {self.nA13.info()}")
            print(f"self.nA21.info() = {self.nA21.info()}")
            print(f"self.nA22.info() = {self.nA22.info()}")
            print(f"self.nA23.info() = {self.nA23.info()}")
            print(f"self.nA31.info() = {self.nA31.info()}")
            print(f"self.nA32.info() = {self.nA32.info()}")
            print(f"self.nA33.info() = {self.nA33.info()}")
            """

            self.matrix = Matrix3x3(self.nR1, self.nR2, self.nR3, self.nA11, self.nA12, self.nA13, self.nA21, self.nA22, self.nA23, self.nA31, self.nA32, self.nA33)

            self.label4 = Label(root, width=150, borderwidth=5, text=self.matrix.SolveDelta0()).grid(row=12, column=1, columnspan=10)
            self.label5 = Label(root, width=150, borderwidth=5, text=self.matrix.SolveDelta1()).grid(row=14, column=1, columnspan=10)
            self.label6 = Label(root, width=150, borderwidth=5, text=self.matrix.SolveDelta2()).grid(row=16, column=1, columnspan=10)
            self.label7 = Label(root, width=150, borderwidth=5, text=self.matrix.SolveDelta3()).grid(row=18, column=1, columnspan=10)
            self.label8 = Label(root, width=150, borderwidth=5, text=self.matrix.SolveUnknown(1)).grid(row=20, column=1, columnspan=10)
            self.label9 = Label(root, width=150, borderwidth=5, text=self.matrix.SolveUnknown(2)).grid(row=22, column=1, columnspan=10)
            self.label10 = Label(root, width=150, borderwidth=5, text=self.matrix.SolveUnknown(3)).grid(row=24, column=1, columnspan=10)

    #autoButtton for debug in matrix calculations
        """
        class Auto:
        def __init__(self):
            self.nR1 = Complex("Polar", 5, 5)
            self.nR2 = Complex("Polar", 5, 5)
            self.nR3 = Complex("Polar", 6, 7)

            self.nA11 = Complex("Polar", 4, 3)
            self.nA12 = Complex("Polar", 9, 50)
            self.nA13 = Complex("Polar", 7, 30)

            self.nA21 = Complex("Polar", 45, 80)
            self.nA22 = Complex("Polar", 6, 87)
            self.nA23 = Complex("Polar", 3, -45)

            self.nA31 = Complex("Polar", 2, -126)
            self.nA32 = Complex("Polar", 7, 280)
            self.nA33 = Complex("Polar", 10, -175)


            self.matrix = Matrix3x3(self.nR1, self.nR2, self.nR3, self.nA11, self.nA12, self.nA13, self.nA21, self.nA22, self.nA23, self.nA31, self.nA32, self.nA33)
            print(f"self.matrix.SolveDelta1() = {self.matrix.SolveDelta1()}")
            self.label4 = Label(root, width=150, borderwidth=5, text=self.matrix.SolveDelta0()).grid(row=12, column=1, columnspan=10)
            self.label5 = Label(root, width=150, borderwidth=5, text=self.matrix.SolveDelta1()).grid(row=14, column=1, columnspan=10)
            self.label6 = Label(root, width=150, borderwidth=5, text=self.matrix.SolveDelta2()).grid(row=16, column=1, columnspan=10)
            self.label7 = Label(root, width=150, borderwidth=5, text=self.matrix.SolveDelta3()).grid(row=18, column=1, columnspan=10)
            self.label8 = Label(root, width=100, borderwidth=5, text=self.matrix.SolveUnknown(1)).grid(row=20, column=1, columnspan=4)
            self.label9 = Label(root, width=100, borderwidth=5, text=self.matrix.SolveUnknown(2)).grid(row=22, column=1, columnspan=4)
            self.label10 = Label(root, width=100, borderwidth=5, text=self.matrix.SolveUnknown(3)).grid(row=24, column=1, columnspan=4)
        """
    #autoButton = Button(root, width=50, borderwidth=5, text=f"Preench Auto", command=lambda: Auto()).grid(row=10, column=6, columnspan=2, rowspan=2)    

    #detects r1 initial entries for debugging
        """
        print(f"r1.get_format() = {r1.get_format()}")
        print(f"r1.get_entry() = {r1.get_entry()}")
        print(f"r1.get_entry2() = {r1.get_entry2()}") 
        """

    label3 = Label(root, width=20, borderwidth=5, text=" ").grid(row=9, column=3, columnspan=2)
    readyButton = Button(root, width=50, borderwidth=5, text=f"Calcular", command=lambda: Calcular(r1, r2, r3, a11, a12, a13, a21, a22, a23, a31, a32, a33)).grid(row=10, column=3, columnspan=2, rowspan=2)

    root.mainloop()

if __name__=='__main__':
    main()