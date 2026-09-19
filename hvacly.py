"""Primitivas iniciais para validar eventos de telemetria HVACLY."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class TelemetryRecord:
    """Evento mínimo de telemetria associado a um sensor e ativo."""

    asset_id: str
    sensor_id: str
    quantity: str
    value: float
    unit: str
    measured_at: datetime


def validate_record(record: TelemetryRecord) -> None:
    """Valida invariantes obrigatórias de um registro de telemetria."""
    fields = {
        "asset_id": record.asset_id,
        "sensor_id": record.sensor_id,
        "quantity": record.quantity,
        "unit": record.unit,
    }
    for name, value in fields.items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name} must be a non-empty string")

    if not isinstance(record.value, (int, float)):
        raise TypeError("value must be numeric")
    if not isinstance(record.measured_at, datetime):
        raise TypeError("measured_at must be a datetime")
