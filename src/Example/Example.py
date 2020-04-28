class Example:
    def __init__(self, string, number):
        self.string = string
        self.number = number

    def returnConcatenatedProperties(self):
        return f"{self.string} {self.number}"
