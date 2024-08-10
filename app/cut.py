import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QPainter, QPen, QGuiApplication

class ScreenshotSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Screenshot Selector')
        self.setWindowOpacity(0.2)
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
            self.start_point = event.globalPos()
            self.is_selecting = True

    def mouseMoveEvent(self, event):
        if self.is_selecting:
            self.end_point = event.globalPos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.end_point = event.globalPos()
            self.is_selecting = False
            self.capture_screenshot()

    def paintEvent(self, event):
        if self.start_point and self.end_point:
            painter = QPainter(self)
            pen = QPen(Qt.red, 2, Qt.SolidLine)
            painter.setPen(pen)

            # Obtenha a geometria da tela atual para calcular as coordenadas relativas
            current_screen = QGuiApplication.screenAt(self.start_point)
            if current_screen:
                screen_rect = current_screen.geometry()
                adjusted_start = self.start_point - screen_rect.topLeft()
                adjusted_end = self.end_point - screen_rect.topLeft()
                rect = QRect(adjusted_start, adjusted_end)
                painter.drawRect(rect)

    def capture_screenshot(self):
        rect = QRect(self.start_point, self.end_point).normalized()
        
        # Itera sobre todos os monitores
        for screen in QGuiApplication.screens():
            if screen.geometry().intersects(rect):
                # Converte as coordenadas globais para as coordenadas do monitor
                screen_rect = rect.translated(-screen.geometry().topLeft())
                screenshot = screen.grabWindow(0, screen_rect.left(), screen_rect.top(), screen_rect.width(), screen_rect.height())
                screenshot.save('screenshot.png', 'png')
                break
        
        self.close()
