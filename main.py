import sys
from threading import Thread
from math import floor

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

from mainform import Ui_Form  # if toplevel widget in .ui file is also called "sss"

import youtube_dl


class Logger(object):
    def debug(self, msg):
        print(msg)
        pass

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)
        
downloading = False

class MainForm(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.addFunctionality(Form)

    def addFunctionality(self, Form):
        self.dlButton.clicked.connect(lambda: self.downloadVideo())
    def progress_hook(self, d):
        percent_str = d['_percent_str']
        percent_str = percent_str[:len(percent_str)-1]
        self.progressBar.setValue(floor(float(percent_str)))
        pass

    def downloadVideo(self):
        if not downloading:
            downloading = True
            Thread(target=self.runYoutubeDl).start()

    def runYoutubeDl(self):
        ydl_opts = {
            'format': 'best',
            'logger': Logger(),
            'progress_hooks': [self.progress_hook]
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.linkLineEdit.text()])

        downloading = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = MainForm()
        ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())