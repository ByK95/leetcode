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
    def test_numSteps_v1(self):
        # given
        s = "1101"

        # when
        result = self.numSteps_v1(s)

        # then
        assert result == 6

    def test_big_int2(self):
        pass
        # given
        s2 = "1111011110000011100000110001011011110010111001010111110001"

        # # when
        result = self.numSteps_v2(s)

        assert result == 85        

    def numSteps_v1(self, s: str) -> int:
        steps = 0
        number = int(s,2)

        while number > 1:
            steps+=1
            if number % 2 == 0:
                number /= 2
                continue
            
            number += 1

        return steps

    def numSteps_v2(self, s: str) -> int:
        steps = 0
        number_arr = [digit for digit in s]
        
        while True:
            size = len(number_arr) - 1

            if size == 0:
                break

            if number_arr[size] == '0':
                number_arr.pop()
                steps += 1
                continue
            
            while number_arr[size] == '1':
                number_arr[size] = '0'
                size = size - 1
            
            if size == -1:
                number_arr.insert(0, '1')
                steps += 1
                continue

            number_arr[size] = '1'
            size = size - 1
            
            steps += 1
        
        return steps

if __name__ == '__main__':
    Solution.run()