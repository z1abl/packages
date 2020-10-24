import unittest

UNIT = 3

sm = UNIT
md = UNIT*2
lg = UNIT*3

# as input takes order_size number in range 1-100
# returns dictionary "result" with packages type/quantity
# i.e. {'order_size': 32, 'small': 0, 'medium': 1, 'large': 3, 'bunch': 2}

def calculate_packaging(order_size):
    if not order_size:
        return 'Provide order number between 1-100.'
    if order_size > 100:
        return 'Max. order size is 100. Try again with lower number.'

    sm_qnt = 0
    md_qnt = 0
    lg_qnt = 0
    bunch_qnt = 0

    # 1-9
    if order_size <= sm:
        sm_qnt = 1
    elif sm < order_size <= md:
        md_qnt = 1
    elif order_size <= lg:
        lg_qnt = 1

    # 10-12
    elif lg < order_size <= md*2:
        md_qnt = 2
        bunch_qnt = 1

    # 13-17
    elif md*2 < order_size < lg*2:
        lg_qnt = 2
        bunch_qnt = 1

    # 18-100
    elif order_size >= md * 2:
        floor = order_size // lg
        remainder = order_size % lg

        lg_qnt = floor

        if remainder > md:
            lg_qnt+=1

        if remainder:
            if remainder <= sm:
                sm_qnt = 1
            elif remainder <= md:
                md_qnt = 1

        bunch_qnt = lg_qnt - 1 if sm_qnt or md_qnt else lg_qnt - 2

    result = {
        'order_size': order_size,
        'small': sm_qnt,
        'medium': md_qnt,
        'large': lg_qnt,
        'bunch': bunch_qnt
    }

    print(result)
    return result

class Test(unittest.TestCase):
   def test_calculate_packaging(self):
      self.assertEqual(calculate_packaging(1),{'order_size': 1, 'small': 1, 'medium': 0, 'large': 0, 'bunch': 0})
      self.assertEqual(calculate_packaging(3),{'order_size': 3, 'small': 1, 'medium': 0, 'large': 0, 'bunch': 0})
      self.assertEqual(calculate_packaging(9),{'order_size': 9, 'small': 0, 'medium': 0, 'large': 1, 'bunch': 0})
      self.assertEqual(calculate_packaging(10),{'order_size': 10, 'small': 0, 'medium': 2, 'large': 0, 'bunch': 1})
      self.assertEqual(calculate_packaging(17),{'order_size': 17, 'small': 0, 'medium': 0, 'large': 2, 'bunch': 1})
      self.assertEqual(calculate_packaging(21),{'order_size': 21, 'small': 1, 'medium': 0, 'large': 2, 'bunch': 1})
      self.assertEqual(calculate_packaging(24),{'order_size': 24, 'small': 0, 'medium': 1, 'large': 2, 'bunch': 1})
      self.assertEqual(calculate_packaging(29),{'order_size': 29, 'small': 1, 'medium': 0, 'large': 3, 'bunch': 2})
      self.assertEqual(calculate_packaging(31),{'order_size': 31, 'small': 0, 'medium': 1, 'large': 3, 'bunch': 2})
      self.assertEqual(calculate_packaging(36),{'order_size': 36, 'small': 0, 'medium': 0, 'large': 4, 'bunch': 2})

if __name__ == '__main__':
    calculate_packaging(30)
    # unittest.main()
