import streamlit as st

st.title("kioscardovich de papuleon")

cliente=st.text_input("ingrese su nombre:")
precioAlfajor=1500
cantidadA = st.number_input("Ingrese Cantidad de Alfajores que quiere comprar:", 0, step=1)
totalA=cantidadA*precioAlfajor
precioGaseosa= 2800
cantidadG = st.number_input("Ingrese Cantidad de Gaseosas que quiere comprar:", 0, step=1)
totalG=cantidadG*precioGaseosa
total=totalA+totalG
st.write(f"{cliente} tu total a pagar es ${total}")