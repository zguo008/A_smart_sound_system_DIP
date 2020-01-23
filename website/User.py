import config
import uuid
class User(object):
    def __init__(self, uid: str = None, request = None):
        self.id = uid if uid is not None else uuid.uuid4()
        self.audio_conf = config.default_control
        self.request = request

if __name__ == "__main__":
    user = User('123')
    print(user.audio_conf)
    print(user)