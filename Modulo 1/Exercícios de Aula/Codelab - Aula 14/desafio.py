dic = {1: "João", 2: "Bete", 3: "Pedro", 1: "Solange"}

print (dic[1])
import collections
print([item for item, count in collections.Counter(dic).items() if count > 1])