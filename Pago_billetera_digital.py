from MetodoPago import Metodopago

class Pago_billetera_digital(Metodopago):
      def procesar_pago(self, value):
            comision = value * 0.2
            return comision + value