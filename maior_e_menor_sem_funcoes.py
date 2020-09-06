def maior_e_menor(um,dois,tres,quatro,cinco):
    if um > dois and um>tres and um>quatro and um>cinco:
        print(f'{um}')
        if dois<um and dois<tres and dois<quatro and dois<cinco:
            print(f'{dois}')
        if tres<um and tres<dois and tres<quatro and tres<cinco:
            print(f'{tres}')
        if quatro<um and quatro<dois and quatro<tres and quatro<cinco:
            print(f'{quatro}')
        if cinco<um and cinco<dois and cinco<tres and cinco<quatro:
            print(f'{cinco}')
    elif dois>um and dois>tres and dois>quatro and dois>cinco:
        print(f'{dois}')
        if um<dois and um<tres and um<quatro and um<cinco:
            print(f'{um}')
        if tres<um and tres<dois and tres<quatro and tres<cinco:
            print(f'{tres}')
        if quatro<um and quatro<dois and quatro<tres and quatro<cinco:
            print(f'{quatro}')
        if cinco<um and cinco<dois and cinco<tres and cinco<quatro:
            print(f'{cinco}')
    elif tres>um and tres>dois and tres>quatro and tres>cinco:
        print(f'{tres}')
        if um<dois and um<tres and um<quatro and um<cinco:
            print(f'{um}')
        if dois<um and dois<tres and dois<quatro and dois<cinco:
            print(f'{dois}')
        if quatro<um and quatro<dois and quatro<tres and quatro<cinco:
            print(f'{quatro}')
        if cinco<um and cinco<dois and cinco<tres and cinco<quatro:
            print(f'{cinco}')
    elif quatro>um and quatro>dois and quatro>tres and quatro>cinco:
        print(f'{quatro}')
        if um<dois and um<tres and um<quatro and um<cinco:
            print(f'{um}')
        if dois<um and dois<tres and dois<quatro and dois<cinco:
            print(f'{dois}')
        if tres<um and tres<dois and tres<quatro and tres<cinco:
            print(f'{tres}')
        if cinco<um and cinco<dois and cinco<tres and cinco<quatro:
            print(f'{cinco}')
    elif cinco>um and cinco>dois and cinco>tres and cinco>quatro:
        print(f'{cinco}')
        if um<dois and um<tres and um<quatro and um<cinco:
            print(f'{um}')
        if dois<um and dois<tres and dois<quatro and dois<cinco:
            print(f'{dois}')
        if tres<um and tres<dois and tres<quatro and tres<cinco:
            print(f'{tres}')
        if quatro<um and quatro<dois and quatro<tres and quatro<cinco:
            print(f'{quatro}')
def main():
    um=int(input(''))
    dois=int(input(''))
    tres=int(input(''))
    quatro=int(input(''))
    cinco=int(input(''))
    maior_e_menor(um,dois,tres,quatro,cinco)
if __name__=='__main__':
    main()
