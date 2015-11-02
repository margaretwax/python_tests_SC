


def do_login(driver):
    find_id = driver.find_element_by_id


    find_id("tbUser").clear()
    find_id("tbUser").send_keys("support@solidcommerce.com")
    find_id("tbPass").clear()
    find_id("tbPass").send_keys("demo54321")
    find_id("bSubmit").click()
