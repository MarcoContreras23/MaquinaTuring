dire = {'variables': {'00': '00',
                      '01': '00',
                      '10': '00',
                      '11': '00'}  # Se asigna el resultado de la operacion
        }


class MaquinaTuring:

    def __init__(self):
        self.cinta = []
        self.valor = ""
        self.valor2 = ""
        self.cadenaCodigos = ""
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

    def sumaBin(self, var1, var2):

        operacion = int(str(var1), 2) + int(str(var2), 2)
        resultado = int(bin(operacion)[2:])
        return resultado

    def restaBin(self, var1, var2):
        variable2 = self.complementoA2(var2)
        operacion = int(str(var1), 2) + int(str(variable2), 2)
        resultado = int(bin(operacion)[2:])
        return resultado

    def complementoA2(self, var):

        if var == '00':
            complementoA2 = "100"
        elif var == '10':
            complementoA2 = "10"
        elif var == "01":
            complementoA2 = "11"
        elif var == "11":
            complementoA2 = "01"

        return complementoA2

    # Obtiene los datos de las variables y valores ingresados
    def getvariableA(self):
        variableA = dire['variables']['00']
        return variableA

    def getVariableB(self):
        variableB = dire['variables']['01']
        return variableB

    def getVariableC(self):
        variableC = dire['variables']['10']
        return variableC

    def getVariableT(self):
        variableT = dire['variables']['11']
        return variableT

    def getValor(self):
        self.cadenaCodigos += self.valor
        return self.cadenaCodigos

    def getValor2(self, valor):
        return valor

    def escribirPrograma(self):

        print("----------------------------------")
        print("Ingrese 0 0 0 para asignar valores")
        print("Ingrese 0 0 1 para asignar variables")
        print("Ingrese 0 1 0 para desplazar")
        print("Ingrese 0 1 1 para Sumar")
        print("Ingrese 1 0 0 para restar")
        print("Ingrese 1 0 1 para inicio repetir")
        print("Ingrese 1 1 0 para fin repetir")
        print("Ingrese 1 1 1 para FIN de programa")
        print("----------------------------------")
        self.valor = input("Ingrese el valor ")
        # self.getValor()
        self.cinta.append(self.valor)
        bandera = 1
        contador = 0
        while self.valor != "111":
            while bandera != 0:
                if contador == 1:
                    print("----------------------------------")
                    print("Ingrese 0 0 0 para asignar valores")
                    print("Ingrese 0 0 1 para asignar variables")
                    print("Ingrese 0 1 0 para desplazar")
                    print("Ingrese 0 1 1 para Sumar")
                    print("Ingrese 1 0 0 para restar")
                    print("Ingrese 1 0 1 para inicio repetir")
                    print("Ingrese 1 1 0 para fin repetir")
                    print("Ingrese 1 1 1 para FIN de programa")
                    print("----------------------------------")
                    self.valor = input("Ingrese el valor ")
                    # self.getValor()
                    self.cinta.append(self.valor)

                if self.valor == "000":
                    # Se asignan las variables y el valor
                    self.valor2 = input(
                        "Asignar valor a las variables ingresando la variable y el valor separados por comas ")
                    self.cadenaCodigos += self.valor
                    self.cadenaCodigos += self.valor2
                    self.cinta.append(self.valor2)
                    # self.getValor2(valor2)
                    separado = self.valor2.split(',')
                    dire['variables'][separado[0]] = separado[1]
                    contador = 1

                elif self.valor == "001":
                    self.valor2 = input(
                        "Ingresar las variables a igual separadas por coma ")
                    # self.getValor2(valor2)
                    self.cadenaCodigos += self.valor
                    self.cadenaCodigos += self.valor2
                    self.cinta.append(self.valor2)
                    separado = self.valor2.split(',')
                    variable1 = separado[0]
                    valor1 = dire['variables'][variable1]
                    dire['variables'][separado[1]] = valor1
                    contador = 1

                elif self.valor == "010":
                    # Desplaza el valor de la variable
                    self.valor2 = input(
                        "Ingrese la variable y en el desplazamiento separado por coma siendo 0 = L y 1 = R ")
                    self.cadenaCodigos += self.valor
                    self.cadenaCodigos += self.valor2
                    # self.getValor2(valor2)
                    self.cinta.append(self.valor2)
                    separado = self.valor2.split(',')

                    if ((separado[0] == "00" and separado[1] == "1") or (separado[0] == "00" and separado[1] == "0") or (separado[0] == "01" and separado[1] == "1")
                            or (separado[0] == "10" and separado[1] == "0")):
                        dire['variables'][separado[0]] = "00"
                    elif ((separado[0] == "01" and separado[1] == "0") or (separado[0] == "11" and separado[1] == "0")):
                        dire['variables'][separado[0]] = "10"
                    elif ((separado[0] == "10" and separado[1] == "1") or (separado[0] == "11" and separado[1] == "1")):
                        dire['variables'][separado[0]] = "01"
                    contador = 1

                elif self.valor == "011":
                    self.valor2 = input(
                        "Ingrese las variables a sumar separadas por coma ")
                    self.cadenaCodigos += self.valor
                    self.cadenaCodigos += self.valor2
                    # self.getValor2(valor2)
                    self.cinta.append(self.valor2)
                    variables = self.valor2.split(',')
                    contador = 1
                    variable1 = variables[0]
                    variable2 = variables[1]
                    valor1 = dire['variables'][variable1]
                    valor2 = dire['variables'][variable2]
                    resultado = self.sumaBin(valor1, valor2)
                    dire['variables']['11'] = resultado

                elif self.valor == "100":
                    self.valor2 = input(
                        "Ingrese las variables a restar separadas por coma ")
                    self.cadenaCodigos += self.valor
                    self.cadenaCodigos += self.valor2
                    # self.getValor2(valor2)
                    self.cinta.append(self.valor2)
                    variables = self.valor2.split(',')
                    contador = 1
                    variable1 = variables[0]
                    variable2 = variables[1]
                    valor1 = dire['variables'][variable1]
                    valor2 = dire['variables'][variable2]
                    resultado = self.restaBin(valor1, valor2)
                    dire['variables']['11'] = resultado

                elif self.valor == "101":
                    self.valor2 = input("Ingrese cantidad de iteraciones ")
                    self.cadenaCodigos += self.valor
                    self.cadenaCodigos += self.valor2
                    # self.getValor2(valor2)
                    self.cinta.append("Z")
                    self.cinta.append(self.valor2)
                    contador = 1

                elif self.valor == "111":
                    # self.getValor2(valor2)
                    bandera = 0
                    valor = '111'
                else:
                    print("ingrese un codigo valido")
                    contador = 1
        print("El programa ingresado es ", self.cinta)
        print("El resultado del programa es ", dire['variables'])
