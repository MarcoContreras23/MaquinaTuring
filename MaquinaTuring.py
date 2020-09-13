class MaquinaTuring:

    def __init__(self):
        self.cinta = []
        self.A = "00" 
        self.B = "B0" 
        self.C = "00"
        self.T = "00"
    
    def configurarMaquina(self):
        self.cinta.append(self.A)
        self.cinta.append(self.B)
        self.cinta.append(self.C)
        self.cinta.append(self.T)
        self.cinta.append("Z")
    
    
    

    def movimiento(self, ins):
		if ins == "R" :
			self.posicion += 1
		if ins == "L":
			self.posicion -= 1

def configCinta(n, cinta, c):
	for i in range (0, n):
		cinta[i] = c


