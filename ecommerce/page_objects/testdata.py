class TestData():
    #--account login--
    BASE_URL = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    INDEX_PAGE_URL = "http://automationpractice.com/index.php"
    DRESS_URL = "http://automationpractice.com/index.php?id_product=5&controller=product&search_query=dress&results=7"
    new_email="testing2@ecommercetstngstester.com"
    password = "test1234"
    email = "test@ecommercetesting2.com"


    #--account creation--
    first_name = "test fn"
    last_name = "test ln"
    address = "3121 test Ln"
    city = "testCity"
    state = "Maryland"
    postcode = "21040"
    mobile_phone = "111111111"
    country = "United States"
    alias = "test"
    invalid_email = "test1@test"

    invalid_email_set = [("test@test", "test123"),("test.com","test123"),]

    #--browse categories--
    browse_categories = ["TOPS\nT-shirts\nBlouses", "DRESSES\nCasual Dresses\nEvening Dresses\nSummer Dresses"]
    search_list_results = ["Summer Dresses > Printed Summer Dress","Evening Dresses > Printed Dress","Summer Dresses > Printed Summer Dress",
                           "Summer Dresses > Printed Chiffon Dress","Casual Dresses > Printed Dress","T-shirts > Faded Short Sleeve T-shirts",
                           "Blouses > Blouse"]
    address_list = ['YOUR DELIVERY ADDRESS', 'test fntest fn test lntest ln', '3121 test Ln',
                    'testCity, Maryland 21040', 'United States', '111111111']
    ship_list = ['YOUR BILLING ADDRESS', 'test fntest fn test lntest ln', '3121 test Ln',
                    'testCity, Maryland 21040', 'United States', '111111111']