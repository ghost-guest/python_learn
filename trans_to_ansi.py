# -*- coding: utf-8 -*-

import chardet
import codecs
import unicode
str = open("2.txt","r",encoding='iso8859-1').readline()
uft_str = str.encode("iso-8859-1").decode('gbk').encode('utf8')
print(uft_str)

with open('3.txt', 'wb') as f:
     f.write(uft_str)

#保存ANSI格式
fh = open("3.txt","r",encoding="utf8").read()
with codecs.open('4.txt', 'w', 'gbk') as f:
     f.write(fh)
a = open('4.txt', 'rb').readline()
print(chardet.detect(a))
b = open('4.txt', 'r').readline()
planstr1 = unicode(b, 'iso-8859-1')

print(type(a))