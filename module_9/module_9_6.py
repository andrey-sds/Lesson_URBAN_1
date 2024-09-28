def all_variants(text):
    yield from text
    i = 0

    while i <= len(text):
        yield text[i] + text[i+1]
        if i+1 == len(text)-1:
            yield text
            break
        else:
            i += 1


a = all_variants("abc")
for i in a:
    print(i)
