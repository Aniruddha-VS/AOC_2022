with open("data_prod.txt") as data:
    ##Read data
    input_text = data.read()

## Part 1
for idx in range(len(input_text) -3):
    if len(set(input_text[idx:idx+4])) == 4:
        print(idx+4)
        break

## Part 2
for idx in range(len(input_text) -13):
    if len(set(input_text[idx:idx+14])) == 14:
        print(idx+14)
        break