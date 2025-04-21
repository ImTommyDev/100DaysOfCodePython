class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.validado = False 

    def validate(self):
        if self.age >= 18:
            self.validado = True
        else:
            self.validado = False

    def __str__(self):
        return f"User(name={self.name}, age={self.age}, validado={self.validado})"


user1 = User("JohnDoe", 30)
user1.validate()

print(user1)