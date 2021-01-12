def leiaDinheiro(txt):
    t = input(txt).strip()
    while True:
        if t.isnumeric() or '.' in t:
            return float(t)
        elif ',' in t:
            t = t.replace(',', '.')
            return float(t)
        print('\033[31mERRO! Digite somente valores.\033[m')
        t = input(txt).strip()
