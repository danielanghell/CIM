# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# import time - for method8
import Complex
import Methods


if __name__ == "__main__":

    obj1 = Complex.Complex(2,-5)
    obj2 = Complex.Complex(3,10)

    def switchMethod(argument):

        switcher = {
            1: Methods.method1(15,2),       #return int method
            2: Methods.method2(10,5),       #return double method
            3: Methods.method3(),           #read from a file and display
            4: Methods.method4("+40 712312315"),        #parsing
            5: Methods.method5(4),                      #works with values from a range
            6: Methods.selection_sort(5),                       #poor method of sorting
            7: Methods.random_generator_and_quicksort(6),                     #better method to sort
            8: 'processing time-method8',               #writes 2kk values in a file -> takes some time or processing
            9: Methods.random_list_generator(10),               #method that obtains a random list
            10: method9(),                              #method that returns object from Complex class
            11: method10(),                              #method that sums up 2 Complex numbers
            12: method11(),                              #method that substracts 2 Complex numbers
            13: method12()                              #method that calculates modulus of a Complex number

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


#fabric of Complex numbers
    def complex_class_factoring(real, img):
        obj = Complex.Complex(real, img)
        return obj

#format the + or - signs and display 2 Complex numbers
    def method9():
        obj1 = complex_class_factoring(2,-10)
        obj2 = complex_class_factoring(-5, 13)
        return obj1.fullnumber() + "\n" + obj2.fullnumber()

#add Complex numbers
    def method10():
        obj1 = complex_class_factoring(3,-5)
        obj2 = complex_class_factoring(-2, 10)
        return (obj1 + obj2).fullnumber()


#substract Complex numbers
    def method11():
        obj1 = complex_class_factoring(2,10)
        obj2 = complex_class_factoring(4,-10)
        return (obj1 - obj2).fullnumber()


#modulus of Complex numbers
    def method12():
        obj1 = complex_class_factoring(5,4)
        return obj1.modulus()




    while(input):
        try:
            mode = int(input("Choose a number: "))
            if mode == 1:
                switchMethod(1)

            elif mode == 2:
                switchMethod(2)

            elif mode == 3:
                switchMethod(3)

            elif mode == 4:
                switchMethod(4)

            elif mode == 5:
                switchMethod(5)

            elif mode == 6:
                switchMethod(6)

            elif mode == 7:
                switchMethod(7)

            elif mode == 8:
                switchMethod(8)

            elif mode == 9:
                switchMethod(9)

            elif mode == 10:
                switchMethod(10)

            elif mode == 11:
                switchMethod(11)

            elif mode == 12:
                switchMethod(12)

            elif mode == 13:
                switchMethod(13)

            else:
               print('shit')
        except ValueError:
            print("Oooops try again but with a number this time -.-")



