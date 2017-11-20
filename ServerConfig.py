#Embedded file name: ServerConfig.py

import os
import ServerInfo
ru = lambda text: text.decode('utf-8', 'ignore')
ur = lambda text: text.encode('utf-8', 'ignore')
name = '%s.ini' % ServerInfo.Info('name').get_info().replace(' ', '')
path = '/'
conf = '%s%s%s' % (os.getcwd(), path, name)

class Sets:

    def __init__(self):
        self.LHOST = ''
        self.LPORT = ''
        self.FQUERY = ''
        self.MQUERY = ''
        self.BQUERY = ''
        self.RQUERY = ''
        self.CQUERY = ''
        self.IQUERY = ''
        self.IMETHOD = ''
        self.ILINE = ''
        self.ISPLIT = ''
        self.RPORT = ''
        self.RPATH = ''
        self.ADMODE = ''
        self.CUSHDR0 = ''
        self.VALHDR0 = ''
        self.CUSHDR1 = ''
        self.VALHDR1 = ''
        self.CUSHDR2 = ''
        self.VALHDR2 = ''
        self.CUSHDR3 = ''
        self.VALHDR3 = ''
        self.KEEP = ''
        self.RHTTP = ''
        self.RHTTPS = ''
        self.SBUFF = ''
        self.TIMEOUT = ''
        self.PHOST = ''
        self.PPORT = ''
        self.PTYPE = ''
        self.load()

    def load(self):
        try:
            for name, value in [ line.split(' = ') for line in open(conf, 'rb').read().splitlines() ]:
                self.__dict__[name] = eval(value)

        except:
            self.save()
            for name, value in [ line.split(' = ') for line in open(conf, 'rb').read().splitlines() ]:
                self.__dict__[name] = eval(value)

    def save(self):
        data = ''
        for name in self.__dict__.keys():
            line = name + ' = ' + repr(self.__dict__[name]) + '\r\n'
            data += line

        open(conf, 'wb').write(ur(data))
        del data