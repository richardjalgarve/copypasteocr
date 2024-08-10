import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QPainter, QPen

class ScreenshotSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Screenshot Selector')
        self.setWindowOpacity(0.3)
        self.setWindowState(Qt.WindowFullScreen)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.start_point = None
        self.end_point = None
        self.is_selecting = False

        self.label = QLabel(self)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.pos()
            self.is_selecting = True

    def mouseMoveEvent(self, event):
        if self.is_selecting:
            self.end_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.end_point = event.pos()
            self.is_selecting = False
            self.capture_screenshot()

    def paintEvent(self, event):
        if self.start_point and self.end_point:
            painter = QPainter(self)
            pen = QPen(Qt.blue, 2, Qt.SolidLine)
            painter.setPen(pen)
            rect = QRect(self.start_point, self.end_point)
            painter.drawRect(rect)

    def capture_screenshot(self):
        rect = QRect(self.start_point, self.end_point).normalized()
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(0, rect.left(), rect.top(), rect.width(), rect.height())
        screenshot.save('screenshot.png', 'png')
        self.close()
