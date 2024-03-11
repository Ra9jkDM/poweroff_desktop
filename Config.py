import json

CONFIG_PATH = "config.json"

class Config:
    def __init__(self):
        self.load_config(CONFIG_PATH)
        self._api_id = 0

    def load_config(self, path):
        with open(path) as f:
            text = f.read()
            obj = json.loads(text)
            
            self._image_path = obj["imagePath"]
            self._apis = obj["api"]


    @property
    def _api(self):
        return self._apis[self._api_id]

    @property
    def image_path(self):
        return f"{self._image_path}{self._api['image']}"

    @property
    def url(self):
        return self._api["api"]   

    @property
    def name(self):
        return self._api["name"]
        
    @property
    def api_names(self):
        return [i["name"] for i in self._apis]

    @property
    def api_id(self):
        return self.api_id

    @api_id.setter
    def api_id(self, value):
        if value < 0 or value > len(self._apis):
            raise Exception("API list out of range")

        self._api_id = value

if __name__ == "__main__":
    c = Config()
