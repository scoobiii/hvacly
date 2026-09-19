from datetime import datetime, timezone

import pytest

from hvacly import TelemetryRecord, validate_record


def valid_record(**overrides):
    values = {
        "asset_id": "asset-1",
        "sensor_id": "sensor-1",
        "quantity": "temperature",
        "value": 23.5,
        "unit": "degC",
        "measured_at": datetime.now(timezone.utc),
    }
    values.update(overrides)
    return TelemetryRecord(**values)


def test_valid_record_is_accepted():
    validate_record(valid_record())


@pytest.mark.parametrize("field", ["asset_id", "sensor_id", "quantity", "unit"])
def test_required_text_fields_must_not_be_empty(field):
    with pytest.raises(ValueError, match=field):
        validate_record(valid_record(**{field: "   "}))


def test_value_must_be_numeric():
    with pytest.raises(TypeError, match="value"):
        validate_record(valid_record(value="23.5"))


def test_measured_at_must_be_datetime():
    with pytest.raises(TypeError, match="measured_at"):
        validate_record(valid_record(measured_at="2026-01-01T00:00:00Z"))
