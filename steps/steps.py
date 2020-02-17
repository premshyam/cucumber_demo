"""
behave uses tests written in a natural language style, backed up by Python code.
It's the cucumber counter part in python. Supports Gherkin language
This file contains the step definitions.
"""
from behave import *


@given('we have behave installed')
def step_impl(context):
    # do nothing
    pass


@when('we visit "{url}"')
def step_impl(context, url):
    """
    instruct the browser to visit the give url
    :param context:
    :param url:
    :return:
    """
    context.browser.get(url)


@then('it should have a title "{title}"')
def step_impl(context, title):
    """
    check the title of the web page
    :param context:
    :param title:
    :return:
    """
    assert context.browser.title == title

