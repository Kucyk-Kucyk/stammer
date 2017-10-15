import os
import msvcrt
from msvcrt import getch
import time
from random import choice

os.system('cls') 
os.system('title stammer')
cwd = os.getcwd()
fwd = os.path.join(cwd, r'stammerfiles')
nwd = os.path.join(cwd, r'drawfiles')
if not os.path.exists(fwd):
   os.makedirs(fwd)

title = 'stammer'
version = '1.2'

bcolors = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
entry = []
linecount = 0
tabnum = 0
spaces = '    '
thing = '>>>'
yestab = ['if ','elif ','else ','while ','for ','def ', 'class ']
colon = ':'

def demo():
    
    demo = 0

    while demo < 10 :
       col = choice(bcolors)
       wor = choice(yestab)
       siz = choice(range(10,80))
       siz2 = choice(range(10,80))
       os.system('mode con:cols=%s lines=%s' % (siz, siz2))
       print wor * 2000
       os.system('color 0%s' % (col))
       demo += 1
       time.sleep(0.01)
       os.system('cls')

    os.system('color 07')
    os.system('mode con:cols=13 lines=13')
    print '\n' * 4
    print 's t a m m e r'
    time.sleep(3)
    os.system('cls')
    os.system('mode con:cols=100 lines=50')
    os.system('cls')


demo()
print title, version
print

