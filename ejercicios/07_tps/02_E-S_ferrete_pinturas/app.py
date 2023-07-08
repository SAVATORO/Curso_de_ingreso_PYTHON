import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

2.	Para el departamento de Pinturas:
	A.	Al ingresar una temperatura en Fahrenheit debemos mostrar la temperatura en Centígrados con un mensaje concatenado 
        (0 °F − 32) × 5/9 = -17,78 °C

    B.	Al ingresar una temperatura en Centígrados debemos mostrar la temperatura en Fahrenheit 
        (0 °C × 9/5) + 32 = 32 °F

    
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Temperatura °C")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_temperatura_c = customtkinter.CTkEntry(master=self)
        self.txt_temperatura_c.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Temperatura °F")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_temperatura_f = customtkinter.CTkEntry(master=self)
        self.txt_temperatura_f.grid(row=1, column=1)
       
        self.btn_convertir_c_f = customtkinter.CTkButton(master=self, text="Convertir °C a °F", command=self.btn_convertir_c_f_on_click)
        self.btn_convertir_c_f.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_convertir_f_c = customtkinter.CTkButton(master=self, text="Convertir °F a °C", command=self.btn_convertir_f_c_on_click)
        self.btn_convertir_f_c.grid(row=4, pady=10, columnspan=2, sticky="nsew")
    
    def btn_convertir_c_f_on_click(self):
        temperatura_c = self.txt_temperatura_c.get()
        temperatura_c = float(temperatura_c)

        convertir_f = (temperatura_c * 9/5) + 32 
        convertir_f = int(convertir_f)

        mensaje = f"{convertir_f} °f"

        self.txt_temperatura_f.delete(0,100)
        self.txt_temperatura_f.insert(0,convertir_f)
        alert(title="resultado", message=mensaje)
        






        
        

    def btn_convertir_f_c_on_click(self):
        temperatura_f = self.txt_temperatura_f.get()
        temperatura_f = float(temperatura_f)

        convertir_c = (temperatura_f - 32) * 5/9
        convertir_c = int(convertir_c) 

        mensaje = f"{convertir_c} °C"

        self.txt_temperatura_c.delete(0,100)
        self.txt_temperatura_c.insert(0,convertir_c)
        alert(title="resultado", message=mensaje)
        
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()