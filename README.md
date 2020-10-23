
I used PyTest framework with Selenium WebDriver to automate the eCommerce site. Please follow the virtual environment and PyCharm setup details in order to run the tests.

# Prerequisites for Selenium testing with Python & PyTest:
For using the PyTest framework, Python needs to be installed on the machine from here: https://www.python.org/downloads/. I have used the latest version Python 3.9.0. 

Since PyTest will be used for automated browser testing, Selenium WebDriver for the browser under test needs to be installed. I used chrome driver for my tests.

It is important to create a virtual environment and activate it before doing any test. The details to create a virtual environment is described below and can also be found here:
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/ 


1.Setup the pip package manager:
Check to see if your Python installation has pip. 
Enter the following in your terminal:pip -h,If you see the help text for pip then you have pip installed, otherwise download and install pip. 
 
2.Install the virtualenv package:
The virtualenv package is required to create virtual environments. You can install it with pip: pip install virtualenv

3.Create the virtual environment:
To create a virtual environment, you must specify a path. For example, to create one in the local directory called ‘mypython’, type the following:
virtualenv mypython

4.Activate the virtual environment:
You can activate the python environment by running the following command:

Mac OS / Linux:source mypython/bin/activate

Windows:mypthon\Scripts\activate

You should see the name of your virtual environment in brackets on your terminal line e.g. (mypython).


I used PyCharm IDE for all my Automation tests, Page objects etc. You will need to configure the project interpreter. Some helpful links are below:
https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#packages


## Test Coverage area:
The following are the areas that have the coverage: 
•	Account creation 
•	Login 
•	Browsing the store’s main categories (Women, Dresses, T-shirts) 
•	Searching for clothing items 
•	Sharing an item via social media 
•	Shopping cart 
•	Checkout 


We start with making class for each of these pages. We will create a Base Page class which all of these page classes would inherit. After doing that, next task would be to put the locators and methods related to different pages in their respective classes. There are two approaches to maintain the locators. First is keeping all the locators specific to a page in its own class and the other is to keep locators of all pages at a common place. I found that it is better to put locators in its own page class for ease of tracking. After the page classes, locators and test data are in place, the next task would be of writing the test scripts/cases.

Executing the PyTest command (without mentioning a filename) on the terminal will run all the Python files that have filenames starting with ‘test_*’ or ending with ‘*_test’. These files are automatically identified as test files by the PyTest framework. The framework also mandates that the test methods should start with ‘test’, else the method will not be considered for execution. 

Also, I kept all the test data like URL of the application, search term etc., in a separate TestData file. This will help us change the TestData and retest to make sure the scripts work fine with different sets of test data. One improvement here could be putting all the test data in a .json file in AWS s3 bucket and download from there dynamically when the tests run so that larger test data will not consume a lot of space locally.

I used ‘Implicit Wait’ in script that would wait while searching for any web element on the page, and also explicit wait to explicitly wait for an element or a condition to happen, for example: WebDriverWait and Expected_Conditions.


## Framework Setup:
I have the main folder eCommerce. Under that I have the sub folders automation_ui, automation_api, pageobejcts, helpers and conftest.py file. The UI test cases are under automation_ui. The page objects are under the file page_objects. The fixtures are in conftest.py and the api test cases in future can be put under automation_api: this folder is empty now. There is also a folder called helpers, which can be used to put any helper method for api and ui tests. 

base_page.py: Base Page Class is the one from which classes of all other pages inherit. We will therefore create it first, populate it with methods for the most common actions that are expected to be performed on any page in the application.

login_page.py: All the locators and methods that are used by login and account creation can be found here.

product_details.py: All the product’s locators and methods can be added to this page. Some of the locators and method that are used to tests the products are added to this page.

browse_categories.py: All the search related locators and browse results etc. are put together in this page.

carts_page.py: The shopping cart locators and methods and payment details etc. are added to this page.

