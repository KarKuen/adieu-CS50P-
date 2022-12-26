def main():
    names = []
    while True:
        try:
            name = input()
            names.append(name)
        except EOFError:
            break
    adieu(names)

def adieu(names):
    if len(names) == 1:
        print('Adieu, adieu, to', names[0])

    elif len(names) == 2:
        print('Adieu, adieu, to ', end='')
        print(names[0], end=' and ')
        print(names[1])

    else:
        print('Adieu, adieu, to ', end='')
        for name in names:
            if name == names[-2]:
                print(name, end=', and ')
            elif name == names[-1]:
                print(name, end='\n')
            else:
                print(name, end=', ')

main()