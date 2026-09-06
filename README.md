# Lecciones aprendidas: Nomenclatura y buenas prácticas en Python (POO)

> Notas basadas en la corrección iterativa del ejercicio "Sistema de pagos" (polimorfismo). Documenta los puntos donde hubo debilidad para tenerlos presentes en próximos ejercicios.

---

## 1. Convención de nombres de clases: PascalCase

**Regla:** en Python, los nombres de clase se escriben en `PascalCase` (también llamado `CapWords`): cada palabra empieza con mayúscula y **sin guiones bajos** entre ellas.

| Correcto (PascalCase) | Incorrecto |
|---|---|
| `MetodoPago` | `Metodopago` |
| `PagoTarjetaCredito` | `Pago_tarjeta_credito` |
| `PagoBilleteraDigital` | `Pago_Billetera_Digital` |
| `PagoCriptomonedas` | `pago_criptomonedas` |

**Por qué importa:** no es solo estética. Es la convención oficial de Python (PEP 8) y la que espera cualquier persona que lea tu código, un linter, o un profesor/revisor. Mezclar `snake_case` con mayúsculas parciales (`Pago_Billetera_Digital`) es un híbrido que no sigue ninguna convención reconocida.

**Regla rápida para diferenciar:**
- **Clases** → `PascalCase` → `MetodoPago`, `Cliente`, `Compra`
- **Variables, atributos, métodos, funciones** → `snake_case` → `calcular_total`, `metodo_pago`, `valor`

---

## 2. Consistencia entre español e inglés

**El problema detectado:** mezclar idiomas dentro del mismo proyecto. Por ejemplo:

```python
# Inconsistente: value en inglés, metodopago sin separar palabras
def __init__(self, value, metodopago: MetodoPago):
    self.value = value
    self.metodopago = metodopago
```

**Regla general:** si el dominio del problema está en español (nombres de clases, del enunciado, de los métodos), **todo el proyecto debe mantenerse en español** — variables, parámetros, atributos y comentarios incluidos. No hay una regla universal de "usa inglés siempre" en la industria; lo que sí es un estándar innegociable es la **consistencia**: no mezclar `value` con `valor`, ni `metodopago` con `metodo_pago` en el mismo proyecto.

| Inconsistente | Consistente (español) |
|---|---|
| `self.value = valor` | `self.valor = valor` |
| `metodopago` | `metodo_pago` |
| `def procesar_pago(self, comision)` cuando recibe un valor | `def procesar_pago(self, valor)` |

**Nota sobre nombres de parámetros:** el nombre de un parámetro debe describir **lo que realmente recibe**, no lo que la clase hija hace con él. `MetodoPago.procesar_pago(self, comision)` fue un error conceptual porque el método padre no recibe una comisión — recibe el valor de la compra; la comisión es algo que cada subclase *calcula* internamente.

---

## 3. Verificar la ejecución antes de entregar

**El error más grave detectado en el proceso:** al renombrar un parámetro (`value` → `valor`) se actualizó el `__init__` pero no el método que lo usaba, dejando referencias a un atributo que ya no existía:

```python
def __init__(self, valor, metodopago: MetodoPago):
    self.value = valor              # se guarda en self.value
    ...
def calcular_total(self):
    return self.metodopago.procesar_pago(self.valor)   # busca self.valor -> no existe
```

Esto provoca un `AttributeError` en tiempo de ejecución — el programa ni siquiera corre.

**Regla de oro:** después de cualquier cambio de nombre (variable, atributo, parámetro), ejecuta el archivo (`python main.py`) antes de dar la corrección por terminada. Un error de este tipo se detecta en segundos corriendo el código, pero puede pasar desapercibido en una simple lectura visual.

---

## 4. Verificar la lógica contra los ejemplos numéricos del enunciado

**El error repetido varias veces:** un descuento del 2% escrito como `valor * 0.2` (20%) en lugar de `valor * 0.02` (2%). El signo de la operación (resta vs. suma) se corrigió antes que el porcentaje, y el error de magnitud pasó desapercibido en más de una entrega.

**Regla de oro:** cuando el enunciado da un ejemplo numérico (ej. "compra 100000 → total 98000"), **corre ese caso concreto mentalmente o en el intérprete** antes de dar por buena una corrección. Si el número no coincide exactamente, hay un error — no importa que "se vea" conceptualmente correcto.

```python
# Prueba rápida antes de entregar:
# compra = 100000 → esperado 98000 (descuento del 2%)
print(PagoBilleteraDigital().procesar_pago(100000))  # ¿da 98000.0?
```

---

## 5. Resumen de checklist antes de entregar un ejercicio de POO

- [ ] ¿Los nombres de clase están en `PascalCase`, sin guiones bajos?
- [ ] ¿Los nombres de variables, atributos y métodos están en `snake_case`?
- [ ] ¿Todo el proyecto usa el mismo idioma de forma consistente?
- [ ] ¿Los nombres de los métodos coinciden exactamente con los que pide el enunciado?
- [ ] ¿Corriste el archivo principal (`python main.py`) sin errores?
- [ ] ¿Verificaste los resultados contra los ejemplos numéricos exactos del enunciado?
- [ ] ¿Cada clase hija sobrescribe correctamente el método de la clase padre (sin cambiar su firma de forma incompatible)?
