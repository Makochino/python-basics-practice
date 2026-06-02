import datetime

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
        return(f"[{status}] From: {self.sender} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        
class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email_list):
        for email in email_list:
            self.emails.append(email)

    def list_emails(self):
        if not self.emails:
            print("Inbox is empty.\n")
            return
        
        print("\nYour Emails: ")
        for i, email in enumerate(self.emails, start=1):
            print(f"{i}. {email}")
        return 

    def read_email(self, index):
        index -= 1
        if not self.emails:
            print("Inbox is empty.\n")
            return

        if index >= 0 and index < len(self.emails):
            self.emails[index].mark_as_read()  
            self.emails[index].display_full_email()      
        else:
            print(f"Index that your choised is out of range")
            return

    def delete_email(self, index):
        index -= 1
        if not self.emails:
            print("Inbox is empty.\n")
            return 
        
        if index >= 0 and index < len(self.emails):
            print(f"Email {self.emails[index]} was succefully deleted")
            self.emails.pop(index) 
        else:
            print(f"Index that your choised is out of range")
            return


class User():
    def __init__(self, name, inbox):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        return None
# User should create the Email object.

# Think in real life:

# John writes a letter
# ↓
# Letter is created
# ↓
# Letter is put into Mike's mailbox
    

#Email class checker
email_1 = Email("Dude", "Another-Dude", "How to say Hello to your dude", "Just say hey: what's up dude")
email_2 = Email("Duder", "Another-Duder", "How to say Hello to your duder", "Just say hey: what's up duder")
email_3 = Email("Dudler", "Another-Dudler", "How to say Hello to your dudler", "Just say: hey what's up dudler")


#Inbox class checker
inbox_1 = Inbox()
inbox_1.receive_email([email_1, email_2, email_3])
inbox.list_emails()


#User class checker


