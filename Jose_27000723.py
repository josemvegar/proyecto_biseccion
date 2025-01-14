#!/usr/bin/env python3
"""
Proyecto en Python sobre el Algoritmo de Bisección.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math


#def biseccion(a, b, ER, N, mx, m, n,err):
def biseccion(f, a, b, ER, N):
    n=int
    m=float
    mx =float
    """
    Implementa el Algoritmo de Biseccion y retorna la aproximación de la raiz.

    Parámetros:
    f: función de variable real f(x).
    a: límite inferior del intervalo.
    b: límite superior del intervalo.
    ER: cota mínima del error relativo.
    N: número máximo de iteraciones.
    """
    n=0
    while (n<N):
        if (n != 0):
            if (f(a)>0 and f(mx)<0):
                b= mx
            if ( f(a)<0 and f(mx) >0):
                a=a
            if (f(mx)>0 and f(b)<0 ):
                a= mx
            if ( f(mx)<0 and f(b)>0):
                b= b
            mx=(a+b)/2
            n=n+1
            err= (mx - m) / mx
            m=mx
            if (err <0):
                err=err*-1
            if (err> ER):
                if (n!=N):
                    print("Iteración:", n, "Punto Medio:", mx, "Error:", err)
                    #mx=biseccion (a, b , ER, N, mx, m, n, err)
                else:
                    print("Iteración:", n, "Punto Medio:", mx, "Error:", err)
                    print ("Fin de las iteraciones por cantidad máxima alcanzada.")
                    n=N
            else:
                print("Iteración:", n, "Punto Medio:", mx, "Error:", err)
                print ("Fin de las iteraciones,  error menor el indicado.")
                n=N
        else:
            n=n+1
            m=(a+b)/2
            mx=m
            print("Iteración:", n, "Punto Medio:", mx, "Error: La primera iteración no lleva cálculo de error")
            #mx= biseccion(a,b,ER,N,mx, m, n, err)
            
    return mx

def f(x):
    print ("f(x)")
    return lambda x: math.cos(x)- (x)
    #esta y la f de abajo se deben cambiar las 2

if __name__ == "__main__":
    # Pruebe aquí su función.
    #esta y la f de arriba se deben cambiar las 2

    f=lambda x: math.cos(x)-x
    
    b=float
    a=float    
    err= float
    rep= "s"
    while (rep =="s" or rep =="S"):
        print ("Algoritmo de bisección para aproximar las raices de una función.")
        print ("Ingrese los valores para los extremos A y B")
        print ("Ingrese valor de A: ")
        a= float (input ())
        print ("Igrese el valor de B")
        b= float (input ())
        fa=f(a)
        fb=f(b)
        while (fa*fb > 0):
            print ("Estos valores no están dentro de un cambio de signo, ingrese otros valores correctos:")
            print ("Valor de a")
            a= float (input ())
            print ("Valor de b")
            b= float (input ())
            fa=f(a)
            fb(b)
        print ("Ingrese el valor del error para d1etener el algoritmo")
        err=float (input ())
        while (err<0):
            print ("El error no puede ser menor a 0, ingrese un valor correcto.")
            err= float (input ())
        print ("¿Cuántas veces se va a iterar si no ha llegado al error?")
        n= float (input ())
        while (n< 1):
            print ("La cantidad de iteraciones no puede ser menor a 1, ingrese un valor correcto")
            n= input ()
        #print ("el punto medio más cercano a la raiz es: ",biseccion(a, b, err, n,0,0,0,0))
        print ("el punto medio más cercano a la raiz es: ",biseccion(f,a,b,err,n))
        print ("fin del algoritmo, desea repetir las operacones (n/s) ?")
        rep= input ()
        while (rep != "n" and rep != "s"):
            print ("Ingrese un valor correcto (n/s)")
            rep= input()
    print ("Bye.")
    chao=input()
    pass
