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
			'S': "am Strand",
			'L': "am Land",
			'SR': "am Siedlungsrand",
			'SN': u"in Strandn\"ahe"
			}
	return d[s]

def format_geb(s):
	d = { 
			'+': 'viele Geb"aude',
			'-': 'wenige Geb"aude'
			}
	return d[s]
			
def format_num(n):
	return n[:7]

def format_percent(p):
	p = p.replace(",", ".")
	return str(int(float(p) * 100)) + "\%"

counter = 0
for i in l:
	counter += 1
	out = ""
	out += str(counter) + " & "
	out += i[0] + " " + format_lage(i[1]) + ', ' + format_geb(i[2]) + ' & '

	for j in xrange(5, 10):
		out += format_num(i[j]) + ' & ' 

	out += format_percent(i[10])

	out += "\\\\"
	print out



#pdb.set_trace()

