import unittest

from employee import Employee

class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('ola', 'pacia', 100)

        
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(5100, self.employee.yearly_income)

    def test_give_custom_raise(self):
        self.employee.give_raise(200)
        self.assertEqual(300, self.employee.yearly_income)

if __name__ =='__main__':
    unittest.main()


        