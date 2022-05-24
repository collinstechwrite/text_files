```python
import random
trade_data = []

#https://www.adamsmith.haus/python/answers/how-to-iterate-through-the-lines-of-a-file-in-python
with open("historicADA.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    stripped_line = float(stripped_line)
    trade_data.append(stripped_line)
    print(stripped_line)

random.shuffle(trade_data)
print(trade_data)
```
