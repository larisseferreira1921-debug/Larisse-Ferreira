# Classe base
class Veiculo:
    def _init_(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_dados(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)


# Classe filha Carro
class Carro(Veiculo):
    def realizar_entrega(self):
        print("O carro está transportando várias encomendas.")


# Classe filha Moto
class Moto(Veiculo):
    def realizar_entrega(self):
        print("A moto está fazendo uma entrega rápida.")


# Classe filha Bicicleta
class Bicicleta(Veiculo):
    def realizar_entrega(self):
        print("A bicicleta está realizando uma entrega ecológica.")


# Criando objetos (instâncias)
carro1 = Carro("Toyota", "Corolla", 2022)
moto1 = Moto("Honda", "CG 160", 2021)
bike1 = Bicicleta("Caloi", "Elite", 2023)


# Mostrando informações e ações
print("=== CARRO ===")
carro1.mostrar_dados()
carro1.realizar_entrega()

print("\n=== MOTO ===")
moto1.mostrar_dados()
moto1.realizar_entrega()

print("\n=== BICICLETA ===")
bike1.mostrar_dados()
bike1.realizar_entrega()

