
if __name__ == "__main__":

    peso = float(input("Informe seu peso em kg: "))
    altura = float(input("informe a sua altura em metros: "))

    imc = peso / (altura ** 2)

    if imc < 18.5:
        print(f"Seu IMC é de {imc}. Você está abaixo do peso")

    elif imc >= 18.5 and imc <= 24.9:
        print(f"Seu IMC é de {imc}. Você está com o peso normal")

    elif imc >= 25 and imc <= 29.9:
        print(f"Seu IMC é de {imc}. Você está com o sobrepeso")

    elif imc >= 30 and imc <= 34.9:
        print(f"Seu IMC é de {imc}. Você está com obesidade grau I.")

    elif imc >= 35 and imc <= 39.9:
        print(f"Seu IMC é de {imc}. Você está com obesidade grau II.")

    else:
        print(f"Seu IMC é de {imc}. Você está com grau de obesidade III.")

