class Cliente:
    def __init__(self, nombre_completo, documento, telefono, mail):
        self.nombre_completo = nombre_completo
        self.documento = documento
        self.telefono = telefono
        self.mail = mail
        
    def __str__(self):
        return f" Nombre:{self.nombre_completo},\n Documento: {self.documento}\n Telefono: {self.telefono}\n Mail: {self.mail}"
    
    def pagar(self, modalidad_pago):
        self.modalidad_pago = modalidad_pago
        print(f"El cliente {self.nombre_completo} ha pagado con la siguiente modalidad: {self.modalidad_pago}")
    
    def comprar(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        print(f"El cliente {self.nombre_completo} ha comprado {self.cantidad} unidade(s) del producto {self.producto}")
