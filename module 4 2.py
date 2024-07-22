def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function() #Вызов функции работает, так как функция создана локально в области видимости функции test_function()

#inner_function() | если мы вызываем функцию здесь,
# то в консоле мы получаем ошибку:
# Traceback (most recent call last):
#   File "F:\PythonUrbanUniversity\PythonProjects\Module4Work2\module 4 2.py", line 6, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
# которая говорит что функция inner_function() вне области видимости
# и предлагает нам использовать функцию test_function()

test_function()

#inner_function() | если мы вызываем функцию здесь,
# то в консоле мы получаем такуюже ошибку,
# так как область видимости функции не распространяется на эти строки