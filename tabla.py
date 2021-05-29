class Table:
    """
    Este programa nos permite crear tablas descriptivas con datos y titulos principales.
    Para ello, debe contar con una lista de titulos, y otra lista de registros
    """
    def __init__(self):
        pass

    def ordenar(self, listaCabeza=[], lista=[]):
        valores = []
        lista = self.convertirString(lista)
        lista.insert(0, listaCabeza)
        cantidadCampos = len(lista[0])
        for ine in range(cantidadCampos):
            arreglo = []
            for i in range(len(lista)):
                for x in range(len(lista[i])):
                    if x == ine:
                        arreglo.append(lista[i][x])
            valores.append(arreglo)
        # devuelve los valores de cada campo como una fila para hallar el
        # maximo valor de una columna para realizar un formato
        # print( valores )
        longitudesValores = []
        for indice in range(len(valores)):
            longitud = []
            for i in range(len(valores[indice])):
                lgCampo = len(valores[indice][i])
                longitud.append(lgCampo)
            longitudesValores.append(longitud)
        # hasta aquí devuelve la longitud de cada campo en cada registro
        # print( longitudesValores )
        maximosCampos = []
        for indice in range(len(longitudesValores)):
            maximoCampo = self.obtenerMaximo(longitudesValores[indice])
            maximosCampos.append(maximoCampo)
        # aca devuelvo el maximo de cada campo para todos lso registros 
        # print( maximosCampos )
        respuesta = self.igualar(lista, maximosCampos)
        return respuesta
        # return self.mostrarTabla(respuesta)

    def obtenerMaximo(self, lista):
        maximo = max(lista, key=int)
        return maximo





    def convertirString(self, lista):
        nuevaLista = []
        for i in range(len(lista)):
            fila = lista[i]
            temp = []
            for x in range(len(fila)):
                tempCamp = str(fila[x])
                temp.append(tempCamp)
            nuevaLista.append(temp)
        return nuevaLista



    def igualar(self, lista=[], longitudes=[]):
        nuevaLista = []
        for indice in range(len(lista)):
            fila = lista[indice]
            filaNueva = []
            for i in range(len(fila)):
                maximoLg = longitudes[i]
                if len(fila[i]) < maximoLg:
                    diferencia = maximoLg - len(fila[i])
                    for x in range(diferencia):
                        fila[i] += " "
                filaNueva.append(fila[i])
            nuevaLista.append(filaNueva)
        return nuevaLista

    def formato(self, tamanoFuente=False, saltosLinea=1, espaciosDerecha=1, caracterSalto="\n", caracterEspacio=" "):
        self.tamanoFuente = tamanoFuente
        self.saltosLinea = saltosLinea
        self.espaciosDerecha = espaciosDerecha
        self.caracterSalto = caracterSalto
        self.caracterEspacio = caracterEspacio

    def fuenteTitulo(self):
        pass

    def darTamano(self, valor):
        if self.tamanoFuente == True:
            return f"{valor}".upper()
        else:
            return f"{valor}"

    def recorrer(self, cantidad, caracter=""):
        resultado = ""
        for indice in range(cantidad):
            resultado += caracter
        return resultado

    def obtenerTabla(self, lista, espacioDeLado=2, fuenteCabeza=False, caracter=" ", estilo="", estilizarCabeza=False, ambasPartes=False, lineaCabeza="–"):
        saltos = self.recorrer(self.saltosLinea, self.caracterSalto)
        espacio = self.recorrer(self.espaciosDerecha, self.caracterEspacio)
        espacioDeLadoderecho = self.recorrer(espacioDeLado, caracter)
        igualarEstilo = self.recorrer(len(estilo), " ")
        resultado = ""
        longitudParalinear = 0
        for indice in range(len(lista)):
            fila = lista[indice]
            filaDeTabla = f"{espacioDeLadoderecho}"
            for i in range(len(fila)):
                if indice != 0 and estilizarCabeza==False:
                    filaDeTabla += f"{estilo}{fila[i]}{espacio}"
                else:
                    if estilizarCabeza==False:
                        filaDeTabla += f"{fila[i]}{igualarEstilo}{espacio}"
                    else:
                        filaDeTabla += f"{estilo}{fila[i]}{espacio}"
            
            if indice == 0 and fuenteCabeza==False:
                filaDeTabla = f"{filaDeTabla}".title()
                longitudParalinear = len(filaDeTabla) - len(espacioDeLadoderecho)
                linea_estilo = self.recorrer(longitudParalinear, lineaCabeza)
                exclusivo = (len(espacioDeLadoderecho) - 2)
                renovarEspacio = self.recorrer(exclusivo, " ")
                if ambasPartes == False:
                    filaDeTabla += f"\n{renovarEspacio}{linea_estilo}{saltos}"
                else:
                    filaDeTabla = f"{renovarEspacio}{linea_estilo}\n{filaDeTabla}\n{renovarEspacio}{linea_estilo}{saltos}"
            elif indice == 0 and fuenteCabeza==True:
                filaDeTabla = f"{filaDeTabla}".upper()
                longitudParalinear = len(filaDeTabla) - len(espacioDeLadoderecho)
                linea_estilo = self.recorrer(longitudParalinear, lineaCabeza)
                exclusivo = (len(espacioDeLadoderecho) - 2)
                renovarEspacio = self.recorrer(exclusivo, " ")
                if ambasPartes == False:
                    filaDeTabla += f"\n{renovarEspacio}{linea_estilo}{saltos}"
                else:
                    filaDeTabla = f"{renovarEspacio}{linea_estilo}\n{filaDeTabla}\n{renovarEspacio}{linea_estilo}{saltos}"
            else:
                filaDeTabla += f"{saltos}"
                filaDeTabla = self.darTamano(filaDeTabla)
            resultado += filaDeTabla
        return resultado
        # devuelve el tamaño de fuente del resultado final
        # print( self.darTamano(resultado))


    def limpiar(self):
        from os import system
        system("cls")

    def mensajeVacio(self, mensaje="No se he encontrado ningun registro.", caracter=""):
        if caracter == "":
            caracter = "¯\_(ツ)_/¯"
        mensajeDev = f"\n\n\t{caracter} {mensaje}\n\n"
        print(mensajeDev)




