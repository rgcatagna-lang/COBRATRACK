from datetime import date
from datetime import timedelta

from src.core.acuerdo_pago import AcuerdoPago

acuerdo = AcuerdoPago(
    100,
    250.50,
    date.today() + timedelta(days=15)
)

print(acuerdo.resumen())
