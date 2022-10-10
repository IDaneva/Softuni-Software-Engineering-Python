class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_inf0(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []
while True:
    information = input()
    if information == "Stop":
        break

    message_data = information.split(" ")
    sender = message_data[0]
    receiver = message_data[1]
    content = message_data[2]
    email = Email(sender, receiver, content)
    emails.append(email)

sent_emails = list(map(int, input().split(", ")))

for x in sent_emails:
    emails[x].send()

for email in emails:
    print(email.get_inf0())
