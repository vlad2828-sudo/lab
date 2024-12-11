class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("Метод має бути реалізований у підкласі")

# оплати кредитною карткою
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Оплата {amount} грн здійснена за допомогою кредитної картки.")

#оплати через PayPal
class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Оплата {amount} грн здійснена за допомогою PayPal.")

# оплати готівкою
class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Оплата {amount} грн здійснена готівкою.")

# Студентський код для використання системи оплати
class StudentPaymentSystem:
    def __init__(self, payment_method):
        self.payment_method = payment_method  # Передаємо обраний метод оплати

    def pay(self, amount):
        self.payment_method.process_payment(amount)

# Використання:
if __name__ == "__main__":
    payment_method = CreditCardPayment()  # Інші варіанти: PayPalPayment(), CashPayment()
    student_payment = StudentPaymentSystem(payment_method)

    # Оплата за навчання
    student_payment.pay(1000)
