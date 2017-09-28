import os
import msvcrt
import time

os.system('cls')
os.system('color 06')  
os.system('title Stammer')
cwd = os.getcwd()
fwd = os.path.join(cwd, r'stammerfiles')
if not os.path.exists(fwd):
   os.makedirs(fwd)

title = 'Stammer'
version = '1.0'

entry = []
linecount = 0
tabnum = 0
spaces = '    '
thing = '  '
yestab = ['if','elif','else','while','for','def']

print title, version
print

while True:
    tab = tabnum * spaces
    
    print linecount,
    text = raw_input(thing + '>' + tab)

    for x in yestab:
        if x in text:
            tabnum = tabnum + 1
    if text == '\t':
        tabnum = tabnum - 1
        os.system('cls')
        print title, version
        print
        linecount = 0
        for x,y in enumerate(entry):
            print linecount,'>' + y,
            linecount = linecount + 1
    elif text == 'exxit':
        break
    elif text == 'saave':
        if len(entry) != 0:
            os.system('cls')
            print title, version
            print
            name = raw_input('Save under what name ?\n')
            file = open('%s\\%s.py' % (fwd, name),'w')
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
        for line in open('%s\\%s.py' % (fwd, name),'r'):
            print linecount, thing + '>' + line,
            entry.append(line)
            linecount = linecount + 1
    elif text == 'eddit':
        os.system('cls')
        print title, version
        print
        linecount = 0
        for x,y in enumerate(entry):
                print linecount, thing + '>' + y,
                linecount = linecount + 1
        print
        name = raw_input('Edit what line ?\n')
        name = int(name)
        os.system('cls')
        print title, version
        print
        linecount = 0
        for x,y in enumerate(entry):
                print linecount, thing + '>' + y,
                linecount = linecount + 1
        print
        overwrite = raw_input('Replace with what ?\n')
        entry[name]= overwrite + '\n'
        os.system('cls')
        print title, version
        print
        linecount = 0
        for x,y in enumerate(entry):
                print linecount, thing + '>' + y,
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
        print title, version
        print
    elif text == 'cllear':
        os.system('cls')
        print title, version
        print
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
                print linecount, thing + '>' + y,
                linecount = linecount + 1
    elif text == 'heelp':
        os.system('cls')
        print title, version
        print
        print '   H E E L P'
        print
        print '   tab + enter : del ident.'
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
        if linecount + 1 == 10 :
            thing = ' '
            linecount = linecount + 1
            entry.append(tab+text+'\n')
        elif linecount + 1 == 100 :
            thing = ''
            linecount = linecount + 1
            entry.append(tab+text+'\n')
        else :
            linecount = linecount + 1
            entry.append(tab+text+'\n')
        


        
