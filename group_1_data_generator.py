import random
import matplotlib.pyplot as plt


class TemperatureDataGenerator:
    def __init__(self, base=0, delta=0.15, mean=0, std_dev=5.0, uniform_min=-2, uniform_max=2):
        """
        Initialize the temperature data generator with default values.
        """
        self.base = base
        self.delta = delta
        self.mean = mean
        self.std_dev = std_dev
        self.uniform_min = uniform_min
        self.uniform_max = uniform_max
        self.current = base  # Tracks the current temperature

    def __generate_normalized_value(self):
        """Generate a random value between 0 and 1."""
        return random.random()

    @property
    def random_value(self):
        """Generate a scaled random value in the range [-5, 5]."""
        x_min = -5
        x_max = 5
        m = x_max - x_min
        c = x_min
        x = self.__generate_normalized_value()
        y = m * x + c
        return y

    def generator_1(self):
        """Generate a constant value."""
        return 0

    def generator_2(self):
        """Small squiggles using uniform distribution."""
        return random.randint(self.uniform_min, self.uniform_max)

    def generator_3(self):
        """Simulate real-world temperature noise (Gaussian)."""
        return random.gauss(self.mean, self.std_dev)

    def generator_4(self, increment=True):
        """Simulate gradual increase/decrease over time."""
        if increment:
            self.current += self.delta
        else:
            self.current -= self.delta
        return self.current

    def generate_data(self, num_points=500):
        """Generate a sequence of temperature data points."""
        data = []
        for i in range(num_points):
            value = self.generator_1()
            value += self.generator_4((i % 50) > 24)
            value += self.generator_3()
            value += self.generator_2() / 20.0
            value += self.random_value
            value = max(-40, min(40, value))
            data.append(value)
        return data


# Wrapper class to be used in Labs 7 & 8
class TemperatureSensor(TemperatureDataGenerator):
    def __init__(self):
        super().__init__()

    def get_temperature(self):
        return self.generator_3()  # This can be changed to generator_4() or custom logic
