
class FlexibleDict(dict):
    def __getitem__(self, i):
        try :
            if i in self:
                return super().__getitem__(i)
            elif str(i) in self:
                return super().__getitem__(str(i))
            elif int(i) in self:
                return super().__getitem__(int(i))
        except ValueError:
            raise ValueError

fd = FlexibleDict({1: 100500, '2': '100500'})

print(fd['1'])
print(fd[2])
