class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = self._validate(hour, 23)
        self.minute = self._validate(minute, 59)
        self.second = self._validate(second, 59)

    def _validate(self, value, max_val):
        if isinstance(value, int) and 0 <= value <= max_val:
            return value
        return 0

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def is_after(self, other):
        return (self.hour, self.minute, self.second) > (other.hour, other.minute, other.second)

    def __add__(self, other):
        total_seconds = self.second + other.second
        extra_minutes, second = divmod(total_seconds, 60)

        total_minutes = self.minute + other.minute + extra_minutes
        extra_hours, minute = divmod(total_minutes, 60)

        hour = (self.hour + other.hour + extra_hours) % 24

        return Time(hour, minute, second)


