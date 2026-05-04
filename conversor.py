import wx

# --- LÓGICA DE CONVERSIÓN (Clase de Negocio) ---
class LogicaConversora:
    """Clase que encapsula los cálculos de cambio de base."""
    
    def __init__(self):
        self.bases = {
            "Decimal": 10,
            "Binario": 2,
            "Hexadecimal": 16,
            "Octal": 8
        }

    def convertir(self, valor, base_origen, base_destino):
        try:
            # Primero convertimos todo a decimal (base 10)
            decimal = int(valor, self.bases[base_origen])
            
            # Luego convertimos del decimal a la base destino
            if base_destino == "Decimal":
                return str(decimal)
            elif base_destino == "Binario":
                return bin(decimal)[2:]
            elif base_destino == "Octal":
                return oct(decimal)[2:]
            elif base_destino == "Hexadecimal":
                return hex(decimal)[2:].upper()
        except ValueError:
            return "Error: Entrada no válida para la base seleccionada."

# --- INTERFAZ GRÁFICA (Clase de Vista) ---
class VentanaConversor(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Conversor de Bases Numéricas', size=(450, 350))
        self.logica = LogicaConversora()
        self.configurar_gui()
        self.Show()

    def configurar_gui(self):
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        opciones = ["Decimal", "Binario", "Hexadecimal", "Octal"]

        # Componentes
        self.txt_instruccion = wx.StaticText(panel, label="Valor a convertir:")
        self.input_valor = wx.TextCtrl(panel)

        self.txt_origen = wx.StaticText(panel, label="Base de origen:")
        self.combo_origen = wx.ComboBox(panel, choices=opciones, style=wx.CB_READONLY)
        self.combo_origen.SetSelection(0) # Decimal por defecto

        self.txt_destino = wx.StaticText(panel, label="Base de destino:")
        self.combo_destino = wx.ComboBox(panel, choices=opciones, style=wx.CB_READONLY)
        self.combo_destino.SetSelection(1) # Binario por defecto

        self.btn_convertir = wx.Button(panel, label="Convertir Ahora")
        self.lbl_resultado = wx.StaticText(panel, label="Resultado: ")
        
        # Fuente para que el resultado resalte
        fuente = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.lbl_resultado.SetFont(fuente)

        # Eventos
        self.btn_convertir.Bind(wx.EVT_BUTTON, self.al_convertir)

        # Layout
        elementos = [self.txt_instruccion, self.input_valor, self.txt_origen, 
                     self.combo_origen, self.txt_destino, self.combo_destino, 
                     self.btn_convertir, self.lbl_resultado]
        
        for el in elementos:
            sizer.Add(el, 0, wx.ALL | wx.EXPAND, 8)

        panel.SetSizer(sizer)

    def al_convertir(self, event):
        valor = self.input_valor.GetValue()
        b_origen = self.combo_origen.GetValue()
        b_destino = self.combo_destino.GetValue()

        resultado = self.logica.convertir(valor, b_origen, b_destino)
        self.lbl_resultado.SetLabel(f"Resultado: {resultado}")

if __name__ == '__main__':
    app = wx.App()
    VentanaConversor()
    app.MainLoop()
