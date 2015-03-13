# -*- coding: utf-8 -*- 

#------------------------------------------------
#             Osiris-bot Config file
#                  v0.2beta
#------------------------------------------------

RSSsettings = {
'whoami'	: u'rss',
'jid'		: u'rss_login@server.tld/osiris rss',
'password'	: u'********',
'status'	: u'online',
'message'	: u'Osiris RSS/ATOM feed bot',
'priority'	: 777,
'msglimit'	: 4096,
'port'		: 5222}

TRsettings = {
'whoami'	: u'translate',
'jid'		: u'tr_login@server.tld/osiris translate',
'password'	: u'********',
'status'	: u'online',
'message'	: u'Osiris translate bot',
'priority'	: 777,
'msglimit'	: 512,
'port'		: 5222}

Settings = [RSSsettings,TRsettings]
Owner = ['jid1@server.tld','jid2@server.tld','jid3@server.tld']
Ignore = ['gmail.com']

#debugmode = True
#dm = True
#dm2 = True

CommandsLog = True
#ENABLE_TLS = False