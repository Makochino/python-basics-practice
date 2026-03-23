class Printer:
    def work(self):
        return "Printing a document"

class Scanner:
    def work(self):
        return "Scanning a document"
    
def office_device(device):
    print(device.work())

office_device(Printer())
office_device(Scanner())