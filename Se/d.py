import win32com.client
import os
outlook=win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
inbox=outlook.GetDefaultFolder(6) #Inbox default index value is 6
message=inbox.Items
message2=message.GetLast()
subject=message2.Subject
body=message2.body
date=message2.senton.date()
sender=message2.Sender
attachments=message2.Attachments
for m in message:
    if m.Subject=="Your-subject-here":# here in my requirement i will change the dates
        print(m.body)
