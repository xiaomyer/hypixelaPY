class NoInputError(Exception):
    pass


class NoPlayerFoundError(Exception):
    def __init__(self, input_):
        self.input_ = input_


class NoAPIKeyError(Exception):
    pass
