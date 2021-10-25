# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# import time - for method8
import Complex
import Methods



if __name__ == "__main__":

    obj1 = Complex.Complex(2, -5)
    obj2 = Complex.Complex(3, 10)

    def switchMethod(argument):

        switcher = {
            1: Methods.sum(122, 2),       #return int method
            2: Methods.remainder(11, 5),       #return double method
            3: Methods.method3(),           #read from a file and display   TODO - sum numbers from a file
            4: Methods.phoneValidator("+40 712312315"),        #parsing
            5: Methods.rangedListFabric(4),                      #works with values from a range
            6: Methods.selection_sort(5),                       #poor method of sorting
            7: Methods.random_generator_and_quicksort(6),                     #better method to sort
            8: 'processing time-method8',               #writes 2kk values in a file -> takes some time or processing
            9: Methods.random_list_generator(10),               #method that obtains a random list
            10: Complex.sumComplex_numbers(),                                #method that sums up 2 Complex numbers
            11: Complex.subComplex_numbers(),                              #method that substracts 2 Complex numbers
            12: Complex.modulusComplex_numbers(),                             #method that calculates modulus of a Complex number
            13: 'est'

        }
        func = switcher.get(argument, "Invalid choice")
        print(func)

    #write numbers in a file ---> this function will take longer
    # def method8():
    #     start = time.time()
    #     f = open("tests.txt", "w")
    #     for i in range(0,20000000):
    #         f.write(str(i))
    #     f.close()
    #     end = time.time()
    #     return (str(end - start) + " seconds")


#format the + or - signs and display 2 Complex numbers    ---> used to test the fullnumber() method
    # def sumComplex():
    #     obj1 = complex_class_factoring(2, -10)
    #     obj2 = complex_class_factoring(-5, 13)
    #     return obj1.fullnumber() + "\n" + obj2.fullnumber()


    while(input):
        try:
            mode = int(input("\n1-Sum\n2-Diff\n3-Sum from file\n4-Phone Validator\n5-Ranged list fabric\n6-Selection sort\n7-Quick sort\n8-in progress\n9-Random list fabric\n10-Sum 2 complex numbers\n11-Substract 2 complex numbers\n12-Modulus of a complex number\nChoose a number: "))
            switchMethod(mode)

        except ValueError:
            print("Oooops try again but with a number this time -.-")



