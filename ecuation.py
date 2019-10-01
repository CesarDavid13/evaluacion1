#En este cprograma le pedimos al usario
#que teclee los coeficientes de un polinomio
#y hallamos el valor de las raices
def ecuation ():
    print "introduzca los coeficientes de el polinomio"
    print "A*x*2+b*x+C=0"
    a=input ("A= ")
    b=input ("B= ")
    c=input ("C= ")
    raiz1=(-b+(b*b-4*a*c)^(1/2))/(2*a)
    raiz2=(-b-(b*b-4*a*c)^(1/2))/(2*a)
    print "primera solucion = "
    print raiz1
    print "segunda solucion = "
    print raiz2
ecuation ()
