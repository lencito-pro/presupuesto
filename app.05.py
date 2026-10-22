import streamlit  as st

from fpdf import FPDF


def armar_pdf(cliente, total):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica","B",20)
    pdf.cell(0, 12, "kioscardovitch megapro", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica","",12)
    pdf.cell(0,9,f"cliente: {cliente}",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0,9,f"cliente: ${total:.2f}",new_x="LMARGIN", new_y="NEXT")
    return bytes (pdf.output())
    

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


st.title("Kioscaso de los PAPUS")

cliente= st.text_input("¿Cómo te llamas?: ")
fecha=st.date_input("Fecha")
numero=st.number_input("numero de presupuesto", min_value=1, step=1,  value=101)
producto= "Alfajor"
precio=1600
cantidad = st.number_input("Cantidad:", min_value=1, step=1)
forma_pago = st.radio("Forma de pago:", [EFECTIVO, TRANSFERENCIA])
subtotal=precio*cantidad
descuento= aplicar_descuento(subtotal, forma_pago)
iva=calcular_iva(descuento)
total=round(descuento + iva, 2)

import presupuesto_pdf       
archivo = presupuesto_pdf.armar_pdf(numero, fecha, cliente, producto, cantidad, precio, subtotal,descuento, iva, total)
 
st.download_button("Descargar presupuesto (PDF)", archivo,
                   file_name=f"presupuesto_{numero}.pdf", mime="application/pdf")
