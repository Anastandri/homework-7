cook_book = {}
with open('cook-book.txt', encoding='utf-8') as src_file:
    last_key = ''
    for line in src_file:
        line = line.strip()
        if line.isdigit():
            continue
        elif line and '|' not in line:
            cook_book[line] = []
            last_key = line
        elif line and '|' in line:
            name, qt, msure = line.split(" | ")
            cook_book.get(last_key).append(dict(ingredient_name=name, quantity=int(qt), measure=msure))
 
print(cook_book)