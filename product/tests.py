from django.test import TestCase
from .models import Product, customerDetail


# Create your tests here.
 

class ModelTestCase(TestCase):


    def test_product_name(self):

        productobj = Product("suzuki","suzuki",100,"laptop image")
        self.assertEquals(productobj.product_name,"suzuki")

    def test_check_valid_format_of_code(self):
        codesobj = Product("suzuki","@adfs",'ma001',"laptop image")
        value=codesobj.check_valid_format_of_code,"ma001"
        self.assertTrue(value, True)
    
    def test_check_total_contact_list(self):
        listobj = customerDetail("suzuki","hetauda",30)
        value=listobj.check_total_contact_list, 30
        self.assertTrue(value,True)
    
    def test_check_customer_addresss_of_customer_for_delivery(self):
        contactobj = customerDetail("ujjwal","hetauda","hetauda")
        self.assertEqual(contactobj.customer_address,"hetauda")

    def test_check_valid_product_price(self):
        checkobj = Product("ujjwal","ram",100,"imagefield")
        value=checkobj.check_valid_product_price()
        self.assertFalse(value, True)