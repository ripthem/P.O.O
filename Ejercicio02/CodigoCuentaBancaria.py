class CuentaBancaria:
    def __init__(self, titular, numeroCuenta, saldo):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo

    # Metodo para depositar
    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad

    # Metodo para retirar
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
            return cantidad
        else:
            return "Saldo insuficiente"

    # Metodo para consultar saldo
    def consultarSaldo(self):
        return self.saldo

    def mostrarInformacion(self):
        return f"{self.titular} tienes {self.saldo}"

#Crear cuenta
cuenta1 = CuentaBancaria("David Castro", "12345", 2000.0)
print(cuenta1.mostrarInformacion())
cuenta1.depositar(700.0)
print(cuenta1.mostrarInformacion())
print(cuenta1.retirar(500.0))
cuenta1.depositar(5000.0)
print(cuenta1.mostrarInformacion())
print(cuenta1.consultarSaldo())

cuenta2 = CuentaBancaria("Johana Aguilera", "54321", 5000.0)
print(cuenta2.mostrarInformacion())
cuenta2.depositar(200.0)
print(cuenta2.mostrarInformacion())
print(cuenta2.retirar(6000.0))
cuenta2.depositar(0.0)
print(cuenta2.mostrarInformacion())
print(cuenta2.consultarSaldo())
