with open("oops.cpp", "w") as poop:
    poop.write("""
#include "oops.h"

bool isntOdd_ANDis_even(int help){
""")

with open("oops.cpp", "a") as myfile:
    # HERERERE!!!!
    bits = 32; #<<---- HEEEREEE YOU CAN BREAKE YOUR COMPUTER!!!! PUT AS BIG NUMBER AS YOU CAN


    i = 0
    max = pow(2, bits)
    print(max)

    progress = -1
    while i < max:
        help = round(100*(i/max), 1)
        if help > progress:
            print(f"\n{progress}%\nif counts:{i}/{max}")
            progress = help

        myfile.write("    if (help == " + str(i) + "){return " + str(i%2 == 0).lower() + ";}\n")
        i += 1
    myfile.write("    return false;\n}")
