from selenium import webdriver


def before_all(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    context.browser = webdriver.Chrome(chrome_options=chrome_options)


# def after_all(context):
    # context.browser.implicitly_wait(30)
    # context.browser.quit()
