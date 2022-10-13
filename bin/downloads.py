import email
import imaplib
import os

def removeExcess(num, fileList):
    for _ in range(num):
        filePath = os.path.dirname(os.getcwd()) + '\\attachments\\' + fileList[0]
        os.remove(filePath)
        print(f'removing {fileList.pop(0)} (exceeds MAX FILES)')

def downloadAttachments(attachmentDictList, path):
    for attachmentDict in attachmentDictList:
        fileName = attachmentDict['fileName']
        fileObject = attachmentDict['object']
        payLoad = fileObject.get_payload(decode=True)
        #print(payLoad)
        with open(path + fileName,'wb') as file:
            file.write(payLoad)

def writeDict(filesDictList):
    stringOut = ''
    for item in filesDictList:
        stringOut += item['fileName']
        stringOut += ';'

    with open('attachments.csv','w') as attachments:
        attachments.write(stringOut)

def readDict():
    output = []
    try:
        with open('attachments.csv','r') as attachments:
            output = attachments.read().split(';')[:-1]
    except:
        with open('attachments.csv','w') as attachments:
            
            attachments.write('')

    return output
if __name__ == '__main__':
    print(readDict())
        
            
