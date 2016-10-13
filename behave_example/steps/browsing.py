from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

@given(u'we have gone to the web site')
def step_impl(context):
    context.browser.get("http://drdelozier.pythonanywhere.com")

@when(u'we do nothing')
def step_impl(context):
    pass

@then(u'we will be at the "{text}" page')
def step_impl(context, text):
    heading = context.browser.find_element_by_tag_name('h1')
    assert text in heading.text

@then(u'we will see a table with tasks in it')
def step_impl(context):
    table = context.browser.find_element_by_tag_name('table')
    assert type(table.text) is str
    assert len(table.text) > 0

@then(u'we will see a table with "{text}" row in it')
def step_impl(context, text):
    table = context.browser.find_element_by_tag_name('table')
    rows = context.browser.find_elements_by_tag_name('tr')
    for row in rows:
        print(row.text)
        if row.text == text:
            return
    raise

@then(u'every "{text}" row in the table has a link')
def step_impl(context, text):
    table = context.browser.find_element_by_tag_name('table')
    rows = context.browser.find_elements_by_tag_name('tr')
    for row in rows:
        if row.text == text:
            link = row.find_elements_by_tag_name("a")
            assert len(list(link)) == 1

@when(u'we click on the first link in the "{text}" row')
def step_impl(context, text):
    table = context.browser.find_element_by_tag_name('table')
    rows = context.browser.find_elements_by_tag_name('tr')
    for row in rows:
        if row.text == text:
            link = row.find_elements_by_tag_name("a")
            assert len(list(link)) >= 1
            link[0].click()


@when(u'we enter input "{text}" as new task')
def step_impl(context, text):
    input = context.browser.find_element_by_name('task')
    input.send_keys(text)


@when(u'we click on button "{text}"')
def step_impl(context, text):
    button = context.browser.find_element_by_name(text)
    button.click()
    time.sleep(3)

@when(u'we click on the OK confirmation')
def step_impl(context):
    ok_button = context.browser.find_element_by_tag_name('a')
    assert ok_button.text == "OK"
    ok_button.click()
    time.sleep(3)
    

