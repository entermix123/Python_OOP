class Integer:

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        # if not float_value.isinstance(float_value, float):    # can check float with isinstance() function
        #     return "value is not a float"
        if type(float_value) != float:
            return "value is not a float"
        # Integer.value = value // 1
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        # dictionary with possible rome values
        rom_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        int_value = 0   # sum of all values
        for k in range(len(value)):                         # iterate true len of values
            if k != 0 and rom_val[value[k]] > rom_val[value[k-1]]:     # check if next value is bigger than previous
                # if next value is bigger than previous, subtract 2 times the value of previous value
                int_value += rom_val[value[k]] - 2 * rom_val[value[k-1]]
            else:
                int_value += rom_val[value[k]]  # if next value is smaller than previous, add current value to sum

        return cls(int_value)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return "wrong type"
        return cls(int(value))
