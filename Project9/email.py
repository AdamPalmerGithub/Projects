'''A program auto generates emails, lists the subject lines and allows the user to choose and read the emails and changing them to read, view unread emails or quit the program '''


inbox = []        #Empty list to store emails


class Email():             #email class

    has_been_read = False     #initially sets read status to unread
    is_spam = False           #initially sets spam status to not

    def __init__(self, email_address, subject_line, email_contents):    #combnes the 3 parts into 1 item

        self.email_address = email_address
        self.subject_line = subject_line
        self.email_contents = email_contents
    
    def read_status(self):                                #when called returns a read status depending on true or false
        if self.has_been_read == False:
            return self.email_address + " is unread"
        else:
            return self.email_address + " is read"
        
    def spam_status(self):                                  #when called returns a spam status
        if self.is_spam == False:
            return "isn't spam"
        else:
            return "is spam"
        
    def mark_as_read(self):                     #when called changes value to true
        self.has_been_read = True    

    def mark_as_spam(self):
        self.is_spam = True

def delete_email(x):         #function to delete an email
    inbox.pop(x)

def populate_inbox():
    inbox.append(Email("breaking.news@email.com", "Breaking news", "Local gran stops armed robbery."))            #adds fake email items to inbox list
    inbox.append(Email("scammy.scam@email.com", "YOU'RE A WINNER!", "You've been selected to win a new car!!"))
    inbox.append(Email("boss.work@email.com", "Coffee run", "Where's my coffee, do you not value this job?"))
    return inbox

populate_inbox()   #call function

def list_emails():
    for i, mail in enumerate(inbox):
        print(f"Email {i}: {mail.subject_line} {mail.read_status()} and {mail.spam_status()}")    #lists each email subject line with a number

def read_email(x):                      #prints the email item and sets read to true, gives a option to mark as spam
    i = inbox[x]
    print(f"{i.email_address}\n{i.subject_line}\n{i.email_contents}")
    i.mark_as_read()
    spam = input("Would you like to mark it as spam? 1 = yes  2 = no : ")
    if spam == "1":
        i.mark_as_spam()
        print(f"Email {x} has been marked as spam")
    elif spam != "1":
        return
        

while True:
    j = int(input("Choose a mode from the following:\n1. Read an email\n2. view unread emails\n3. Quit application\nYour choice: "))

    if j == 1:                     #menu to choose read emails, list unread email or exit the application
        list_emails()
        read_email(int(input("please input a number to see the email: ")))
    elif j == 2:
        for i, mail in enumerate(inbox):
            if mail.has_been_read == False:
                print(f"Email {i}: {mail.subject_line} is {mail.read_status()} and {mail.spam_status()}")

    elif j == 3:
        break
