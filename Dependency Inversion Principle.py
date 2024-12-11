class MessageSender:
    def send(self, message):
        raise NotImplementedError

# Низькорівневі модулі
class EmailSender(MessageSender):
    def send(self, message):
        print(f"Відправка email: {message}")

class SmsSender(MessageSender):
    def send(self, message):
        print(f"Відправка SMS: {message}")

# Високорівневий модуль
class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)


if __name__ == "__main__":
    email_service = NotificationService(EmailSender())
    sms_service = NotificationService(SmsSender())

    email_service.notify("Ваше замовлення підтверджено.")
    sms_service.notify("Ваше замовлення буде доставлено завтра.")
