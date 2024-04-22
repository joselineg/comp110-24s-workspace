class Laptop:

    power: bool
    branding: str
    price: int
    size: str
    amount_of_ports: int

    def __init__(self, power_input, branding_input, price_input, size_input, amount_of_ports_input):
        self.power = power_input
        self.branding = branding_input
        self.price = price_input
        self.size = size_input
        self.amount_of_ports = amount_of_ports_input
    
    def type(self, list: str) -> str:
        return f"I type {list}."
    
    def power(self) -> str:
        if self.power:
            return "This laptop is on"
        else:
            return "This laptop is off"
        
lalolaptop: Laptop = Laptop(False, "Apple", 0, "Large", 9)

print(lalolaptop.type("balls"))
print(lalolaptop.power)