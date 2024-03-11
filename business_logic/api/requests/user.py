import business_logic.general_storage as Storage
from pages.message import show_info_msg, show_error_msg
import json

storage = Storage.Storage()

def delete_tokens(tokens: list):
    try:
        storage.requests.post("login/delete", json.dumps({"tokens": tokens}))
    except:
        show_error_msg("Возникла ошибка при попытке удаления")

