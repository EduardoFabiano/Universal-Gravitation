G = 6.6743e-11

def calcular_forca_gravitacional():
    print("Calculadora de Gravitação Universal")
    try:
        m1 = float(input("Digite a massa do primeiro corpo (em kg): "))
        m2 = float(input("Digite a massa do segundo corpo (em kg): "))
        distancia = float(input("Digite a distância entre os centros dos corpos (em metros): "))
        
        if distancia <= 0:
            print("Erro: A distância deve ser maior que zero.")
            return

        forca = G * (m1 * m2) / (distancia ** 2)
        
        print("Resultado")
        print(f"A força de atração gravitacional é: {forca:.4e} Newtons (N)")
        
    except ValueError:
        print("Erro: Por favor, insira apenas valores numéricos válidos.")

if __name__ == "__main__":
    calcular_forca_gravitacional()
