def rotate(iterable, n=0):
    n = n or 0
    items = []
    if len(iterable):
        n = n % len(iterable)
        for item in iterable[-n:len(iterable)] + iterable[:-n]:
            items.append(item)
    return type(iterable)(items)
