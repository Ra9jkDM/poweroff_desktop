import business_logic.general_storage as Storage
from pages.message import show_info_msg, show_error_msg

storage = Storage.Storage()

def shutdown():
    try:
        storage.requests.get("power/shutdown")
        show_info_msg("Выключение сервера")
    except:
        show_error_msg("Возникла ошибка при попытке выключения")

def reboot():
    try:
        storage.requests.get("power/reboot")
        show_info_msg("Перезагрузка сервера")
    except:
        show_error_msg("Возникла ошибка при попытке перезагрузки")