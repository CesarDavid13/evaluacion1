#En este cprograma le pedimos al usario
#que teclee los coeficientes de un polinomio
#y hallamos el valor de las raices
import math
def ecuation ():
    print "introduzca los coeficientes de el polinomio"
    print "A*x*2+b*x+C=0"
    a=input ("A= ")
    b=input ("B= ")
    c=input ("C= ")
    radicando=b*b-4*a*c
    if (radicando>0):
        raiz1=(-b+math.sqrt(radicando))/(2*a)
        raiz2=(-b-math.sqrt(radicando))/(2*a)
        print "primera solucion = "
        print raiz1
        print "segunda solucion = "
        print raiz2
    else:
        print "esta ecuacion no tienen solucion"
ecuation ()
