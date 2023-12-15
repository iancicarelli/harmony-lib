class Album:
    def __init__(self, id, name, publish_date):
        self.id = id
        self.name = name
        self.publish_date = publish_date
        self.songs = []