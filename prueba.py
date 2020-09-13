def asignarValores():
    resultado = 1 + 1
    print(resultado,'que emocion')
def asignarVariables(self):
    pass
def desplazar(self):
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

dire['variables']['00'] = 'gracias'
dire['codigos']['000']()

