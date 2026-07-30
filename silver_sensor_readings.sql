SELECT
    device_id,
    temperature,
    humidity,
    aqi,
    timestamp
FROM sensor_readings
WHERE temperature IS NOT NULL;