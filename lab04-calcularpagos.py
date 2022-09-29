def calcularpago(horas, tarifa)
MAX_HORAS_SEMANALES = 40
horas_extras = 0
if(horas> MAX_HORAS_SEMANALES):
    horas_extra = horas - MAX_HORAS_SEMANALES
    horas = MAX_HORAS_SEMANALES
    calculo = (horas * tarifa) + (horas_extra * tarifa * 1.5)
    else:
        calculo = horas *tarifa
        return calculo

    try:
        horas = int(input("Ingrese numero de horas: "))
        tarifa = int(input("ingrese tarifa: "))
        pago = calcularpago(horas,tarifa)
        print(pago)
    except:
        print8("Error, debe ingresar un valor numerico") 
        