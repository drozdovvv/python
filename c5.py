#!/usr/bin/env python
#encoding: utf8 


#for index in range(0,len(nap), width):
	#print (nap[index:index+width].center(width))


import reregex_liczba = re.compile(
        r'''(?P<liczba> (([0-1][0-9][0-9])|(2[0-1][0-9])|(25[0-5]))
        )''',
        re.IGNORECASE | re.VERBOSE
)


tekst= u'012 sdjchd 1778 yye 398 255 oods 233'
#for match in regex_liczba.finditer(tekst):
       #print(match.groupdict())



