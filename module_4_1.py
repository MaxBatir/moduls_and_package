from true_math import divide as dtrue
from fake_math import divide as dfake

result = dfake(24, 6)
result2 = dfake(24,0)
result3 = dtrue(55, 5)
result4 = dtrue(55, 0)
print(result)
print(result2)
print(result3)
print(result4)