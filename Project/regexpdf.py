from extractpdf import pdf_text
import re

# Expresiones regulares
expresion_cantidad = r'\d+\.\d{3}'
expresion_producto = r'\d{3}\-\d{6}\-\d{2}'
expresion_lote = r'\d{10}[\w.]*'
expresion_nota = r'Nota de entrega:\s+(\w+)'

cantidad_list = re.findall(expresion_cantidad, pdf_text)
producto_list = re.findall(expresion_producto, pdf_text)
lote_list = re.findall(expresion_lote, pdf_text)
nota_entrega = re.search(expresion_nota, pdf_text)

nota_entrega = nota_entrega.group(1)

cantidad_list2 = [numero.split('.')[0] for numero in cantidad_list]