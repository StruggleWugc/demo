'''通过函数 addDirectPath 将当前目录下的文件夹（含子文件夹）的绝对路径添加到
   sys目录中。运行一个py文件时，当前目录会自动添加到sys目录中，无需手动添加!
'''

import os,sys
def getFolderName(path):        #获取当前目录下的文件和文件夹
    dirList = []
    fileList = []

    files=os.listdir(path)   #当前路径下所有的文件和文件夹
    for f in files:
        if(os.path.isdir(path +'/' + f)):
            if(f[0] == '.'):    #排除隐藏文件夹
               pass
            else:
               dirList.append(f)
        if(os.path.isfile(path + '/' +f)):
               fileList.append(f)
    return dirList

def addDirectPath(path):
    folderList = getFolderName(path)
    if folderList !=[]:
        for f in folderList:
            if f !='__pycache__':
                sys.path.append(path.replace('\\','/') + '/' +f) #添加系统变量
                abspath = path + '\\' + f
                addDirectPath(abspath)

#addDirectPath(os.curdir)
addDirectPath(sys.path[0])

if __name__ == "__main__":
    print(os.path.abspath(os.curdir))
    plen = len(sys.path)
    for p in range(plen):
        print(sys.path[p])
