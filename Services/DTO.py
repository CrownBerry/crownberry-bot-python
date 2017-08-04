class DTO(dict):
    def __init__(self):
        pass

    def __getattr__(self, attr):
        return self[attr]