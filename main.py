from MetodoPago import Metodopago
from Compra import Compra
from Pago_billetera_digital import Pago_billetera_digital
from Pago_criptomonedas import Pago_criptomonedas
from Pago_tarjeta_credito import Pago_tarjeta_credito
from Pago_transferencia_bancaria import Pago_transferencia_bancaria

def main():
    
    purchase1 = Compra(25000, Pago_billetera_digital())
    purchase2 = Compra(25000, Pago_criptomonedas())
    purchase3 = Compra(25000, Pago_transferencia_bancaria())
    purchase4 = Compra(25000, Pago_tarjeta_credito())
    
    print(f"\nBilletera Digital: {purchase1.calcular_compra()}")
    print(f"\nCriptomonedas: {purchase2.calcular_compra()}")
    print(f"\nTransferencia Bancaria: {purchase3.calcular_compra()}")
    print(f"\nTarjeta de Crédito: {purchase4.calcular_compra()}")
    
main()