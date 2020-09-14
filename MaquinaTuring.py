import ventana

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
        valor = input("Ingrese el valor")
        self.cinta.append(valor)
        print(self.cinta)


    def entradas(self):
        print("Ingrese 0 0 0 para asignar valores")
        print("Ingrese 0 0 1 para asignar variables")
        print("Ingrese 0 1 0 para desplazar")
        print("Ingrese 0 1 1 para Sumar")
        print("Ingrese 1 0 0 para restar")
        print("Ingrese 1 0 1 para inicio repetir")
        print("Ingrese 1 1 0 para fin repetir")
        print("Ingrese 1 1 1 para FIN de programa")
    

    
    """def movimiento(self, ins):
		if ins == "R" :
			self.posicion += 1
		if ins == "L":
			self.posicion -= 1

def configCinta(n, cinta, c):
	for i in range (0, n):
		cinta[i] = c"""


