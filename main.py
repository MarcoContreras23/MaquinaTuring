class MaquinaTuring:

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

    def escribirPrograma(self):

        print("Ingrese 0 0 0 para asignar valores")
        print("Ingrese 0 0 1 para asignar variables")
        print("Ingrese 0 1 0 para desplazar")
        print("Ingrese 0 1 1 para Sumar")
        print("Ingrese 1 0 0 para restar")
        print("Ingrese 1 0 1 para inicio repetir")
        print("Ingrese 1 1 0 para fin repetir")
        print("Ingrese 1 1 1 para FIN de programa")
        valor = input("Ingrese el valor ")
        self.cinta.append(valor)
        bandera = 1
        while valor != "111":
            while bandera != 0:
                if valor == "000":
                    valor2 = input("Asignar valor a las variables ")
                    self.cinta.append(valor)
                elif valor == "001":
                    valor2 = input("Asignar variables ")
                    self.cinta.append(valor)
                elif valor == "010":
                    valor2 = input("identifique variable y sentido para desplazar ")
                    self.cinta.append(valor)
                elif valor == "011":
                    valor2 = input("Ingrese las variables a sumar ")
                    self.cinta.append(valor)
                elif valor == "100":
                    valor2 = input("Ingrese las variables a restar ")
                    self.cinta.append(valor)
                elif valor == "101":
                    valor2 = input("Ingrese cantidad de iteraciones ")
                    self.cinta.append(valor)
        print(self.cinta)


def main():
    maquina = MaquinaTuring()
    maquina.configurarMaquina()
    maquina.escribirPrograma()
main()
