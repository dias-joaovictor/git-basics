from helloworld import hello_world
from geometrica import *

if __name__ == '__main__':
    hello_world()
    print("-------------Iniciando calculadora----------------")
    print(calcular_area_retangulo(4, 5, 'm2'))
    print(calcular_area_retangulo(4, 4, 'm2'))

    # Escrever a função no script geometrica e considerar pi = 3.1415
    print(calcular_area_circunferencia(3, 'm2'))

    # Escrever um novo script(de um nome qualquer que faça sentido),
    # 1 - Programar nele uma função que irá receber 2 notas e calcular uma média
    # 2 - Programar uma função que receba 3 notas, calcule a média aritmética e diga se o aluno está abaixo da média, na média ou acima da média.
    #
    # 2.1
    # se estiver abaixo de 7 é "abaixo da média"
    # se estiver com média igual a 7 é "Na média"
    # se estiver com média acima de 7 é "Acima da média"
    print("-------------Finalizando calculadora----------------")
