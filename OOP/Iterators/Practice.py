class EvenNumbers:
    def __iter__(self):
        self.n = 2
        return self
    
    def __next__(self):
        x = self.n
        self.n += 2
        return x
    
even = EvenNumbers()
it = iter(even)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))