testdata.py: The test data that are used in the tests are added to this page. As an improvement, it is possible to either add the test data as a .json file and load to test or better yet add it in AWS S3 bucket and download dynamically for the tests to avoid the burden on the framework.

Conftest.py: All fixtures used by the tests can be put in conftest.py that can be called by tests. My tests uses the fixture chrome_driver_init() that will create the `driver`, using ChromeDriverManager() to download and install chrome and we will close the browser at the end of the test. Alternatively, you can also download and pass the chromedriver executable path to webdriver.Chrome() method. 


## Tests walkthrough:
Step 1. The necessary modules are imported, namely PyTest, Selenium, time, classes etc.

Step 2. Using the fixture: chrome_driver_init(),the Chrome WebDriver is instantiated. The test then creates an instance of the class and in the class __init__() method the URL is passed using the .get method in Selenium.

Once the web elements are located using the appropriate Selenium methods [i.e. find_element_by_name(), find_element_by_id()], necessary operations [i.e. click(), etc.] are performed on those elements.


Command to run tests:
•	py.test  filename_to_run/directory_to_run
  •	py.test  ecommerce/automaiton_ui/test_login.py
•	You can also run a specific test under a class:
  •	pytest test_file.py::TestClass::test_method


## Potential Options/Improvements:

•	Putting test data in .json file and move them to aws/s3 bucket or dynamic loading
•	Automation for api functionality is not added as of now but can be a great addition as the api tests runs faster and hence reduces the time taken by UI tests and their timeouts. UI tests, depending on how fast the browser loads and detects locator, can sometimes result in timeouts and will need more maintenance to fix those failures. As of now time.sleep, implicit and explicit waits etc. handle that to some extent. 

•	I see that there are a number of test scenarios that can be automated for each of the pages that I worked on. Because of time constraints I had to cut short to cover the basic functionality/happy path testing for the scenarios that I need to cover. But I did include some negative scenarios using parametrize to demonstrate how we can add some negative tests for test_login.py. Every test can have classes for positive and negative scenarios so as to make sure that we cover all the possible functionalities and to ensure they work as expected. 

•	test_browsing_categories.py is hovering over and browsing all the main categories but those categories have multiple links that can be automated to make sure they work as expected. 

•	test_search.py is searching only one item for the test. However, it can be parametrized to search for many items. It can also be checked for their click function to make sure those items can be browsed, the lists of items are viewable and can perform additional functionalities on it, to name few. Additionally, grid, list layout, sorting functionality, top sellers and the filters etc. can also be tested.

•	test_add_to_cart.py: I have automated the functionality from user’s perspective that they come to site, browse and then add item to cart for checkout. It can also be automated as they sign in, browse and checkout. A few more items from multiple images and links can be automated to verify that they can be added to cart.

•	Cart has additional functionalities like add count, delete count etc. which I verified. This can be designed as a test on its own to make sure each item’s price varies when we add or delete or modify. The shipping tab can have additional tests to make sure that it verifies the shipping charge, type etc. The address tab can also be tested to verify adding of new addresses/update etc.

•	The payment tab can have multiple tests to cover different payment methods.

•	I have covered all the tests with their main functionalities, however there are areas that can improve the test coverage and design lot more scenarios as I mentioned above.

In summary, there are a number of pages like contact, header, footer links and my account functions and many more that can be automated when needed. 


## Test results:


====================================== test session starts =========================================================
platform darwin -- Python 3.9.0, pytest-6.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /Users/guest/PycharmProjects/test_python
collected 8 items                                                                                                                                                                                                 

ecommerce/automaiton_ui/test_add_to_cart.py .                                                                                                                                                               [ 12%]
ecommerce/automaiton_ui/test_browsing_categories.py .                                                                                                                                                       [ 25%]
ecommerce/automaiton_ui/test_login.py .....                                                                                                                                                                 [ 87%]
ecommerce/automaiton_ui/test_search.py .                                                                                                                                                                    [100%]

========================================================================================== 8 passed in 845.53s (0:14:05)===









