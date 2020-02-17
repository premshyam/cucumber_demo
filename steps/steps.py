from behave import *


@when('we visit "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@then('it should have a title "{title}"')
def step_impl(context, title):
    assert context.browser.title == title

