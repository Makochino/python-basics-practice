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

    def receive_email(self, email_s):
        if isinstance(email_s, list):    
            for email in email_s:
                self.emails.append(email)
        else:
            self.emails.append(email_s)

    def list_emails(self):
        if not self.emails:
            print("Inbox is empty.\n")
            return
        
        print("\nYour Emails: ")
        for i, email in enumerate(self.emails, start=1):
            print(f"{i}. {email}")
        return 

    def mark_as_read(self, index):
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

    def del_email(self, index):
        index -= 1
        if not self.emails:
            print("Inbox is empty.\n")
            return 
        
        if index >= 0 and index < len(self.emails):
            print(f"\nEmail {self.emails[index]} was succesfully deleted")
            self.emails.pop(index) 
        else:
            print(f"Index that your choised is out of range")
            return


class User():
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(self.name, receiver.name, subject, body)
        receiver.inbox.receive_email(email)

    def check_inbox(self):
        return self.inbox.list_emails()
        
    def mark_as_read(self, index):
        return self.inbox.mark_as_read(index)
        
    def del_email(self, index):
        return self.inbox.del_email(index)
       

if __name__ == "__main__":
    
    #User class checker
    user_1 = User("Dio Brando")
    receiver_1 = User("Jonathan Joester")

    user_1.send_email(receiver_1, "Personal question for the motherfucker", "How do you still alive?")
    user_1.send_email(receiver_1, "Just a quick reminder", "How does it feel to be beaten by the schoolboy?")
    receiver_1.mark_as_read(1)
    receiver_1.check_inbox()
    receiver_1.del_email(1)
    receiver_1.check_inbox()

