import time
from models import Model


class Reply(Model):

    def __init__(self, form):
        self.id = None
        self.content = form.get('congent', '')
        self.ct = int(time.time())
        self.ut = self.ct
        self.topic_id = int(form.get('topic_id', ''))

    def user(self):
        from .user import User
        u = User.find(self.user_id)
        return u