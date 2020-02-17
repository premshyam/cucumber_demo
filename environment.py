# import webdriver module from selenium package
from selenium import webdriver
"""
The selenium.webdriver module provides all the WebDriver implementations. 
Currently supported WebDriver implementations are Firefox, Chrome, IE and Remote.
for more information refer the following link: https://selenium-python.readthedocs.io
"""


def before_all(context):
    """
    before_all is a behave hook that allows user to assign/modify own
    attributes to the context object.
    for more information refer link: https://behave.readthedocs.io/en/latest/context_attributes.html
    :param context:
    :return:
    """
    # create a chrome options object
    chrome_options = webdriver.ChromeOptions()
    # configuring chrome to run in detached mode
    chrome_options.add_experimental_option("detach", True)
    # create an instance of Chrome WebDriver and parse the chrome options object
    context.browser = webdriver.Chrome(chrome_options=chrome_options)
