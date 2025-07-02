class Persona():
    nombre=""
    edad=0
    dni=0
    sexo=""
    peso=0.0
    altura=0.0
    #ACONTINUACION ESTA EL CONTRUCCTOR PARA DARLE LOS VALORES
    def __init__(self,nombre="",edad=0,dni=0,sexo="",peso=0,altura=0):
        self.nombre=nombre#SELF. HACE REFERENCIA A LA PRIMER VARIABLE, SIN SELF A LO QUE ESTA DENTRO DEL ()
        self.edad=edad
        self.dni=dni
        self.sexo=sexo
        self.peso=peso
        self.altura=altura
    #ESTE DEF SERIA LOS METODOS, LAS ACCINES A REALIZAR
    def calcularIMC(self):
        imc=self.peso/(self.altura**2)
        if imc<20:
            return -1
        elif imc<=25:
            return 0
        else:
            return 1
    def esMayorDeEdad(self):
        if self.edad>=18:
            return True
        else:
            return False
    def ComprobarSexo(self,sexo):
        if self.sexo==sexo:
            return True
        else:
            return False
    def __str__(self):
        return (f"nombre: {self.nombre} edad: {self.edad} dni: {self.dni} sexo: {self.sexo} peso: {self.peso} altura: {self.altura}")
        # return 'nombre: ' + self.nombre  +  '\nEdad '+str(self.edad) + '\nDni '+str(self.dni)

nombre=input("Ingrese el nombre: ")
dni=input("Ingrese el dni: ")
edad=int(input("Ingrese la edad: "))
sexo=input("Ingrese sexo: ")  
peso=float(input("Ingrese peso: "))  
altura=float(input("Ingrese altura: "))  

objetoP=Persona(nombre,edad,dni,sexo,peso,altura)
while True:
    print("1- Calcular IMC")
    print("2- Es mayor de edad")
    print("3- Comprobar sexo")
    print("4- Imprimir todos los datos")
    print("5- Salir")
    opcion=input("Ingrese la opcion deseada: ")
    match opcion:
        case "1":
            imc=objetoP.calcularIMC()
            if imc==-1:
                print("Bajo Peso")
            elif imc==0:
                print("Peso normal")
            else:
                print("Sobrepeso")
        case "2":
            if objetoP.esMayorDeEdad():
                print("Es mayor")
            else:
                print("Es menor")
        case "3":
            sexo=input("Ingrese Sexo")
            if objetoP.ComprobarSexo(sexo):
                print("El sexo ingresado es correcto")
            else:
                print("El sexo ingresado es incorrecto")
        case "4":
            print(objetoP.__str__())
        case "5":
            break
            

# jjjjjj