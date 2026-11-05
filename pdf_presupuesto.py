import io
from fpdf import FPDF


def limpiar(texto):
  """Receta V3 (Parte 7): Deja solo las letras que Helvetica sabe dibujar (ñ y acentos sí; emojis y caracteres raros no)."""
  return texto.encode("latin-1", "ignore").decode("latin-1").strip()


def armar_pdf(
    cliente, productos, subtotal, descuento, base, iva, total, forma_pago
):
  """Genera el archivo PDF con la estructura del presupuesto."""
  pdf = FPDF(format="A4", unit="mm")
  pdf.add_page()

  pdf.set_font("Helvetica", "B", 16)
  pdf.cell(0, 10, "PRESUPUESTO DE COMPRA", ln=True, align="C")

  pdf.set_font("Helvetica", "", 11)
  pdf.cell(0, 8, f"Cliente: {cliente}", ln=True)
  pdf.cell(0, 8, f"Forma de Pago: {forma_pago}", ln=True)
  pdf.ln(5)

  pdf.set_font("Helvetica", "B", 10)
  pdf.cell(80, 8, "Producto", border=1)
  pdf.cell(25, 8, "Cant.", border=1, align="C")
  pdf.cell(40, 8, "Precio U.", border=1, align="R")
  pdf.cell(45, 8, "Subtotal", border=1, align="R")
  pdf.ln()

  pdf.set_font("Helvetica", "", 10)
  for p in productos:
    nombre_limpio = limpiar(p["nombre"])
    pdf.cell(80, 8, nombre_limpio, border=1)
    pdf.cell(25, 8, str(p["cantidad"]), border=1, align="C")
    pdf.cell(40, 8, f"${p['precio_unitario']:.2f}", border=1, align="R")
    pdf.cell(45, 8, f"${p['subtotal']:.2f}", border=1, align="R")
    pdf.ln()

  pdf.ln(5)

  pdf.set_font("Helvetica", "", 10)
  pdf.cell(145, 6, "Subtotal:", align="R")
  pdf.cell(45, 6, f"${subtotal:.2f}", align="R", ln=True)

  pdf.cell(145, 6, "Descuento:", align="R")
  pdf.cell(45, 6, f"-${descuento:.2f}", align="R", ln=True)

  pdf.cell(145, 6, "Base Imponible:", align="R")
  pdf.cell(45, 6, f"${base:.2f}", align="R", ln=True)

  pdf.cell(145, 6, "IVA (21%):", align="R")
  pdf.cell(45, 6, f"${iva:.2f}", align="R", ln=True)

  pdf.set_font("Helvetica", "B", 12)
  pdf.cell(145, 8, "TOTAL:", align="R")
  pdf.cell(45, 8, f"${total:.2f}", align="R", ln=True)

  return bytes(pdf.output())