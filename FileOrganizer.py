import os
import shutil
import sys
import time

SHIP_DIRECTORY_TO_OTHERS = False

PDF_DIR_NAME = 'PDFs'
DOC_DIR_NAME = 'Documents'
MUSIC_DIR_NAME = 'Music'
VIDEO_DIR_NAME = 'Videos'
SOFTWARE_DIR_NAME = 'Softwares'
IMAGE_DIR_NAME = 'Images'
OTHER_DIR_NAME = 'Others'

def isPathExists(path):
    return os.path.exists(path)

def getPathList(args = sys.argv):
    validPaths = []
    argsExcludingFileName = args[1:]
    if len(argsExcludingFileName) > 0:
        for path in argsExcludingFileName:
            if isPathExists(path):
                validPaths.append(path)
            else:
                print(f'Invalid path - {path}. Skipping this one...')
    else:
        validPaths.append(os.getcwd())
    return validPaths

def getFileExtension(fileName):
    return os.path.splitext(fileName)[1]

def isPdfFile(fileName):
    return getFileExtension(fileName) == '.pdf'

def isMusicFile(fileName):
    fileExtension = getFileExtension(fileName)
    return fileExtension == '.mp3' or fileExtension == '.wav' or fileExtension == '.midi'

def isVideoFile(fileName):
    fileExtension = getFileExtension(fileName)
    return fileExtension == '.mp4' or fileExtension == '.mov' or fileExtension == '.avi' or fileExtension == '.mpeg' or fileExtension == '.mpg'

def isDocFile(fileName):
    fileExtension = getFileExtension(fileName)
    return fileExtension == '.doc' or fileExtension == '.docx' or fileExtension == '.xlsx' or fileExtension == '.xls' or fileExtension == '.txt' or fileExtension == '.odt' or fileExtension == '.ppt' or fileExtension == '.pptx' or fileExtension == '.zip' or fileExtension == '.csv'

def isSoftware(fileName):
    fileExtension = getFileExtension(fileName)
    return fileExtension == '.exe' or fileExtension == '.apk' or fileExtension == '.bin' or fileExtension == '.bat' or fileExtension == '.com' or fileExtension == '.wsf' or fileExtension == '.dmg'

def isImageFile(fileName):
    fileExtension = getFileExtension(fileName)
    return fileExtension == '.jpg' or fileExtension == '.png' or fileExtension == '.jpeg' or fileExtension == '.gif' or fileExtension == '.tif'

def getTragetPath(fileName, path):
    if isPdfFile(fileName):
        targetPath = os.path.join(path,PDF_DIR_NAME)
    elif isMusicFile(fileName):
        targetPath = os.path.join(path, MUSIC_DIR_NAME)
    elif isVideoFile(fileName):
        targetPath = os.path.join(path, VIDEO_DIR_NAME)
    elif isDocFile(fileName):
        targetPath = os.path.join(path, DOC_DIR_NAME)
    elif isSoftware(fileName):
        targetPath = os.path.join(path, SOFTWARE_DIR_NAME)
    elif isImageFile(fileName):
        targetPath = os.path.join(path, IMAGE_DIR_NAME)
    else:
        targetPath = os.path.join(path, OTHER_DIR_NAME)
    
    if not isPathExists(targetPath):
        os.makedirs(targetPath)
    
    return targetPath

def shiftFileToRespectiveSubfolder(filename, path):
    targetPath = getTragetPath(filename, path)
    print(f'Shifting {path}/{filename} to {targetPath}/{filename}')
    shutil.move(os.path.join(path,filename),targetPath)

def checkFilesAndStartShifting(path):
    for filename in os.listdir(path):
        if not os.path.isdir(path+'/'+filename) and not filename == '.DS_Store':
            shiftFileToRespectiveSubfolder(filename, path)

def startFileOrganizer():
    startTime = time.time()
    pathList = getPathList()
    for path in pathList:
        checkFilesAndStartShifting(path)
    endTime = time.time()
    print('Finished rearranging files !..!')
    print(f'Process completed in {endTime - startTime} seconds.')

startFileOrganizer()