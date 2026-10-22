import streamlit  as st
import pdf
from funciones import aplicar_descuento, EFECTIVO, TRANSFERENCIA, calcular_iva, buscar_posicion

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
