def quadrado(lado):
    if lado < 0:
        return -1.00
    else:
        return lado * lado

def retangulo(base, altura):
    if base < 0 or altura < 0:
        return -1.00
    else:
        return base * altura

def circulo(raio):
    if raio < 0:
        return -1.00
    else:
        return 3.14 * (raio ** 2)

def resumo(listaQuadrado, listaRetangulo, listaCirculo):
    print("Maior circulo: {:.2f}".format(listaCirculo[0]))
    print("Maior retangulo: {:.2f}".format(listaRetangulo[0]))
    print("Maior quadrado: {:.2f}".format(listaQuadrado[0]))
    print("Quantidade de figuras", quantFiguras)
    print("Percentual de circulos: {:.2f}".format((len(listaCirculo) / quantFiguras) * 100))

listaQuadrado = []
listaRetangulo = []
listaCirculo = []
quantFiguras = 0
while True:
    figura = str(input()).lower()

    if figura == "q":
        lado = float(input())
        listaQuadrado.append(quadrado(lado))

    elif figura == "r":
        base = float(input())
        altura = float(input())
        listaRetangulo.append(retangulo(base, altura))

    elif figura == "c":
        raio = float(input())
        listaCirculo.append(circulo(raio))

    elif figura == "sair":
        break

    quantFiguras += 1

listaQuadrado.sort(reverse=True)
listaRetangulo.sort(reverse=True)
listaCirculo.sort(reverse=True)

resumo(listaQuadrado, listaRetangulo, listaCirculo)