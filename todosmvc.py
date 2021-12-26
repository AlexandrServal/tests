from selene import have, command
from selene.support.shared import browser


todo_list = browser.all('#todo-list>li')


def visit():
    browser.config.hold_browser_open = True
    browser.open("http://todomvc4tasj.herokuapp.com/")
    browser.should(have.js_returned(True, "return $._data($('#clear-completed')[0], 'events').hasOwnProperty('click')"))


def add(*todos: str):
    for todo in todos:
        browser.element('#new-todo').type(todo).press_enter()


def should_have(*todos: str):
    todo_list.should(have.exact_texts(*todos))


def start_editing(todo: str, new_text):
    todo_list.element_by(have.exact_text(todo)).double_click()
    return todo_list.element_by(have.css_class('editing'))\
        .element('.edit').perform(command.js.set_value(new_text))


def edit(todo: str, new_text):
    start_editing(todo, new_text).press_enter()


def cancel_editing(todo: str, new_text):
    start_editing(todo, new_text).press_escape()


def toggle(todo: str):
    todo_list.element_by(have.exact_text(todo)).element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()


def delete(todo: str):
    todo_list.element_by(have.exact_text(todo)).hover().element('.destroy').click()

