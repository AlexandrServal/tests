from codarium_python_selene_more_tests.tests import todosmvc # ?


def test_todo_life_cycle():
     todosmvc.visit()

     todosmvc.add('a', 'b', 'c')
     todosmvc.should_have('a', 'b', 'c')

     # todosmvc.start_editing('a', 'a editing')
     todosmvc.edit('a', 'a edited')

     todosmvc.delete('a edited')
     todosmvc.should_have('b', 'c')

     todosmvc.cancel_editing('c', 'to be canceled')

     todosmvc.toggle('c')
     todosmvc.clear_completed()
     todosmvc.should_have('b')
