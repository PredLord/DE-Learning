# 03 Seconds into hours, minutes, seconds Easy • ~8 min
# Write `format_duration(seconds)` for non-negative integer seconds. Return a string formatted
# `HH:MM:SS`, with at least two digits per part. Hours may exceed 99.
# SAMPLE INPUT / OUTPUT
# format_duration(3661) -> '01:01:01'
# format_duration(61) -> '00:01:01'
def format_duration(seconds):
    hour = seconds // 3600
    minute = (seconds % 3600) // 60
    second = seconds % 60
    return f"{hour:02d}:{minute:02d}:{second:02d}"


print(format_duration(5000))

