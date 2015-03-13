#!/usr/bin/python
# -*- coding: utf -*-

import os, sys, time
pid_file = 'osiris.pid'

def writefile(filename, data): file(filename, 'w').write(data)

def tZ(val):
	val = str(val)
	if len(val) == 1: val = '0'+val
	return val

def printlog(text):
	print text
	lt = tuple(time.localtime())
	fname = 'log/crash_%s%s%s.txt' % (tZ(lt[0]),tZ(lt[1]),tZ(lt[2]))
	fbody = '%s%s%s|%s\n' % (tZ(lt[3]),tZ(lt[4]),tZ(lt[5]),text)
	open(fname, 'a').write(fbody.encode('utf-8'))

def crash(text):
	printlog(text)
	sys.exit()

if os.name == 'nt': printlog('Warning! Correct work only on *NIX system!')

try: writefile('settings/starttime',str(int(time.time())))
except:
	printlog('\n'+'*'*50+'\n Osiris is crashed! Incorrent launch!\n'+'*'*50+'\n')
	raise

if os.path.isfile(pid_file):
	try: last_pid = int(file(pid_file).read())
	except: crash('Unable get information from %s' % pid_file)
	try:
		os.getsid(last_pid)
		printlog('Multilaunch detected! Pid %s is killed!' % last_pid)
		os.kill(int(last_pid),3)
		time.sleep(1)
		try: os.kill(int(last_pid),9)
		except: pass
	except Exception, SM:
		if not str(SM).lower().count('no such process'): crash('Unknown exception!\n%s' % SM)
	
writefile(pid_file,str(os.getpid()))

os.system('echo `svnversion` > version')

while 1:
	try: execfile('kernel.py')
	except KeyboardInterrupt: break
	except SystemExit, mode:
		mode = str(mode)
		if mode == 'update':
			os.system('svn up')
			os.system('echo `svnversion` > version')
		elif mode == 'exit': break
		elif mode == 'restart': pass
		else:
			printlog('unknown exit type!')
			break
	except Exception, SM:
		printlog('\n'+'*'*50+'\n Osiris is crashed! It\'s imposible, but You do it!\n'+'*'*50+'\n')
		printlog(str(SM)+'\n')
		raise
