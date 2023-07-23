import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Brayam Felipe
apellido:Torres Rojas
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acomulador_suma_negativos= 0
        acomulador_suma_positivos= 0 
        contador_positivos= 0 
        contador_negativos= 0
        contador_ceros= 0
        numero=" "
        diferencia = 0

        while numero != None:
            numero= prompt(title="EJ10", prompt="Ingrese numero")

            if numero != None:
                numero=int(numero)

                if numero < 0 :
                    acomulador_suma_negativos= acomulador_suma_negativos + numero
                    contador_negativos=contador_negativos + 1
                elif numero > 0:
                    acomulador_suma_positivos=acomulador_suma_positivos + numero
                    contador_positivos= contador_positivos + 1
                else:
                    contador_ceros= contador_ceros + 1

        diferencia=contador_positivos - contador_negativos

        mensaje= f"la suma acomulada de los negativos es:{acomulador_suma_negativos}\n"
        mensaje += f"la suma acomulada de los positivos {acomulador_suma_positivos}\n"
        mensaje += f"cantidad de numeros positivos ingresados {contador_positivos}"
        mensaje += f"cantidad de nuemros negativos {contador_negativos}"
        mensaje += f"cantidad de ceros {contador_ceros}"
        mensaje += f"diferencia entre la cantidad de los numeros positivos ingresados y los negativos es: {diferencia}"

        alert(title="EJ10" , message=mensaje)




    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
