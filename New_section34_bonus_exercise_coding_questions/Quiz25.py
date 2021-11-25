# OOPS

"""
Output?

"""


class Computer:

    def __init__(self, model, memory, processor):
        self.memory = memory
        self.processor = processor

    def price(self):
        return (self.memory * self.processor) / 10


macbook = Computer('Macbook Pro 15" 2016', 16, 2400)
print(macbook.price())
