from MetodoPago import MetodoPago

class PagoBilleteraDigital(MetodoPago):
      def procesar_pago(self, valor):
            descuento = valor * 0.02
            return valor - descuento