

'''
Для запуска pytest tests/test_something.py
либо pytest tests/ для запуска всех тестов в директории 

pytest -v -s tests/

-v - информация о тестах
-s - вывод print в консоль
'''

def test_equal():
    assert 1 == 1, "Number is not equal to expected"

def test_is_not_equal():
    assert 1 != 2, "Number is equal"

#упавший тест
def test_is_not_equal_fail():
    assert 1 != 1, "Number is equal"