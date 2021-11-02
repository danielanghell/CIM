import phonenumbers
import random
import timeit

if __name__ == "__main__":
    print("executed as main")
else:

    #sum
    def sum(number1, number2):
        sum = number1 + number2
        return sum

    #rest
    def remainder(number1, number2):
        try:
        # if number2 < 0:
        #     raise ZeroDivisionError("Divisor is less than 1")
        # else:
            rest = number1 % number2
            return int(rest)
        except ZeroDivisionError:
            return "divisor is less than 1"


    #division
    def division(number1, number2):
        try:
            return int(number1 / number2)
        except ZeroDivisionError:
            return "divisor is less than 1"




    #difference
    def difference(number1, number2):
        diff = number1 - number2
        return diff

    #read from a file
    def method3():
        f=open("file.txt", "r")
        return f.read()


    #verify a string
    def phoneValidator(phone_number):
        phone_number_parsed=phonenumbers.parse(phone_number)
        return phonenumbers.is_possible_number(phone_number_parsed)


    #working with values from a defined range
    def rangedListFabric(number):
        list = [*range(int(number))]
        for i in list:
            list[i] = list[i]+10
        return list


    #poor sorting alghortim ----> selection sort
    def selection_sort(values):
        argument = random_list_generator(values)
        for i in range(len(argument)):
            min_idx = i
            for j in range(i + 1, len(argument)):
                if argument[min_idx] > argument[j]:
                    min_idx = j
            argument[i], argument[min_idx] = argument[min_idx], argument[i]
        return argument

    #poor sorting alghortim ----> selection sort -----> passing a list instead of value
    def selection_sort_list(list):
        argument = list
        for i in range(len(argument)):
            min_idx = i
            for j in range(i + 1, len(argument)):
                if argument[min_idx] > argument[j]:
                    min_idx = j
            argument[i], argument[min_idx] = argument[min_idx], argument[i]
        return argument


    def partition(start, end, array):
        # Initializing pivot's index to start
        pivot_index = start
        pivot = array[pivot_index]

        while start < end:
            while start < len(array) and array[start] <= pivot:
                start += 1
            while array[end] > pivot:
                end -= 1
            if (start < end):
                array[start], array[end] = array[end], array[start]
        array[end], array[pivot_index] = array[pivot_index], array[end]
        return end


    def quick_sort(start, end, array):
        if (start < end):
            p = partition(start, end, array)
            quick_sort(start, p - 1, array)
            quick_sort(p + 1, end, array)
        return array


    #generate random list and sort it with quicksort - no shit sherlock
    def random_generator_and_quicksort(argument):
        list = random_list_generator(argument)
        return quick_sort(0, len(list)-1, list)

    def random_list_generator(argument):
        list = random.sample(range(10, 100), argument)
        return list


    #measure time elapsed
    def timer_function(argument):
        start = timeit.timeit()
        random_generator_and_quicksort(argument)
        #selection_sort(argument)
        end = timeit.timeit()
        return start - end


    #pass a list as argument and sort with quicksort
    def quick_sort_list(list):
        return quick_sort(0, len(list)-1, list)
