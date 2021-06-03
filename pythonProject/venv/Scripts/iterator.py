interable_value = "Nidhi"

iterable_obj = inter(interable_value)

while True:
    try:
        item = next(iterable_obj)
        print(item)
    except StopIteration:
        break
