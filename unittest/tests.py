import surfshop
import unittest

class tester(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboards(self):
    for i in range (1,5):
      with self.subTest(i=i):
        message = self.cart.add_surfboards(i)
        if i==1:
          self.assertEqual(message,
    'Successfully added 1 surfboard to cart!', 'Error adding 1 surboard')
        else: 
                self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
        self.cart = surfshop.ShoppingCart()

  #@unittest.skip
  def test_TooManyBoardsError(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards,5)

  @unittest.expectedFailure
  def test_apply_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

unittest.main()
