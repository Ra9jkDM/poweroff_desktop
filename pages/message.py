from PyQt6.QtWidgets import  QMessageBox

def show_error_msg(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle("Ошибка")
    msg.setText(text)
    msg.exec()

def show_info_msg(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setWindowTitle("Сообщение")
    msg.setText(text)
    msg.exec()