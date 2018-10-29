from classes import maior, soma, media, valores_iguais, indice_prim_valor_igual
import random

def main():
    valores1 = [random.randint(0, x + 10) for x in range(10)]
    valores2 = [random.randint(0, x + 10) for x in range(10)]
    valor_x = random.randint(0, 10)
    valor_y = random.randint(0, 10)

    print(f'DADOS')
    print(f'1a lista gerada randomicamente: {valores1}')
    print(f'2a lista gerada randomicamente: {valores2}')
    print(f'Numero gerado randomicamente (0 ~ 10) - X: {valor_x}')
    print(f'Numero gerado randomicamente (0 ~ 10) - Y: {valor_y}')

    print(f'\nAPLICANDO AS FUNÇÕES:')
    print(f'1 - maior valor entre X,Y: {maior(valor_x, valor_y)}')
    print(f'2 - soma da 1a lista com Y: {soma(valores1, valor_y)}')
    print(f'3 - valores iguais da 1a lista e 2a lista: {valores_iguais(valores1, valores2)}')
    print(f'4 - indice primario igual: {indice_prim_valor_igual(valores1, valores2)}')

if __name__ == "__main__":
    main()
