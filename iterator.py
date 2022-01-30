class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num +=1

            return val
        else:
            raise StopIteration 

obj = TopTen()

# print(obj.__iter__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

print(next(obj))
print(next(obj))
for i in obj:
    print(i)


