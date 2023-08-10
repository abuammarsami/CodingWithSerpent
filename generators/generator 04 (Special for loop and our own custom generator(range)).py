def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            # print(iterator)
            print(next(iterator))

        except StopIteration:
            break


# special_for([1, 2, 3])


class MyGen():
    current = 0

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.end:
            num = MyGen.current
            MyGen.current += 1
            return num
        else:
            raise StopIteration


# That's how under need the hood the range function works.
gen = MyGen(0, 100)

# for i in gen:
#     print(i)

special_for(gen)
