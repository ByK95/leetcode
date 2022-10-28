class Test:
    @staticmethod
    def load_from_file(filename):
        with open(f"./{filename}", 'r') as f:
            return f.read()

    @classmethod
    def run(cls):
        instance = cls()
        methods = [method for method in dir(instance) if method.startswith('test')]
        for method in methods:
            func = getattr(instance, method)
            func()


class Solution(Test):
    pass


if __name__ == '__main__':
    Solution.run()