#!/usr/bin/python3
import sys


def check_name_list(name_list):
    # fail here if the name list is bad or unsupported
    single_name = False
    triple_name = False
    bad_name = False
    for name in name_list:
        check = name.split()
        if len(check) == 1:
            single_name = True
        if len(check) == 3:
            triple_name = True
        if len(check) > 3:
            bad_list = True

    if single_name or triple_name or bad_name:
        print("Name list unsupported")
        print("Contains the following:")
        if single_name:
            print("\t- One-string name.")
        if triple_name:
            print("\t- Three-string name.")
        if bad_name:
            print("\t- Names with more than three strings.")

        exit()
    

    return


def generate_names_from_name(name):
    name_split = name.split()
    first = name_split[0]
    last = name_split[1]
    f = first[0]
    l = last[0]
   
    F = f.upper()
    L = l.upper()
    First = F + first[1:]
    Last = L + last[1:]

    gen = []

    gen.append(first + last)
    gen.append(first + '.' + last)
    gen.append(last + first)
    gen.append(last + '.' + first)
    gen.append(f + last)
    gen.append(f + '.' + last)
    gen.append(l + first)
    gen.append(l + '.' + first)

    gen.append(First + Last)
    gen.append(First + '.' + Last)
    gen.append(Last + First)
    gen.append(Last + '.' + First)
    gen.append(F + Last)
    gen.append(F + '.' + Last)
    gen.append(L + First)
    gen.append(L + '.' + First)
 

    return gen

def generate_combinations(name_list):
    check_name_list(name_list)
    generated_list = []

    for name in name_list:
        gen = generate_names_from_name(name) 
        for n in gen:
            generated_list.append(n)
   
    return generated_list

def get_natural_names(file_name):
    name_list = []
    name_file = open(file_name, 'r')

    for name in name_file:
        if name != '':
            name_list.append(name.lower())
     
    return name_list

def main():
    name_list = get_natural_names(sys.argv[1])
    generated_list = generate_combinations(name_list)
    for gen in generated_list:
        print(gen)
    return


if __name__ == "__main__":
    main()