while True:
   key = 0
   tab = tabnum * spaces
   print linecount,
   text = raw_input(thing + '>' + tab)

   for x in yestab:
      if x in text:
         if colon in text :
            tabnum = tabnum + 1
   
   if text == '\t' :
      tabnum = tabnum - 1
      os.system('cls')
      print title, version
      print
      linecount = 0
      for x,y in enumerate(entry):
         if linecount in range(0,10):
            thing = '>>>'
         elif linecount in range(10,100):
            thing = '>>'
         elif linecount in range(100,1000):
            thing = '>'
         print linecount, thing + '>' + y,
         linecount = linecount + 1
         
   elif text == 'keeys' :
      os.system('cls')
      print title, version
      print
      print
      print '   K E Y Y S'
      print '   ~~~~~~~~~'
      print
      print '   press any key to get its ord(getch()) number.'
      print
      print '   press enter to leave.'
      print
      print '   by the way, number for enter is 13.'
      print
      print
      while True:
       key = ord(getch())
       print '  ',key
       if key == 13:
          break
      os.system('cls')
      print title, version
      print
      linecount = 0
      for x,y in enumerate(entry):
         if linecount in range(0,10):
            thing = '>>>'
         elif linecount in range(10,100):
            thing = '>>'
         elif linecount in range(100,1000):
            thing = '>'
         print linecount, thing + '>' + y,
         linecount = linecount + 1
         
   elif text == 'chaars':
      os.system('cls')
      print title, version
      print
      print
      print '   C H A A R S'
      print '   ~~~~~~~~~~~'
      print
      print '   press enter for next.'
      print
      print '   type exit to leave.'
      print
      a = 0
      while True:
          a = a + 1
          print '  ',a, chr(a)
          b = raw_input('   ')
          if b == 'exit':
             break
      os.system('cls')
      print title, version
      print
      linecount = 0
      for x,y in enumerate(entry):
         if linecount in range(0,10):
            thing = '>>>'
         elif linecount in range(10,100):
            thing = '>>'
         elif linecount in range(100,1000):
            thing = '>'
         print linecount, thing + '>' + y,
         linecount = linecount + 1
         
   elif text == 'coolors':
      b = '0'
      f = '7'
      os.system('cls')
      print title, version
      print
      print
      print '   C O O L O R S'
      print '   ~~~~~~~~~~~~~'
      print
      print '   0 : black.    8 : gray. '
      print '   1 : blue.     9 : light blue.'
      print '   2 : green.    a : light green.'
      print '   3 : cyan.     b : light cyan.'
      print '   4 : red.      c : light red.'
      print '   5 : magenta.  d : light magenta.'
      print '   6 : yellow.   e : light yellow.'
      print '   7 : white.    f : bright white.'
      print
      b = raw_input('   background color : ')
      print
      f = raw_input('   text color : ')
      os.system('color %s%s' % (b, f))
      os.system('cls')
      print title, version
      print
      linecount = 0
      for x,y in enumerate(entry):
         if linecount in range(0,10):
            thing = '>>>'
         elif linecount in range(10,100):
            thing = '>>'
         elif linecount in range(100,1000):
            thing = '>'
         print linecount, thing + '>' + y,
         linecount = linecount + 1
         
   elif text == 'exxit':
      break
   
   elif text == 'saave':
      if len(entry) != 0:
         os.system('cls')
         print title, version
         print
         print
         print '   S A A V E'
         print '   ~~~~~~~~~'
         print
         name = raw_input('   save under what name ? ')
         print
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
         print
         print '   N O T H I N G  T O  S A A V E'
         print '   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
         print
         print '   file is empty.'
         time.sleep(1.5)
         os.system('cls')
         print title, version
         print
         
   elif text == 'oppen':
      linecount = 0
      os.system('cls')
      print title, version
      print
      print
      print '   O P P E N'
      print '   ~~~~~~~~~'
      print
      name = raw_input('   open what file ? ')
      if name:
         os.system('cls')
         print title, version
         print
         for line in open('%s\\%s.py' % (fwd, name),'r'):
            if linecount in range(0,10):
               thing = '>>>'
            elif linecount in range(10,100):
               thing = '>>'
            elif linecount in range(100,1000):
               thing = '>'
            print linecount, thing + '>' + line,
            entry.append(line)
            linecount = linecount + 1
      else:
         linecount = 0
         os.system('cls')
         print title, version
         print
         
   elif text == 'eddit':
      os.system('cls')
      print title, version
      print
      linecount = 0
      for x,y in enumerate(entry):
         if linecount in range(0,10):
            thing = '>>>'
         elif linecount in range(10,100):
            thing = '>>'
         elif linecount in range(100,1000):
            thing = '>'
         print linecount, thing + '>' + y,
         linecount = linecount + 1
      print
      print '   E D D I T'
      print '   ~~~~~~~~~'
      print
      name = raw_input('   edit what line ? ')
      if name:
         name = int(name)
         os.system('cls')
         print title, version
         print
         linecount = 0
         for x,y in enumerate(entry):
            if linecount in range(0,10):
               thing = '>>>'
            elif linecount in range(10,100):
               thing = '>>'
            elif linecount in range(100,1000):
               thing = '>'
            print linecount, thing + '>' + y,
            linecount = linecount + 1
         print
         print '   E D D I T'
         print '   ~~~~~~~~~'
         print
      else:
         linecount = 0
         os.system('cls')
         print title, version
         print
      overwrite = raw_input('   replace with what ? >')
      if overwrite:
         entry[name]= overwrite + '\n'
         os.system('cls')
         print title, version
         print
         linecount = 0
         for x,y in enumerate(entry):
            if linecount in range(0,10):
               thing = '>>>'
            elif linecount in range(10,100):
               thing = '>>'
            elif linecount in range(100,1000):
               thing = '>'
            print linecount, thing + '>' + y,
            linecount = linecount + 1
      else:
         linecount = 0
         os.system('cls')
         print title, version
         print
         
   elif text == 'ruun':
      os.system('cls')
      print title, version
      print
      print
      print '   R U U N'
      print '   ~~~~~~~'
      print
      print '   python files only.'
      print
      print '   no extension needed.'
      print
      print
      folder = raw_input('   from which folder (stammer / draw) ? ')
      if folder == 'stammer':
         folder = fwd
      elif folder == 'draw':
         folder = nwd
      else:
         print 'nope'
      print
      name = raw_input('   run what file ? ')
      os.system('cls')
      os.system('python %s\\%s.py' % (folder, name))
      raw_input()
      os.system('cls')
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
      
   elif text == 'rr':
      if len(entry) != 0:
            os.system('cls')
            print title, version
            print
            linecount = 0
            del entry[-1]
            for x,y in enumerate(entry):
               if linecount in range(0,10):
                  thing = '>>>'
               elif linecount in range(10,100):
                  thing = '>>'
               elif linecount in range(100,1000):
                  thing = '>'
               print linecount, thing + '>' + y,
               linecount = linecount + 1
      else:
         os.system('cls')
         print title, version
         print
         print
         print '   N O T H I N G  T O  D E E L'
         print '   ~~~~~~~~~~~~~~~~~~~~~~~~~~~'
         print
         print '   file is empty.'
         time.sleep(1.5)
         os.system('cls')
         print title, version
         print

   elif text == 'addd':
      print
      name = raw_input('   add line after what line number ? ')
      entry.insert(int(name) + 1, (tab+''+'\n'))
      os.system('cls')
      print title, version
      print
      linecount = 0
      for x,y in enumerate(entry):
         if linecount in range(0,10):
            thing = '>>>'
         elif linecount in range(10,100):
            thing = '>>'
         elif linecount in range(100,1000):
            thing = '>'
         print linecount, thing + '>' + y,
         linecount = linecount + 1

   elif text == 'deel':
      print
      name = raw_input('   delete what line ? ')
      del entry[int(name)]
      os.system('cls')
      print title, version
      print
      linecount = 0
      for x,y in enumerate(entry):
         if linecount in range(0,10):
            thing = '>>>'
         elif linecount in range(10,100):
            thing = '>>'
         elif linecount in range(100,1000):
            thing = '>'
         print linecount, thing + '>' + y,
         linecount = linecount + 1
         
   elif text == 'heelp':
      os.system('cls')
      print title, version
      print
      print
      print '   H E E L P'
      print '   ~~~~~~~~~'
      print
      print '   <file management>'
      print
      print '   oppen : open file.'
      print '   saave : save file.'
      print '   eddit : edit line.'
      print '   ruun  : run file (python files only).'
      print
      print
      print '   <edition>'
      print
      print '   tab + enter : reverse tab.'
      print '   rr          : delete last line.'
      print '   cllear      : clear screen.'
      print '   addd        : add empty line.'
      print '   deel        : delete line.'
      print
      print
      print '   <display>'
      print
      print '   coolors : change colors.'
      print
      print
      print '   <python toolbox>'
      print
      print '   chaars : list of char and their numbers for chr()'
      print '   keeys  : show key numbers for ord(getch()).'
      print '   draaw  : ASCII based drawing.'
      print
      print
      print
      raw_input('   press enter to exit heelp')
      os.system('cls')
      print title, version
      print
      linecount = 0
      for x,y in enumerate(entry):
         if linecount in range(0,10):
            thing = '>>>'
         elif linecount in range(10,100):
            thing = '>>'
         elif linecount in range(100,1000):
            thing = '>'
         print linecount, thing + '>' + y,
         linecount = linecount + 1
         
   elif text == 'draaw':
      import draw
      os.system('cls')
      print title, version
      print
      linecount = 0
      
   else :
      if linecount in range(0,9):
         thing = '>>>'
         linecount = linecount + 1
         entry.append(tab+text+'\n')
      elif linecount in range(9,99):
         thing = '>>'
         linecount = linecount + 1
         entry.append(tab+text+'\n')
      elif linecount in range(99,999):
         thing = '>'
         linecount = linecount + 1
         entry.append(tab+text+'\n')
      else :
         linecount = linecount + 1
         entry.append(tab+text+'\n')
        


        
