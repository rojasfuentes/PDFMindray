from regexpdf import producto_list, nota_entrega, lote_list, cantidad_list2
import pandas as pd

# Crea un diccionario con los datos
data = {
    'Id. Pedido Cliente': nota_entrega, 
    'Delivery': nota_entrega,
    'Codigo Producto': producto_list,
    'Lote': lote_list,
    'Caducidad (AAAAMMDD)': ["" for _ in range(len(producto_list))],
    'Cantidad': cantidad_list2
}

df = pd.DataFrame(data)
#print(df)

ruta_archivo_excel = r'C:\Users\JFROJAS\Desktop\PDFMindray\Docs\resultado.xlsx'
df.to_excel(ruta_archivo_excel, index=False, engine='openpyxl')

print(f"El DataFrame se ha guardado en '{ruta_archivo_excel}'")