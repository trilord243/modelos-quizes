def input_numerico(mensaje, mensaje_err="Ingrese un numero valido"):
    validacion = True
    while validacion:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print(mensaje_err)




