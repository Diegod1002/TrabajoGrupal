##Ejercicio 1 

##Creamos un nodo

class Nodo:
    def __init__(self,key):
        self.valor=key
        self.derecha=None
        self.izquierda=None

def VerificarBST(raiz,der=None,izq=None):
    if (raiz==None):
        return True

    if (izq!=None and raiz.valor<= izq.valor):
        return False
    if (der!=None and raiz.valor>= der.valor):
        return False
    return VerificarBST(raiz.izquierda,izq,raiz) and VerificarBST(raiz.derecha,raiz,der)


if __name__ == '__main__':
    raiz=Nodo(5)
    raiz.derecha=Nodo(6)
    raiz.izquierda=Nodo(4)
    raiz.derecha.derecha=Nodo(7)
    raiz.izquierda.izquierda=Nodo(3)

    if (VerificarBST(raiz,None,None)):
        print("Si es un BST")
    else:
        print("No es BTS")    
