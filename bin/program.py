import init
import emailRead
import downloads

def main():
    server, port, mailAddress, passwd, maxAttachments = init.returnVals()
    path = init.attachmentsDir()
    init.attachmentsCSV()

    while True:
        print(f'Checking mail: last {maxAttachments} values')
        emails = emailRead.checkMail(server, port, mailAddress, passwd,maxAttachments)
        print('Searching for attachments')
        files = emailRead.parseMail(emails)
        print(f'found {len(files)} attachments')

        downloaded = downloads.readDict()
        toDownload = cullDict(files,downloaded)

        if len(toDownload) + len(downloaded) > maxAttachments:
            downloads.removeExcess(len(toDownload) + len(downloaded) - maxAttachments, downloaded)

        if len(toDownload) > 0:
            print(f'found {len(toDownload)} items:')
            for item in toDownload: print(f'\t{item["fileName"]}')
            downloads.downloadAttachments(files,path)
            downloads.writeDict(files)
        else:
            print('no new downloads found')

def cullDict(fileList,downloadedList):
    output = []
    for item in fileList:
        if item['fileName'] not in downloadedList:
            output.append(item)
    return output


if __name__ == '__main__':
    main()


