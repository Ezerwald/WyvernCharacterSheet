class StatBlock:
    def __init__(self, value=8):
        self._value = value
        self._modifier = self._calculate_modifier()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if 1 <= new_value <= 20:  # Validate input value
            self._value = new_value
            self._modifier = self._calculate_modifier()  # Recalculate modifier

    @property
    def modifier(self):
        return self._modifier

    def _calculate_modifier(self):
        return (self._value - 10) // 2
