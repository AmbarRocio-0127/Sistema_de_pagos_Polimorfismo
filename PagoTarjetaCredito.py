from MetodoPago import MetodoPago

class PagoTarjetaCredito(MetodoPago):
    def procesar_pago(self, valor):
        comision = valor * 0.05
        return comision + valor