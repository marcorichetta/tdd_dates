from tdd_dates.app import calcular_meses_entre_fechas
from tdd_dates import __version__
from datetime import datetime


def test_calcular_meses_entre_fechas():
    """
    GIVEN Dos fechas d1 y d2
    WHEN Se llame al método calcular_meses_entre_fechas
    THEN
        Se obtiene una lista con 1 objeto por cada mes que abarquen las fechas
        Cada objeto contiene la fecha de inicio, fecha de fin y la cantidad de dias entre esas 2 fechas
    """

    fecha_inicio = datetime(2021, 2, 22)
    fecha_fin = datetime(2021, 3, 7)

    result = calcular_meses_entre_fechas(fecha_inicio, fecha_fin)

    expected = [
        {
            "fecha_inicio": datetime(2021, 2, 22),  # Fecha de inicio provista
            "fecha_fin": datetime(2021, 2, 28),  # Fecha de fin del mes
            "dias": 7,
        },
        {
            "fecha_inicio": datetime(2021, 3, 1),  # Fecha de inicio del mes
            "fecha_fin": datetime(2021, 3, 7),  # Fecha final provista
            "dias": 7,
        },
    ]

    assert result == expected


def test_version():
    assert __version__ == "0.1.0"
