
# Single responsibility
# class User:
#
#     def __init__(self, username: str, email: str, password: str):
#         self.username = username
#         self.email = email
#         self.password = password
#
#     def get_username(self) -> str:
#         return self.username
#
#     def get_email(self) -> str:
#         return self.email
#
#     def authenticate(self, password):
#         if password == self.password:
#             return True
#         else:
#             return False
#
#
# spas = User('Spas', 'spas@gmail.com', 'password12')
# print(spas.authenticate('SuperSpas'))
#

# # Open/Close Example: Open for execution, close for modification of the existing code
#
# from abc import ABC, abstractmethod
#
#
# class PaymentMethod(ABC):       # base abstract class
#
#     @abstractmethod             # abstract method mandatory for inherited classes
#     def process_payment(self, amount):
#         pass
#
#
# class PayPalPayment(PaymentMethod):     # class for PayPal payments inherited from PaymentMethod class
#
#     def process_payment(self, amount):  # mandatory method from PaymentMethod class
#         print(amount)
#
#
# class CreditCardPayment(PaymentMethod):  # class for credit card payments inherited from PaymentMethod class
#     def process_payment(self, amount):  # mandatory method from PaymentMethod class
#         print(amount)
#
#
# class BankTransferPayment(PaymentMethod):  # class for credit card payments inherited from PaymentMethod class
#
#     def process_payment(self, amount):  # mandatory method from PaymentMethod class
#         print(amount)
#
#
# class PaymentProcessor:                 # class for processing payments, not inherited
#     def __init__(self, payment_method):     # require payment method in initialization
#         self.payment_method = payment_method
#
#     def process_payment(self, amount):              # same method from PaymentMethod class but not mandatory
#         self.payment_method.process_payment(amount)
#         # uses process_payment method from type payment classes: CreditCardPayment, PayPalPayment and BankTransferPayment
#         # we can extend payment methods without changing the class PaymentProcessor - main advantage
#
#
# bank_transfer_payment = BankTransferPayment()
# processor = PaymentProcessor(bank_transfer_payment)
# processor.process_payment(1000)     # 1000

# # Open/Close Example: Open for execution, close for modification of the existing code
# class StudentTaxes:             # class created first for discount calculations
#     def __init__(self, name, semester_tax, avg_grade):
#         self.name = name
#         self.semester_tax = semester_tax
#         self.average_grade = avg_grade
#
#     def get_discount(self):
#         if self.average_grade > 5:
#             return self.semester_tax * 0.4
#
#
# # class created after decision for additional discount that do not change the class StudentTaxes, but add functionality
# class AdditionalDiscount(StudentTaxes):  # created class to add discount for students with average grade between 4 and 5
#     def get_discount(self):
#         result = super().get_discount()     # inherit get_discount function from StudentTaxes class and use it
#         if result:
#             return result
#         if 4 < self.average_grade <= 5:
#             return self.semester_tax * 0.2


# # Liskov Substitution Example:
# # Instances form inherit class can be used in parent class with no errors
# # instance of class Square can be used in class Rectangle
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Square(Rectangle):        # inherit Rectangle class
#
#     def __init__(self, side):
#         super().__init__(side, side)
#         self.side = side
#
#     def area(self):             # same as area function from Rectangle class
#         return self.side * self.side
#
#
# def print_are(rectangle):       # additional function to print area for Rectangle class or Square class
#     print(rectangle.area())
#
#
# # def print_are(square):        # additional function to print area for Rectangle class or Square class
# #     print(square.area())      # works
#
# r = Rectangle(10, 20)
# s = Square(10)
#
# print_are(r)
# print_are(s)

# # Interface Segregation Example:
# from abc import ABC, abstractmethod
#
#
# class Printable(ABC):       # base abstract class Printable
#
#     @abstractmethod
#     def print(self, document):
#         pass
#
#
# class Scannable(ABC):       # base abstract class scannable
#
#     @abstractmethod
#     def scan(self, document):
#         pass
#
#
# class Faxable(ABC):     # base abstract class faxable
#
#     @abstractmethod
#     def fax(self, document):
#         pass
#
#
# class MultifunctionPrinter(Printable, Scannable, Faxable):      # inherit from Printable, Scannable and Faxable
#
#     def print(self, document):      # use print function from Printable class
#         pass
#
#     def scan(self, document):       # use scan function from Scannable class
#         pass
#
#     def fax(self, document):        # use fax function from Faxable class
#         pass
#
#
# class SimplePrinter(Printable):     # inherit from Printable class only
#     # use print function from Printable class only and not forced to use other abstract class methods
#     def print(self, document):  # the client is not forced to use other abstract class methods
#         pass

# # Dependency Inversion Example
# from abc import ABC, abstractmethod
#
#
# # abstract base class. That remove dependency of class Application form class Database
# # This allow us more flexibility in our application
# class DatabaseInterface(ABC):
#
#     @abstractmethod
#     def save(self, data):
#         pass
#
#
# class Database(DatabaseInterface):
#
#     def save(self, data):
#         pass
#
#
# class Application:
#
#     def __init__(self, database):       # depends on database which is violation of dependency inversion principle
#         self.database = database
#
#     def run(self):
#         data = self.fetch_data()
#         self.database.save(data)
#
#     def fetch_data(self):
#         pass

#
