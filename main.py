import os
import time

class Product:
    def __init__(self,nombre,materia_prima,mano_obra,costo_adicional):
        self.nombre = nombre
        self.materia_prima = materia_prima
        self.mano_obra = mano_obra
        self.costo_adicional = costo_adicional

    def getTotalUnity(materia_prima,mano_obra,costo_adicional):
        return materia_prima + mano_obra + costo_adicional
    
    def getTotalCantity(value, cantity):
        return value * cantity


title = """
------------------------------------------------------------------------------------------
|                                                                                        |
|                               #########################                                |
|                               #   Proyecto contable   #                                |
|                               #########################                                |
|                                                                                        |
|-Para usar el aplicativo deben colocar los decimales con punto "."                      |
|                                                                                        |
------------------------------------------------------------------------------------------
"""

msgUnity = """

| El costo de unidad del producto {} es de ${} |

"""

msgCantity = """

| El costo del producto {} por la cantidad {} es de ${} |

"""

msgEmptyData = """

---------------------------------------
|  Por favor ingresa todos los datos  |
---------------------------------------

"""

clear = lambda: os.system('cls')
    
def main():

    print(title)

    input("Presiona Enter para continuar\n")

    print("--------------------------------------------\n")
    name = input("Ingresa el nombre del producto: ")
    materia_prima = input("\nIngresa el costo de la materia prima: ")
    mano_obra = input("\nIngresa el costo de mano de obra: ")
    costo_adicional = input("\nIngresa los costos indirectos de fabricación: ")

    if name and materia_prima and mano_obra and costo_adicional:
        #Se crea el producto
        prd = Product(name,materia_prima,mano_obra,costo_adicional)
        #Se obtiene el total del valor de la unidad del producto
        total = Product.getTotalUnity(float(prd.materia_prima),float(prd.mano_obra),float(prd.costo_adicional))
        print(msgUnity.format(prd.nombre,round(total,2)))
        #Se pregunta por la cantidad de los productos a crear
        cantity = input("Ingresa la cantidad del producto a crear: ")
        if cantity:
            #Se obtiene el total
            totalCantity = Product.getTotalCantity(total,float(cantity))
            print(msgCantity.format(prd.nombre,cantity,str(totalCantity)))
        else:
            print("\nPor favor ingresa la cantidad de productos a crear")
            cantity = input("\nIngresa la cantidad del producto a crear: ")
            if cantity:
                totalCantity = Product.getTotalCantity(total,float(cantity))
                print(msgCantity.format(prd.nombre,cantity,str(totalCantity)))
            else:
                print(msgEmptyData)
                time.sleep(3.5)
                clear()
                main()
    else:
        print(msgEmptyData)
        time.sleep(3.5)
        clear()
        main()


if __name__ == '__main__':
    main()