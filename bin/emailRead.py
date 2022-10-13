from base64 import decode
import email
import imaplib
def parseMail(messages):
    output = []
    for message in messages:
        msg = email.message_from_bytes(message[0][1])
        if msg.is_multipart():
            parts = []
            for part in msg.walk():
                fileName = part.get_filename()
                if fileName != None:
                    output.append({'fileName': fileName, 'object': part})
    if output != []: return output
    return None



        
def checkMail(server,port,mailAddress,passwd,maxAttach): #returns list of emails in mailbox
    mailBox = imaplib.IMAP4_SSL(server,port)
    mailBox.login(mailAddress,passwd)
    mailBox.select('INBOX')
    idList = [int(x) for x in mailBox.search(None,'ALL')[1][0].split()]
    if len(idList) > maxAttach:
        idList = idList[-maxAttach:]
    messages = []
    for id in idList:
        messages.append(mailBox.fetch(str(id),'(RFC822)')[1])
    return messages