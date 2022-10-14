from genericpath import isdir
import os
import platform

def returnVals():
    path = os.path.dirname(os.getcwd()) + '\config.cfg'

    output = []
    with open(path,'r') as initcfg:
        for line in initcfg:
            output.append(line.split(': ')[1].split('\n')[0])
    return(output[0],int(output[1]),output[2],output[3],int(output[4]))

def attachmentsDir():
    attachmentPath = os.path.dirname(os.getcwd()) + '\\attachments\\'
    if not os.path.isdir(attachmentPath): 
        print(f'attachments dir missing, making at {attachmentPath}')
        os.mkdir(attachmentPath)
    return attachmentPath

def attachmentsCSV():
    if not os.path.exists('attachments.csv'):
        print(f'attachments.csv missing, making at{os.path.dirname(os.path.realpath("init.py"))}' + '\\attachments.csv')
        with open('attachments.csv','w') as attachments:
            attachments.write('')

def detectOS():
    return platform.system()

if __name__ == '__main__':
    print(detectOS())
