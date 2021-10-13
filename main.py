def show_menu():
    print('1. Citire lista')
    print('2. Determinare cea mai lunga subsecventa cu proprietatea 6')
    print('3. Determinare cea mai lunga subsecventa cu proprietatea 18')
    print('4. Iesire')
def read_list():
    lst=[]
    lst_str=input('Dati numerele separate prin spatiu: ')
    lst_str_split= lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst
def desc(n):
    '''
    Determina daca un nr. are cifrele in ordine descrescatoare
    param: n- nr intreg
    return: True/False daca indeplineste sau nu conditia
    '''
    while n>9:
        if n//10%10<n%10:
            return False
        n//=10
    return True
def get_longest_digit_count_desc(lst: list[int])->list[int]:
    '''
    Determina cea mai lunga subsecventa in care numarul de cifre este in ordine descrescatoare.
    param list: lista de numere
    return: o lista cu subsecventa ceruta
    '''
    n=len(lst)
    result=[]
    for st in range(n):
        for dr in range(st,n):
            digit_count_desc=True
            for num in lst[st:dr+1]:
                if desc(num)==0 :
                    digit_count_desc=False
                    break
            if digit_count_desc:
                if dr-st+1>len(result):
                 result= lst[st:dr+1]
    return result
