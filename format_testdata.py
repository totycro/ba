#!/usr/bin/env python2.7
import csv
import operator
import pdb

r = csv.reader(open("testdata-dump.csv", 'r'), delimiter=",", quotechar="\"")

l = [ i for i in r ]

l = l[3:15]

l.sort(key=operator.itemgetter(0))

def format_lage(s):
	d = {
			'S': "Strand",
			'L': "Land",
			'SR': "Siedlungsrand",
			'SN': u"Strandn\"ahe"
			}
	return d[s]

def format_geb(s):
	d = { 
			'+': 'viele Geb"aude',
			'-': 'wenige Geb"aude'
			}
	return d[s]
			
def format_num(n, x=5):
	n = float(n.replace(",", "."))
	return '%F' % n # round(n, x) 

def format_percent(p, add_plus=False):
	p = p.replace(",", ".")
	val = round(float(p) * 100, 1)
	val_str = str(val)+ "\%"
	if add_plus and val > 0:
		val_str = "+"+val_str
	return val_str

def format_counter(c):
	s = "UC"
	if c < 10: s +="0"
	s += str(c)
	return s

counter = 0
tab1 = ""
tab2 = ""
for i in l:
	counter += 1
	#if counter == 10: import pudb ; pudb.set_trace()
	out1 = ""
	out2 = ""

	out1 += format_counter(counter) + " & "
	out2 += format_counter(counter) + " & "

	out1 += i[0] + " & " + format_lage(i[1]) + ' & ' + format_geb(i[2]) 

	for j in xrange(5, 9):
		out2 += format_num(i[j]) + ' & ' 

	out2 += format_num(i[9], 6) + ' & '
	out2 += format_percent(i[10])

	out1 += "\\\\"
	out2 += "\\\\"

	tab1 += out1 + "\n"
	tab2 += out2 + "\n"

print tab1
print
print tab2



#pdb.set_trace()

