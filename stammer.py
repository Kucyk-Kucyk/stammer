import os
import msvcrt
import time

os.system('color 06')  
os.system('title Stammer')
os.system('mode con:cols=30 lines=30')
cwd = os.getcwd()

title = 'Stammer'
version = '1.0'
dev = 'kucyk-kucyk presents'

entry = []
linecount = 0
tabnum = 0
yestab = ['if','elif','else','while','for','def']

print title, version
print

while True:
    tab = tabnum * '    '
    
    print linecount,
    text = raw_input('>' + tab)

    for x in yestab:
        if x in text:
            tabnum = tabnum + 1
    if text == '\t':
        tabnum = 0
    elif text == 'exxit':
        break
    elif text == 'saave':
        if len(entry) != 0:
            os.system('cls')
            print title, version
            print
            name = raw_input('Save under what name ?\n')
            file = open('%s.py' % name,'w')
            file.write(''.join(entry))
            file.close()
            linecount = 0
            entry = []
            os.system('cls')
            print title, version
            print
        else:
            os.system('cls')
            print title, version
            print
            print 'File is empty.'
            time.sleep(0.5)
            os.system('cls')
            print title, version
            print
            
    elif text == 'oppen':
        linecount = 0
        os.system('cls')
        print title, version
        print
        name = raw_input('Open what file ?\n')
        os.system('cls')
        print title, version
        print
        for line in open('%s.py' % name,'r'):
            print linecount,'>'+line,
            entry.append(line)
            linecount = linecount + 1
    elif text == 'eddit':
        os.system('cls')
        print title, version
        print
        linecount = 0
        for x,y in enumerate(entry):
                print linecount,'>' + y,
                linecount = linecount + 1
        print
        name = raw_input('Edit what line ?\n')
        name = int(name)
        os.system('cls')
        print title, version
        print
        linecount = 0
        for x,y in enumerate(entry):
                print linecount,'>' + y,
                linecount = linecount + 1
        print
        overwrite = raw_input('Replace with what ?\n')
        entry[name]= overwrite + '\n'
        os.system('cls')
        print title, version
        print
        linecount = 0
        for x,y in enumerate(entry):
                print linecount,'>' + y,
                linecount = linecount + 1
    elif text == 'ruun':
        os.system('cls')
        print title, version
        print
        name = raw_input('Run what file ?\n')
        os.system('python %s\\%s.py' % (cwd, name))
        raw_input()
        os.system('cls')
        os.system('color 06')  
        os.system('title Stammer')
        os.system('mode con:cols=30 lines=30')
        print title, version
        print
    elif text == 'cllear':
        os.system('cls')
        print title, version
        linecount = 0
        entry = []
        save = []
        tabnum = 0
    elif text == 'deel':
        os.system('cls')
        print title, version
        print
        linecount = 0
        del entry[-1]
        for x,y in enumerate(entry):
                print linecount,'>' + y,
                linecount = linecount + 1
    elif text == 'heelp':
        os.system('cls')
        print title, version
        print
        print '   H E E L P'
        print
        print '   oppen  : open file.'
        print '   saave  : save file.'
        print '   eddit  : edit file.'
        print '   ruun   : run file.'
        print '   deel   : delete last line.'
        print '   cllear : clear screen.'
        print '   exxit  : exit stammer.'
        print
    else :
        linecount = linecount + 1
        entry.append(tab+text+'\n')
        


        
