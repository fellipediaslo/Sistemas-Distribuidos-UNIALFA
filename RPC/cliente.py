import Pyro4

# Cria um proxy para se conectar ao servidor Pyro
def main():
    calculadora = Pyro4.Proxy("PYRO:obj_2ba5d18568cc4e7cae2f5f8878989319@localhost:54029")  # Substitua 'obj_123456' pelo URI do servidor
    
    # Chamada para o método somar
    resultado_soma = calculadora.somar(85, 3)
    print("A soma é:", resultado_soma)

    # Chamada para o método subtrair
    resultado_subtracao = calculadora.subtrair(85, 3)
    print("A subtração é:", resultado_subtracao)

    # Chamada para o método multiplicar
    resultado_multiplicacao = calculadora.multiplicar(85, 3)
    print("A multiplicação é:", resultado_multiplicacao)

if __name__ == "__main__":
    main()
