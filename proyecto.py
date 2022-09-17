
from complejos import *

import math

def accion_vector(matrix, vector):
        if len(matrix[0]) == len(vector):
            accionv = []
            for i in range(len(matrix)):
                accionv.append((0, 0))
            for i in range(len(matrix)):
                for j in range(len(vector)):
                    for k in range(len(matrix[0])):
                        accionv[i] = suma_complejos(accionv[i], multiplicacion_complejos(matrix[i][k], vector[j]))
            return accionv
        else:
            return False

def adjuntam(matriz):
    matrizd = conjm(transpuesta(matriz))

    return matrizd

def conjm(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = conjugado_complejos(matriz[i][j])

    return matriz  

def conjv(lista):

    for i in range(len(lista)):
        lista[i] = conjugado_complejos(lista[i])
    return lista  

def transpuesta(lista):
    transp = []
    for i in range(len(lista[0])):
        transp.append([])
        for j in range(len(lista)):
            transp[i].append(lista[j][i])

    return transp

def multiesc_matrix(complexn, matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = multiplicacion_complejos(complexn, matrix[i][j])

    return matrix

def inversa_matrizc(matrizc):
    for i in range(len(matrizc)):
        for j in range(len(matrizc[0])):
            matrizc[i][j] = multiplicacion_complejos((-1, 0), matrizc[i][j])

    return matrizc

def suma_matricesc(matrizc1, matrizc2):
    if len(matrizc1) == len(matrizc2) and len(matrizc1[0]) == len(matrizc2[0]):
        line = [(0, 0)] * len(matrizc1[0])
        matriz_r = [line] * len(matrizc1)
        for j in range(len(matrizc1)):
            for k in range(len(matrizc1[0])):
                matriz_r[j][k] = suma_complejos(matrizc1[j][k], matrizc2[j][k])

    return matriz_r

def multiplicacion_escalar(complex_num, complex_v):
    r_vector = [(0, 0)] * len(complex_v)
    for x in range(len(complex_v)):
        r_vector[x] = multiplicacion_complejos(complex_num, complex_v[x])

    return r_vector

def vectorcx_invers(vectorc):
    inverso = [(0, 0)] * len(vectorc)
    for x in range(len(vectorc)):
        inverso[x] = multiplicacion_complejos((-1, 0), vectorc[x])

    return inverso

def suma_vectorescpx(vectorc_1, vectorc_2):
    if len(vectorc_1) == len(vectorc_2):
        vctor = [(0, 0)] * len(vectorc_1)
        for x in range(len(vectorc_1)):
            vctor[x] = (suma_complejos(vectorc_1[x], vectorc_2[x]))

    return vctor

def inproduct(vectorc1, vectorc2):
    if len(vectorc1) == len(vectorc2):
        productointr = (0, 0)
        vectorc1 = conjv(vectorc1)
        for i in range(len(vectorc1)):
            productointr = suma_complejos(productointr, multiplicacion_complejos(vectorc1[i], vectorc2[i]))

        return productointr
    else:
        return False

def norma_v(vectorc):
    productointr = inproduct(vectorc, vectorc)
    norma = modulo_complejos(productointr)
    return norma

def unitaria(matriz):
    matrizalpha = adjuntam(matriz)
    id = [[(0, 0) for i in range(len(matriz[0]))] for j in range(len(matriz))]
    for i in range(len(id)):
        for j in range(len(id[0])):
            if i == j:
                id[i][j] = (1, 0)
    if multiplicacion_matrices(matrizalpha, matriz) == id:
        return True
    else:
        return False

def distanciav(vectorc1, vectorc2):
    if len(vectorc1) == len(vectorc2):
        diferencia = []
        for i in range(len(vectorc1)):
            diferencia.append(resta_complejos(vectorc1[i], vectorc2[i]))
    productodif = inproduct(diferencia, diferencia)
    distancia = modulo_complejos(productodif)

    return distancia

def hermitiana(matriz):
    matrizher = adjuntam(matriz)
    if matrizher == matriz:
        return True
    else:
        return False

def tensor_prod(vectorco1, vectorco2):
   
    tensorg = len(vectorco1) * len(vectorco2)
    R = [(0, 0)] * tensorg
    index = 0
    for i in range(len(vectorco1)):
        for j in range(len(vectorco2)):
            R[index] = multiplicacion_complejos(vectorco1[i], vectorco2[j])
            index += 1

    return R

def multiplicacion_matrices(matrix1, matrix2):
    if len(matrix1[0]) == len(matrix2):
        matrixmul = []
        for i in range(len(matrix1)):
            matrixmul.append([])
            for j in range(len(matrix2[0])):
                matrixmul[i].append((0, 0))
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix1[0])):
                    matrixmul[i][j] = suma_complejos(matrixmul[i][j],
                                                   multiplicacion_complejos(matrix1[i][k], matrix2[k][j]))

        return matrixmul
    else:
        return False

    
