import unittest
import Complex
import Methods
import math


class MyTestCase(unittest.TestCase):

    #RIGHT principle
    def test_sum(self):
        self.assertEqual(Methods.sum(6, 11), 17)

    def test_diff(self):
        self.assertEqual(Methods.difference(10, 6), 4)

    def test_remainder(self):
        self.assertEqual(Methods.remainder(10, 3), 1)

    def test_divide(self):
        self.assertEqual(Methods.division(120, 5), 24)

    def test_phoneValidator(self):
        self.assertEqual(Methods.phoneValidator("+40775315489"), True)

    def test_rangedListFabric(self):
        expected_result = len(Methods.rangedListFabric(4))
        self.assertEqual(expected_result, 4)

    def test_selection_sort(self):
        expected_list = Methods.selection_sort(5)
        ok = False
        for i in range(len(expected_list)-1):
            if expected_list[i] > expected_list[i+1]:
                ok = True
        self.assertEqual(False, ok, "List is not sorted")

    def test_quick_sort(self):
        expected_list = Methods.random_generator_and_quicksort(8)
        ok = False
        for i in range(len(expected_list)-1):
            if expected_list[i] > expected_list[i+1]:
                ok = True
        self.assertEqual(False, ok, "List is not sorted")

    def test_random_list_generator(self):
        list = Methods.random_list_generator(10)
        ok = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                ok = False
        self.assertEqual(False, ok, "List was generated already sorted")

    def test_complex_sum(self):
        self.assertEqual(Complex.sumComplex_numbers(Complex.Complex(2, 4), Complex.Complex(3, 1)), Complex.Complex(5,5).fullnumber(), "Not equal sum")

    def test_complex_difference(self):
        self.assertEqual(Complex.subComplex_numbers(Complex.Complex(2, 10), Complex.Complex(4, -10)), Complex.Complex(-2,20).fullnumber(), "Not equal difference")

    def test_complex_modulus(self):
        self.assertEqual(Complex.modulusComplex_numbers(), 6, "Not equal modulus of complex number")


    #Boundary testing

    def test_boundary_diff(self):
        self.assertEqual(Methods.remainder(11, 1), 0)

    def test_boundary_divide(self):
        self.assertEqual(Methods.division(11, 1), 11)


    #Inverse testing

    def test_inverse_sum(self):
        expected_sum = Methods.sum(5,2)
        param1 = Methods.difference(Methods.sum(5,2), 2)
        self.assertEqual(param1, 5)

    def test_inverse_diff(self):
        # expected_diff = Methods.difference(10, 7)
        param1 = Methods.sum(Methods.difference(10, 7), 7)
        self.assertEqual(param1, 10)

    def test_inverse_remainder(self):
        remainder = Methods.remainder(10, 5)
        div = Methods.division(10, 5)
        self.assertEqual(div*5+remainder, 10)

    def test_inverse_divider(self):
        remainder = Methods.remainder(10,5)
        div = Methods.division(10, 5)
        self.assertEqual((10-remainder)/div, 5)

    #calculated by modulus
    def test_complex_inverse_sum(self):
        obj1 = Complex.Complex(-4, 5)
        obj2 = Complex.Complex(10, -2)
        sum = obj1 + obj2
        expected_param = (sum - obj2).fullnumber()
        self.assertEqual(expected_param, Complex.Complex(-4,5).fullnumber())

    #calculated by modulus
    def test_complex_inverse_diff(self):
        obj1 = Complex.Complex(4, 7).modulus()
        obj2 = Complex.Complex(2, 10).modulus()
        diff = obj1 - obj2
        expected_param = obj1 - diff
        self.assertEqual(expected_param, Complex.Complex(2, 10).modulus())

    #rounding may be an issue here
    def test_complex_modulus_(self):
        obj = Complex.Complex(2, 10)
        result = obj.modulus()
        real = obj.real
        img = obj.img
        expected_param = math.ceil(math.sqrt(pow(result, 2) - pow(real, 2)))
        self.assertEqual(img, expected_param)


    #Cross-check testing

    def test_sorting_methods(self):
        list = Methods.random_list_generator(10)
        list_selection = Methods.selection_sort_list(list)
        list_quick = Methods.quick_sort_list(list)
        self.assertEqual(list_selection, list_quick, "Did not obtain the same result")


    #Error condition testing

    def test_error_remainder(self):
        self.assertRaises(Exception, Methods.remainder(1,0))
        # the_exception = context.exception
        # self.assertEqual("Divisor is less than 1" in context.exception)

    def test_error_divider(self):
        self.assertRaises(Exception, Methods.division(10,0))


    #Performance testing

    def test_performance_timing_sort(self):                             # ----- can be performed on both quick and selection sort methods
        self.assertGreater(Methods.timer_function(20), 0.00001)


    # def test_error_file(self):
    #     self.assertEqual(RuntimeError, )



    #CORRECT principles

    # Conformance principle

    def test_conformance_sum(self):                         # ------ sum of integer numbers only
        self.assertIsInstance(Methods.sum(3, 5), int)

    def test_conformance_diff(self):                              # ----- diff of integer numbers only
        self.assertIsInstance(Methods.difference(5, 2), int)

    def test_conformance_remainder(self):                           # ------ remainder is rounded to int
        self.assertIsInstance(Methods.remainder(5, 1), int)

    def test_conformance_lower_bound(self):                         # ----- lowest element in list is bigger than 10
        self.assertGreater(min(Methods.random_list_generator(10)), 10)

    def test_conformance_higher_bound(self):                        # ------ highest element in list is lower than 100
        self.assertGreater(100, max(Methods.random_list_generator(10)))



if __name__ == '__main__':
    print("test")
    unittest.main()
