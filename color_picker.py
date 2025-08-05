
import sys
from PyQt6 import QtWidgets, QtGui, QtCore
import mss
import PIL.Image
import pyperclip

class ColorPickerBubble(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint |
            QtCore.Qt.WindowType.Tool
        )
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_NoSystemBackground, True)

        self.label = QtWidgets.QLabel("#FFFFFF", self)
        self.label.setStyleSheet("""
            QLabel {
                background-color: rgba(0, 0, 0, 180);
                color: white;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
                font-family: monospace;
            }
        """)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateColor)
        self.timer.start(50)

        self.sct = mss.mss()

    def updateColor(self):
        pos = QtGui.QCursor.pos()
        monitor = {"top": pos.y(), "left": pos.x(), "width": 1, "height": 1}
        pixel = self.sct.grab(monitor)
        img = PIL.Image.frombytes("RGB", (1, 1), pixel.rgb)
        r, g, b = img.getpixel((0, 0))
        hex_color = f"#{r:02X}{g:02X}{b:02X}"
        self.label.setText(hex_color)
        self.move(pos.x() + 20, pos.y() - 20)

    def mousePressEvent(self, event):
        pyperclip.copy(self.label.text())

def main():
    app = QtWidgets.QApplication(sys.argv)
    picker = ColorPickerBubble()
    picker.resize(100, 30)
    picker.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
