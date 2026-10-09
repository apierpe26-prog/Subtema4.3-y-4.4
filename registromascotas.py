import os
nombre_mascotas=[""]*3
edad_mascotas=[0]*3

def insertar():
    for i in range(len(nombre_mascotas)):
        nombre_mascotas[i]= input(f"ingrese nombre de la mascota: ")
        edad_mascotas[i]= int(input(f"ingrese edad de la mascota: "))
def mostrar():
    for i in range(len(nombre_mascotas)):
        nombre_mascotas[i]= input(f"ingrese nombre de la mascota: ")
        print(f"nombre: {nombre_mascota[i]} , edad: {edad_mascotas[i]}")

def main():
    global nombre_mascotas, edad_mascotas
    nombre_mascotas=[""]*3
    edad_mascotas=[0]*3 #iniciar la lista vacia para numeros enteros de longitud 3

    opcion=0
    while opcion != 4:  ## opcion distinto a 4 (true)
        os.system ('cls' if os.name=='nt' else 'clear')
        print("[1] Insertar mascota (nombre | edad)")
        print("[2] Mostrar mascotas (nimbre | edad)")
        print("[3] Eliminar mascota por nombre (en ambos vectores)")
        print("[4] Salir")
        opcion = int(input("escoga la opcion: ")) 


        if opcion==1:
            print("insertar")
        elif opcion==2:
            print("mostra")
        elif opcion==3:
            print("eliminar")
        elif opcion==4:
            print("saliendo...")
        else: print("ipcion invalida")
        if opcion !=4: input("presione para continuar..")
main()