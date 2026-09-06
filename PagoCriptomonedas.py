from MetodoPago import MetodoPago

class PagoCriptomonedas(MetodoPago):
    def procesar_pago(self, valor):
        comision = valor * 0.10
        return comision + valor