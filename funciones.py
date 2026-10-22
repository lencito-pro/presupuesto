
EFECTIVO = "Efectivo"
TRANSFERENCIA = "Transferencia"


def buscar_posicion(lista, nombre):
    """Busca la posicion de un elemento en una lista."""
    for i in range(len(lista)):
        if lista[i] == nombre:
            return i
    return -1


def aplicar_descuento(monto, pago):
    """Aplica un 10% de descuento si el pago es en efectivo."""
    if pago == EFECTIVO:
        monto = monto - (monto * 10 / 100)
    return round(monto, 2)


def calcular_iva(monto):
    """Calcula el 21% de IVA sobre un monto."""
    return round(monto * 21 / 100, 2)

