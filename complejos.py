
import math

def suma_vectorescpx(vectorc_1, vectorc_2):
    :param vectorc_1: vector complejo
    :return: vector suma
    if len(vectorc_1) == len(vectorc_2):
        svector = [(0, 0)] * len(vectorc_1)
        for x in range(len(vectorc_1)):
            svector[x] = (suma_complejos(vectorc_1[x], vectorc_2[x]))

    return svector


def conjugado_complejos(par):
    new_b = par[1] * -1
    new_par = (par[0], new_b)

    return new_par


def modulo_complejos(par):
    modulo = (par[0] ** 2 + par[1] ** 2)

    return round(math.sqrt(modulo), 2)


def resta_complejos(par1, par2):
    :rtype: tuple
    result = (round(par1[0] - par2[0], 2), round(par1[1] - par2[1], 2))

    return result


def suma_complejos(par1, par2):
    :type par1: tuple
    result = (round(par1[0] + par2[0], 2), round(par1[1] + par2[1], 2))

    return result


def multiplicacion_complejos(par1, par2):
    result = (round((par1[0] * par2[0]) - (par1[1] * par2[1]), 2), round((par1[0] * par2[1]) + (par1[1] * par2[0]), 2))

    return result


def division_polar(polar1, polar2):
    complejo_polar = (round(polar1[0] / polar2[0], 2), round(polar1[1] - polar2[1], 2))

    return complejo_polar


def multiplicacion_polar(polar1, polar2):
    complejo_polar = (round(polar1[0] * polar2[0], 2), round(polar1[1] + polar2[1], 2))

    return complejo_polar
  