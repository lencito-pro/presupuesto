
st.set_page_config(
    page_title="Calculadora de Presupuestos", layout="centered"
)

st.title(" Calculadora de Presupuestos")
st.write(
    "Seleccioná los productos, cantidad y forma de pago para generar tu"
    " presupuesto en PDF."
)

st.divider()

PRODUCTOS = {
    "Gaseosa 1.5L": 2800.0,
    "Alfajor Triple": 1500.0,
    "Galletitas Paquete": 1200.0,
    "Agua Mineral 500ml": 1000.0,
    "Sandwich de Miga": 2200.0,
    "Chocolatina": 800.0,
}

st.subheader("1. Selección de Productos")
st.caption(
    "Podés elegir hasta 4 productos distintos para armar la lista de compra:"
)

productos_seleccionados = []

for i in range(1, 5):
  col1, col2 = st.columns([3, 1])
  with col1:
    prod = st.selectbox(
        f"Producto {i}:",
        options=["-- Ninguno --"] + list(PRODUCTOS.keys()),
        key=f"prod_{i}",
    )
  with col2:
    cant = st.number_input(
        "Cantidad:",
        min_value=1,
        max_value=100,
        value=1,
        step=1,
        key=f"cant_{i}",
    )

  if prod != "-- Ninguno --":
    precio_u = PRODUCTOS[prod]
    subtotal_item = precio_u * cant
    productos_seleccionados.append({
        "nombre": prod,
        "cantidad": cant,
        "precio_unitario": precio_u,
        "subtotal": subtotal_item,
    })

st.divider()

st.subheader("2. Forma de Pago")
forma_pago = st.radio(
    "Seleccioná cómo abonás:",
    options=[
        "Efectivo (10% descuento)",
        "Tarjeta / Mercado Pago (Sin descuento)",
    ],
    index=0,
)

es_efectivo = "Efectivo" in forma_pago

subtotal = sum(p["subtotal"] for p in productos_seleccionados)
descuento = (subtotal * 0.10) if es_efectivo else 0.0
base = subtotal - descuento
iva = base * 0.21
total = base + iva

st.divider()
st.subheader("3. Resumen del Presupuesto")

if productos_seleccionados:
  st.table([{
      "Producto": p["nombre"],
      "Cant.": p["cantidad"],
      "Precio U.": f"${p['precio_unitario']:.2f}",
      "Subtotal": f"${p['subtotal']:.2f}",
  } for p in productos_seleccionados])

  col_res1, col_res2 = st.columns(2)
  with col_res1:
    st.write(f"**Subtotal:** ${subtotal:.2f}")
    st.write(f"**Descuento:** -${descuento:.2f}")
    st.write(f"**Base Imponible:** ${base:.2f}")
  with col_res2:
    st.write(f"**IVA (21%):** ${iva:.2f}")
    st.markdown(f"### **TOTAL: ${total:.2f}**")
else:
    st.info("Elegí al menos un producto arriba para ver las cuentas.")

st.divider()

st.subheader("4. Emisión de Comprobante")

cliente_input = st.text_input("Nombre del Cliente:", placeholder="Ej: Julián")
cliente = limpiar(cliente_input)

if not productos_seleccionados:
  st.warning("Seleccioná al menos un producto para generar el documento.")
elif cliente == "":
  st.warning("Escribí el nombre del cliente para armar el presupuesto")
else:
  pdf_bytes = armar_pdf(
      cliente,
      productos_seleccionados,
      subtotal,
      descuento,
      base,
      iva,
      total,
      forma_pago,
  )

  st.download_button(
      label=" Descargar PDF del Presupuesto",
      data=pdf_bytes,
      file_name=f"presupuesto_{cliente.replace(' ', '_')}.pdf",
      mime="application/pdf",
  )
