class CheckImage:
    def __init__(self, image_inspect):
        self.image_inspect = image_inspect
        self.check_result = dict()

    def is_user_exists(self):
        user = self.image_inspect['Config']['User']
        if not user:
            self.check_result['Users'] = 'No user in image'
        return self.check_result

    def check_image(self):
        self.is_user_exists()
        return self.check_result
