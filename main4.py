def func(*args):
    def _():
        print(*args)

        func.args = _.args = (1, 2, 3)
        return _
        func(1, 2)()