class Retangulo:
    lado_a = None
    lado_b = None

    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
        print "Criando nova instancia do Retangulo"

    def calcula_area(self):
        return self.lado_a * self.lado_b

    def calcula_perimetro(self):
        return 2 * self.lada_a + 2 * self.lado_b


r = Retangulo(12, 15)
print r

