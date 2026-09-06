from Compra import Compra
from PagoBilleteraDigital import PagoBilleteraDigital
from PagoCriptomonedas import PagoCriptomonedas
from PagoTarjetaCredito import PagoTarjetaCredito
from PagoTransferenciaBancaria import PagoTransferenciaBancaria

def main():
    purchase1 = Compra(25000, PagoBilleteraDigital())
    purchase2 = Compra(25000, PagoCriptomonedas())
    purchase3 = Compra(25000, PagoTransferenciaBancaria())
    purchase4 = Compra(25000, PagoTarjetaCredito())
    
    print(f"\nBilletera Digital: {purchase1.calcular_total()}")
    print(f"\nCriptomonedas: {purchase2.calcular_total()}")
    print(f"\nTransferencia Bancaria: {purchase3.calcular_total()}")
    print(f"\nTarjeta de Crédito: {purchase4.calcular_total()}")
    
main()