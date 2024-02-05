from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel

def create_title(text):
    label = QLabel(text)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    font = label.font()
    font.setPixelSize(30)
    label.setFont(font)
    return label

def create_image(image_path: str, size: QSize):
        image = QLabel()
        pixmap = _create_pixmap(image_path, size)
        image.setPixmap(pixmap)
        return image

def _create_pixmap(img_path, size: QSize):
        pixmap = QPixmap(img_path)
        return pixmap.scaled(size, Qt.AspectRatioMode.KeepAspectRatio)