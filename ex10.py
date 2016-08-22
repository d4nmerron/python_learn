print "I am 6'2\" Tall."# escape double-quote inside string
print 'I am 6\'2" tall.' # escape singl-quote inside string


tabby_cat = "\tI'm tabbed in"
persian_cat  = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"

fat_cat = '''
I'll do a list: 
\t* Cat Food
\t* Fishies
\t* Poo\n\t* poo2
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,