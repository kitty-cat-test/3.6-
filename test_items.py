link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_basket(browser):
	browser.get(link)
	buttons = browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
	assert len(buttons) == 1, "add to cart button not found"
	
	