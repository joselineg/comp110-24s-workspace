class Phone:

    size: str
    price: int
    service: bool
    branding: str

    def __init__(self, size_input: str, price_input: int, service_input: bool, bradining_input: str):
        self.size = size_input
        self.price = price_input
        self.service = service_input
        self.branding = bradining_input
    
    def call(self, person: str) -> str:
        return f"I am calling {person}"

lalosphone: Phone = Phone("Large", 1000, True, "Apple")

jocsphone: Phone = Phone("Large", 1200, True, "Samsung")

print(jocsphone.call("Stuti"))

print(lalosphone.call("Zac"))