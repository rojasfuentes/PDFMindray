import PySimpleGUI as sg

# Define el diseño de la ventana
layout = [
    [sg.Text('Seleccione un archivo PDF:')],
    [sg.InputText(key='-FILE-'), sg.FileBrowse(file_types=(("Archivos PDF", "*.pdf"),))],
    [sg.Button('Aceptar'), sg.Button('Cancelar')]
]

# Crea la ventana
window = sg.Window('Seleccionar archivo PDF', layout)

pdf_path = None  # Inicializa la variable pdf_path en None

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    elif event == 'Aceptar':
        pdf_path = values['-FILE-']
        if pdf_path:
            break

window.close()
