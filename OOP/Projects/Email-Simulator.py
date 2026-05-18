class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False
        self.timestamp = datetime.datetime.now()

    def mark_as_read(self):
        self.read = True

    def display_full_email(self):
        print(f"From: {self.sender}\nSent: {self.timestamp.strftime('%Y-%m-%d %H:%M')}\nTo: {self.receiver}\nSubject: {self.subject}\n\n{self.body}")
        return

    def __str__(self):
        status = "Read" if self.read else "Unread"
        print(f"[{status}] From: {self.sender} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        return
        
class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)

    def list_emails(self):
        if not self.emails:
            print("Inbox is empty.\n")
            return
        
        print("\nYour Emails:'")
        for i, email in enumerate(self.emails, start=1):
            print(f"{i}. {email}")
            return

    def read_email(self, index):
        if not self.emails:
            print("Inbox is empty.\n")
            return

        if index >= 0 and index < len(self.emails):
            self.emails[index].display_full_email()
            self.emails[index].mark_as_read()        
        else:
            print(f"Index that your choised is out of range")
            return

    