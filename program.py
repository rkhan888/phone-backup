from shutil import copyfile

def copyFile(phoneFileLoc, localFileLoc, diffFileLoc, src, dest):

    diff = []
    filePresent = False

    with open(phoneFileLoc) as f:
        phoneFilesList = f.read().splitlines()

    with open(localFileLoc) as f:
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
    with open(diffFileLoc, 'w') as filehandle:
        for listitem in diff:
            filehandle.write('%s\n' % listitem)

    # copy new files
    for fileName in diff:
        if len(fileName) !=0:
            copyfile(src + fileName, dest + fileName)

    # update the local file manually by copying all names in diff file to the local file



if __name__ == '__main__':
    print("prgrm running")

    dcimLocalFileNames = "LocalFileNames.txt"
    dcimPhoneFileNames = "PhoneFileNames.txt"
    wtsappLocalImgFiles = "LocalFilesWhatsappImgs.txt"
    wtsappPhoneImgFiles = "PhoneFilesWhatsappImgs.txt"
    wtsappLocalVdoFiles = "LocalFilesWhatsappVdos.txt"
    wtsappPhoneVdoFiles = "PhoneFilesWhatsappVdos.txt"

    wtsappImgDiff = "wtsappImgDiff.txt"
    wtsappVdoDiff = "wtsappVdoDiff.txt"

    wtsappTempSrc = "D:/Phone Backups/s10e Rumman/WhatsApp/temp/"
    wtsappImgDest = "D:/Phone Backups/s10e Rumman/WhatsApp/Media/WhatsApp Images/"
    wtsappVdoDest = "D:/Phone Backups/s10e Rumman/WhatsApp/Media/WhatsApp Video/"

    copyFile(wtsappPhoneVdoFiles, wtsappLocalVdoFiles, wtsappVdoDiff, wtsappTempSrc, wtsappVdoDest)