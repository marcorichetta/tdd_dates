from datetime import datetime, timedelta


def calcular_meses_entre_fechas(fecha_inicio: datetime, fecha_fin: datetime):

    delta: timedelta = fecha_fin - fecha_inicio

    # Si las fechas abarcan menos de un mes
    if delta.days > 28:
