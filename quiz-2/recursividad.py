cadena = '312313L....:;;;A;;;;;1231231231231313131 RE13123123\n1313??????******C12312312312313\nU;;;;R???S23123\n12312312I.....V44515\n454%###I####DAD)))))))))))))\n((((((((((((((((((())))))\n))))))))))))) ES{}}}}}}} ,,,<<>>>>>>>G@@@@@E\n{{{{{{{{{{{{{{{NI}}}}}}}}}}}}}}}!!!!!!!$$$$$A......\n........................L!!!!'

def oculta(cad_actual, cad_oculta):
    if len(cad_actual) == 0:
        print(cad_oculta)
    else:
        letra_actual = cad_actual[0]
        if letra_actual.isalpha() or letra_actual.isspace():
            cad_oculta += letra_actual
        oculta(cad_actual[1:], cad_oculta)

oculta(cadena, '')
