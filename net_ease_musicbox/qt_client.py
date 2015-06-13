# coding: utf-8
import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from net_ease_musicbox import PROJECT_ROOT


class MyApplication(QApplication):
    def __init__(self, args):
        super(MyApplication, self).__init__(args)
        self.installEventFilter(self)

    # def notify(self, receiver, event):
    #     if (event.type() == QEvent.KeyPress):
    #         QMessageBox.information(None, "Received Key Press Event!!",
    #                                 "You Pressed: " + event.text())
    #     # Call Base Class Method to Continue Normal Event Processing
    #     return super(MyApplication, self).notify(receiver, event)

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseMove):
            pos = event.pos()
            print('mouse move: (%d, %d)' % (pos.x(), pos.y()))
        return QWidget.eventFilter(self, source, event)


class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None, app=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        self.menu = QtGui.QMenu(parent)
        nextSong = self.menu.addAction(u"下一首")
        prevSong = self.menu.addAction(u"前一首")
        pausePlay = self.menu.addAction(u"暂停/播放")
        exitAction = self.menu.addAction(u"退出网易云音乐")
        exitAction.triggered.connect(app.quit)
        self.setContextMenu(self.menu)

    def exit(self):
        print "exit"


def qt_tray():
    app = QtGui.QApplication(sys.argv)
    icon = QtGui.QIcon(os.path.join(PROJECT_ROOT, "resources/netease_logo.xpm"))
    trayIcon = SystemTrayIcon(icon, app=app)
    trayIcon.show()
    sys.exit(app.exec_())


def main():
    app = MyApplication(sys.argv)
    window = QWidget()

    # Resize width and height
    window.resize(250, 250)
    window.setWindowTitle('PyQt QApplication Key Press')
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    qt_tray()
