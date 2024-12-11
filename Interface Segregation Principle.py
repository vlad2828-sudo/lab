class Printer:
    def print_document(self, document):
        raise NotImplementedError

class Scanner:
    def scan_document(self):
        raise NotImplementedError

class Fax:
    def send_fax(self, document, number):
        raise NotImplementedError

# багатофункціональной пристрій
class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print_document(self, document):
        print(f"Друк: {document}")

    def scan_document(self):
        print("Сканування документа")

    def send_fax(self, document, number):
        print(f"Відправка факсу '{document}' на номер {number}")

# Клас простого принтера
class SimplePrinter(Printer):
    def print_document(self, document):
        print(f"Друк: {document}")

# сканера
class SimpleScanner(Scanner):
    def scan_document(self):
        print("Сканування документа")

if __name__ == "__main__":
    # Багатофункціональний пристрій
    mfp = MultiFunctionPrinter()
    mfp.print_document("Контракт")
    mfp.scan_document()
    mfp.send_fax("Контракт", "+380123456789")

    # Простий принтер
    printer = SimplePrinter()
    printer.print_document("Звіт")
