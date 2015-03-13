#!/usr/bin/python
# -*- coding: utf -*-

#      copy feed to dump
# (c) Disabler Producion Lab.

import sys, os, time

feeds = 'settings/feed'
dump = 'feed.dump'

def readfile(filename):
	fp = file(filename)
	data = fp.read()
	fp.close()
	return data

def writefile(filename, data):
	fp = file(filename, 'a')
	fp.write(data)
	fp.close()

fd = eval(readfile(feeds))

orders = ['url','per','type','time','jid']

print 'Use %s with one of parameter %s' % (sys.argv[0],'|'.join(orders))

try:
	if sys.argv[1] in orders: order = sys.argv[1]
	else: order = 'jid'
except: order = 'jid'

tmp = []

#[u'http://bash.org.ru/rss', u'10m', u'full-url-headline', 1280957978, u'jidd@aaa.xxx',
#             0                 1              2               3               4

for t in fd:
	if order == 'jid': tmp.append((t[4],t[0],t[1],t[2],time.ctime(t[3])))
	elif order == 'url': tmp.append((t[0],t[4],t[1],t[2],time.ctime(t[3])))
	elif order == 'per': tmp.append((t[1],t[0],t[4],t[2],time.ctime(t[3])))
	elif order == 'type': tmp.append((t[2],t[0],t[4],t[1],time.ctime(t[3])))
	elif order == 'time': tmp.append((time.ctime(t[3]),t[0],t[4],t[1],t[2]))
tmp.sort()

if os.path.isfile(dump): os.remove(dump)

for t in tmp: writefile(dump,'\t'.join(t)+'\n')

print 'finished!'