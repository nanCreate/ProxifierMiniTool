import sys, os, pyperclip

argCount = len(sys.argv)

def makeData(analyzePath):
    analyzePath = analyzePath.replace('"', '')
    tempfilePath = os.getenv('APPDATA')+r'\temp.txt'

    def removeTemp():
        os.remove(tempfilePath) if os.path.exists(tempfilePath) else None

    removeTemp()

    # GET EXE FILE LIST
    os.system('dir /s/b "'+analyzePath+'\*.exe" >> "'+tempfilePath+'"')

    # RECONSTRUCT
    with open(tempfilePath, 'r+') as f:
        lines = list(map(lambda x: '"{}"; '.format(x.strip()), f.readlines()))
        f.seek(0)
        [f.write(l) for l in lines]

    # COPY RESULT
    result = open(tempfilePath, 'r', encoding='utf8')
    result=(str(result.read()))
    pyperclip.copy(result)

    # Done
    removeTemp()
    print('Список файлов скопирован в буфер обмена')


# Initial
if argCount > 1:
    makeData(sys.argv[1])
else:
    path = input("Введите путь к папке: ")
    makeData(path)