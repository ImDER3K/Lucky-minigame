import tkinter as tk
import random

class Inicio:
    def __init__(self, ventana_inicio):
        self.ventana_inicio = ventana_inicio
        self.ventana_inicio.title("Lucky")
        self.ventana_inicio.configure(bg='Gray21')

        # Crear rectángulo decorativo
        self.crear_rectangulo_decorativo('left')
        self.crear_rectangulo_decorativo('right')


        self.etiqueta_titulo = tk.Label(ventana_inicio, text="____________", bg='Gray21', fg='white', font=("Karma Future", 16))
        self.etiqueta_titulo.pack(pady=20)

        # Cambiar el color de "Lucky" a verde
        self.etiqueta_lucky = tk.Label(ventana_inicio, text="Lucky", bg='Gray21', fg='seagreen2', font=("Karma Future", 25, 'bold'))
        self.etiqueta_lucky.pack(pady=20)

        self.etiqueta_titulo_continuacion = tk.Label(ventana_inicio, text="____________", bg='Gray21', fg='white', font=("Karma Future", 16))
        self.etiqueta_titulo_continuacion.pack(pady=20)

        self.boton_iniciar = tk.Button(ventana_inicio, text="Iniciar Juego", command=self.iniciar_juego, bd=2, relief=tk.FLAT, bg='seagreen2', fg='white', font=("Arial", 12))
        self.boton_iniciar.pack(pady=20)

        self.etiqueta_titulo_continuacion = tk.Label(ventana_inicio, text="- by Der3k-_-!", bg='Gray21', fg='white', font=("Karma Future", 16))
        self.etiqueta_titulo_continuacion.pack(pady=20)

        


    def crear_rectangulo_decorativo(self, lado):
        frame_decorativo = tk.Frame(self.ventana_inicio, width=10, height=self.ventana_inicio.winfo_screenheight(), bg='seagreen2')
        frame_decorativo.pack(side=lado, fill=tk.Y)

    def iniciar_juego(self):
        self.ventana_inicio.destroy()
        nueva_ventana = tk.Tk()
        nuevo_juego = MiniJuego(nueva_ventana)

class MiniJuego:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lucky by Der3k-_-")
        self.ventana.configure(bg='Gray21')  # Establecer el color de fondo

        self.puntuacion = 0
        self.intentos_restantes = 3
        self.numero_secreto = 0
        self.iniciar_nueva_ronda()

        self.etiqueta_instrucciones = tk.Label(ventana, text="Adivina el número del 1 al 10:", fg="SeaGreen1", bg='Gray21', font=("Karma Future", 12))
        self.etiqueta_instrucciones.pack(pady=10)

        self.entrada_numero = tk.Entry(ventana, justify='center', borderwidth=0, font=("Arial", 12))
        self.entrada_numero.pack(pady=10)

        self.etiqueta_puntuacion = tk.Label(ventana, text=f"Puntuación: {self.puntuacion}", bg='Gray21', fg='white')
        self.etiqueta_puntuacion.pack()

        self.boton_adivinar = tk.Button(ventana, text="Adivinar", command=self.verificar_adivinanza, bd=2, relief=tk.FLAT, bg='seagreen2', fg='white', font=("Arial", 12))
        self.boton_adivinar.pack()

        # Palabras
        texto_personalizado = "by: DER3K-_-"
        etiqueta = tk.Label(ventana, text=texto_personalizado, fg="SeaGreen1", bg='Gray21', font=("Arial", 7))
        etiqueta.pack(padx=100)

    def crear_rectangulo_decorativo(self, lado):
        frame_decorativo = tk.Frame(self.ventana, width=10, height=self.ventana.winfo_screenheight(), bg='seagreen2')
        frame_decorativo.pack(side=lado)

    def iniciar_nueva_ronda(self):
        self.numero_secreto = random.randint(1, 10)

    def verificar_adivinanza(self):
        intento = int(self.entrada_numero.get())
        if intento == self.numero_secreto:
            self.puntuacion += 5
            self.intentos_restantes = 3  # Reiniciar el contador de intentos restantes
            self.iniciar_nueva_ronda()
            mensaje = f"¡Correcto! ¡Has adivinado el número! Puntuación: {self.puntuacion}"
        else:
            self.intentos_restantes -= 1
            self.puntuacion -= 1
            mensaje = f"Incorrecto. ¡Inténtalo de nuevo! Intentos restantes: {self.intentos_restantes}"

            if self.intentos_restantes == 0 or self.puntuacion < 0:
                self.mostrar_pantalla_perdida()
                return

        # Actualizar la etiqueta de la puntuación
        self.etiqueta_puntuacion.config(text=f"Puntuación: {self.puntuacion}")

        resultado_label = tk.Label(self.ventana, text=mensaje, bg='Gray21', fg='white')
        resultado_label.pack(pady=10)

    def mostrar_pantalla_perdida(self):
        self.boton_adivinar.config(state=tk.DISABLED)  # Deshabilitar el botón
        mensaje_perdida = f"¡Perdiste! Tu puntuación es menor que 0."
        etiqueta_perdida = tk.Label(self.ventana, text=mensaje_perdida, font=("Arial", 16), bg='Gray21', fg='red3')
        etiqueta_perdida.pack(pady=20)

        boton_reiniciar = tk.Button(self.ventana, text="Reiniciar Juego", command=self.reiniciar_juego, bd=2,relief=tk.FLAT, bg='red3', fg='white', font=("Arial", 12),)
        boton_reiniciar.pack()

    def reiniciar_juego(self):
        self.ventana.destroy()  # Cerrar la ventana actual

        # Crear una nueva ventana y reiniciar el juego
        nueva_ventana = tk.Tk()
        nuevo_juego = MiniJuego(nueva_ventana)

# Crear la ventana de inicio
ventana_inicio = tk.Tk()
inicio = Inicio(ventana_inicio)

# Iniciar el bucle principal
ventana_inicio.mainloop()
