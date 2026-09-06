from MetodoPago import MetodoPago

class PagoTransferenciaBancaria(MetodoPago):
    def procesar_pago(self, valor):
        return valor