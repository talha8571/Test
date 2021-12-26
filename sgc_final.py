from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium import webdriver
import time
import string
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
#from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner

class SGC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.Firefox(executable_path="D:\\SGC\\geckodriver.exe")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(20)
        cls.driver.get("https://dev-sgc-web.azurewebsites.net/")
        cls.driver.maximize_window()
        # cls.driver.find_element_by_xpath("/html/body/div[2]").click()#man icon
        # cls.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/a[3]").click()#man icon
        # cls.driver.find_element_by_xpath("/html/body/div[3]/div[6]/div[2]/div/div/div/span[1]").click()#man icon
        time.sleep(3)
        #cls.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/div/div[3]/a[2]").click()  # login button

    def test_a_invalidlogin(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/div/div[3]/a[2]").click()  # login button
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div[2]/div[1]/div/input").send_keys("makesr")
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/input").send_keys("fahfjh")
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div/div/button").click()  # login button
        time.sleep(2)
        time.sleep(3)
        s = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div/div/div[2]/div/div/span/span").text
        print(s)
        time.sleep(4)
        self.assertEqual('WRONG USERNAME OR PASSWORD.','WRONG USERNAME OR PASSWORD.',"message not correct")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div[2]/div[1]/div/input").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div[2]/div[1]/div/input").send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/input").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/input").send_keys(Keys.CONTROL + "A", Keys.BACKSPACE)
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div[2]/div[1]/div/input").send_keys("Muhammad_Talhah")
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/input").send_keys("box1234...")
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div/div/button").click()  # login button

    def test_b_StartNewSubmission(self):
        self.driver.implicitly_wait(10)
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/app-dashboard/div[1]/div/div/div/div[2]/a").click()  # start new submission
        self.driver.find_element_by_xpath("/html/body/sgc-web/sgc-modal/div/div/terms-alert/div/label/span").click()  # terms and conditions
        self.driver.refresh()
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-expertise-tier/div/div/div/h3").click()  # start your order

    def test_c_Search(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[1]/div/input").send_keys("makro")
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[1]/div/input").clear()
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[1]/div/input").send_keys("jordan")

    def test_d_ddingCard(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[1]/p/a").click()  # click to add your card

    def test_e_DeclareValue(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys("1300")  # declared value
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/h3").click()  # click on jordan heading
        time.sleep(4)
        sf = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/checkout-side-bar/div/div[7]/p").text
        print("the sf is", sf)
        time.sleep(3)
        self.assertEqual(sf, '$30.00', 'not matched')  # price matching
        self.driver.execute_script("window.scrollTo(0,200)")

    def test_f_ovoersizedtiems(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[4]/label[2]/span").click()  # oversized items
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next
        self.driver.refresh()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    def test_g_serviceplan(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div").click()  # service plan
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next
        time.sleep(2)
        sf = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/checkout-side-bar/div/div[7]/p").text
        print(sf)
        time.sleep(2)
        self.assertEqual(sf, '$250.00', 'not correct')
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()
        pp = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/div").text
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next
        time.sleep(2)

    def test_h_shippingMethod(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-shipping/div/div/div[3]/div[1]").click()  # FedEx International Economy Air
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next
        time.sleep(2)
        sf = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/checkout-side-bar/div/div[7]/p").text
        print("sf is ",sf)
        time.sleep(2)
        self.assertEqual(sf, '$250.00', 'not correct')
        # #eg = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/div").text
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-shipping/div/div/div[3]/div[1]").click()  # FedEx International Economy Air
        fedex = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/checkout-side-bar/div/div[8]/p").text
        print(fedex)
        time.sleep(2)
        self.assertEqual(fedex, '$60.00', 'fedex price is not correct')
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next

    def test_i_promoCOde(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/checkout-side-bar/div/div[3]/input").send_keys("sgcfulldiscount")  # promo
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/checkout-side-bar/div/div[3]/button").click()  # apply
        time.sleep(2)
        total = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/checkout-side-bar/div/div[8]/p/b").text
        print(total)
        self.assertEqual(total, '$0.00', 'not applied')

    def test_j_ZZcompletion(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/checkout-side-bar/div/div[9]/button").click()#click here to finish
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/sgc-web/sgc-modal/div/div/app-payment-terms/div/label/span").click()  # checkbox
        time.sleep(2)
        #self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/checkout-side-bar/div/div[9]/button").click()  # submit nad pay later
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/checkout-side-bar/div/div[10]/button").click()  # submit and pay later
        time.sleep(2)
        ss = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/order-placed/section/h2").text
        print(ss)
        self.assertEqual(ss, 'THANK YOU FOR YOUR SUBMISSION!', 'please correct the flow')
        time.sleep(3)

    def test_k_ZZZcardgrading(self):
        self.driver.implicitly_wait(10)
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div[2]/div[1]/div/input").send_keys("Muhammad_Talhah")
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/input").send_keys("box1234...")
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div/div/button").click()  # login button
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/div/ul/li[1]/a").click()#card grading
        self.driver.execute_script("window.scrollTo(0,200)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(200,400)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(400,200)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(400,800)")

    def test_l_popupreport(self):
        self.driver.implicitly_wait(10)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/div/ul/li[2]/a").click()#popup report

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__=='__main__':
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Rameez\\PycharmProjects\\Latharan\SampleProject\\reports'))

  #testRunner = HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\P.T\\PycharmProjects\\pythonProject\\Reports'