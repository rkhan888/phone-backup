from shutil import copyfile

def copyFile():

    diff = []
    filePresent = False

    with open('D:/Phone Backups/PhoneFileNames.txt') as f:
        phoneFilesList = f.read().splitlines()

    with open('D:/Phone Backups/LocalFileNames.txt') as f:
        localFilesList = f.read().splitlines()



    # with open('D:/Phone Backups/a.txt') as f:
    #     phoneFilesList = f.read().splitlines()
    #
    # with open('D:/Phone Backups/b.txt') as f:
    #     localFilesList = f.read().splitlines()

    # check for new files
    for phoneFile in phoneFilesList:
        for localFile in localFilesList:
            if phoneFile == localFile:
                filePresent = True
                break
        if not filePresent:
            diff.append(phoneFile)
        filePresent = False

    # create file of new file names
    with open('D:/Phone Backups/diffFile.txt', 'w') as filehandle:
        for listitem in diff:
            filehandle.write('%s\n' % listitem)

    # copy new files
    for fileName in diff:
        if len(fileName) !=0:
            copyfile("D:/Phone Backups/temp/" + fileName, "D:/Phone Backups/temp2/" + fileName)






if __name__ == '__main__':
    print("prgrm running")
    copyFile()