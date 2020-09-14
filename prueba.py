def asignarValores():
    resultado = 1 + 1
    print(resultado,'que emocion')
def asignarVariables(self):
    pass
def desplazar():
    pass
def sumar(self):
    pass
def restar(self):
    pass
def inicioRepetir(self):
    pass
def finRepetir(self):
    pass
def finPrograma(self):
    pass

dire = {'variables': {'00': '00',
                      '01': '00',
                      '10': '00',
                      '11': '00'},
        'codigos':{ '000': asignarValores,
                    '001' : asignarVariables,
                    '010': desplazar,
                    '011': sumar,
                    '100': restar,
                    '101': inicioRepetir,
                    '110': finRepetir,
                    '111': finPrograma}}

def __init__(self):
        self.cinta = []
        self.A = "00" 
        self.B = "00" 
        self.C = "00"
        self.T = "00"
    
def configurarMaquina(self):
        self.cinta.append(self.A)
        self.cinta.append(self.B)
        self.cinta.append(self.C)
        self.cinta.append(self.T)
        self.cinta.append("Z")

def escribirPrograma():
    cinta = []
    cinta.append("00")
    cinta.append("00")
    cinta.append("00")
    cinta.append("00")
    cinta.append("Z")
    print("Ingrese 0 0 0 para asignar valores")
    print("Ingrese 0 0 1 para asignar variables")
    print("Ingrese 0 1 0 para desplazar")
    print("Ingrese 0 1 1 para Sumar")
    print("Ingrese 1 0 0 para restar")
    print("Ingrese 1 0 1 para inicio repetir")
    print("Ingrese 1 1 0 para fin repetir")
    print("Ingrese 1 1 1 para FIN de programa")
    valor = input("Ingrese el valor ")
    cinta.append(valor)
    bandera = 1
    contador = 0
    while valor != "111":
        while bandera != 0:
            if contador == 1:
                valor = input("Ingrese el valor ")
                cinta.append(valor)

            if valor == "000":
                #Se asignan las variables y el valor 
                valor2 = input("Asignar valor a las variables ingresando la variable y el valor separados por comas ")
                cinta.append(valor2)
                separado = valor2.split(',')
                dire['codigos'][valor]()
                dire['variables'][separado[0]] = separado[1]
                contador = 1

            elif valor == "001":
                valor2 = input("Asignar variables ")
                cinta.append(valor2)

            elif valor == "010":
                #Desplaza el valor de la variable 
                valor2 = input("Ingrese la variable y en el desplazamiento separado por coma siendo 0 = L y 1 = R ")
                cinta.append(valor2)
                separado = valor2.split(',')

                if ((separado[0] == "00" and separado[1] == "1") or (separado[0] == "00" and separado[1] == "0") or (separado[0] == "01" and separado[1] == "1") 
                    or (separado[0] == "10" and separado[1] == "0")):
                    dire['codigos'][valor]()
                    dire['variables'][separado[0]] = "00"
                elif ( (separado[0] == "01" and separado[1] == "0") or (separado[0] == "11" and separado[1] == "0")):
                    dire['codigos'][valor]()
                    dire['variables'][separado[0]] = "10"
                elif ( (separado[0] == "10" and separado[1] == "1") or (separado[0] == "11" and separado[1] == "1")):
                    dire['codigos'][valor]()
                    dire['variables'][separado[0]] = "01"
                contador = 1

            elif valor == "011":
                valor2 = input("Ingrese las variables a sumar ")
                cinta.append(valor)
            elif valor == "100":
                valor2 = input("Ingrese las variables a restar ")
                cinta.append(valor)
            elif valor == "101":
                valor2 = input("Ingrese cantidad de iteraciones ")
                cinta.append(valor)
            elif valor == "111":
                bandera = 0
                valor = '111'
    print("El programa ingresado es ", cinta)
    print("El resultado del programa es " , dire['variables'])

escribirPrograma()

