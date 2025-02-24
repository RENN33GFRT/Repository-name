import pytest
import os
import logging


# Удаляем файл лога, если он существует
LOGFILE = 'test_logfile.log'
if os.path.exists(LOGFILE):
    os.remove(LOGFILE)

# Пример функции для тестирования
@log(LOGFILE)
def add(a, b):
    return a + b

@log(LOGFILE)
def divide(a, b):
    return a / b

def test_add():
    result = add(5, 3)
    assert result == 8

def test_divide():
    result = divide(10, 2)
    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_log_file_exists():
    assert os.path.exists(LOGFILE)

def test_log_content():
    with open(LOGFILE, 'r') as f:
        log_content = f.read()
        assert 'Starting function: add with arguments: (5, 3)' in log_content
        assert 'Function: add completed successfully with result: 8' in log_content
        assert 'Starting function: divide with arguments: (10, 2)' in log_content
        assert 'Function: divide completed successfully with result: 5' in log_content
        assert 'Function: divide raised an error: ZeroDivisionError' in log_content

# Удаляем файл лога после тестов
def teardown_module(module):
    if os.path.exists(LOGFILE):
        os.remove(LOGFILE)

'эта н существует тока потому что кое-кто нитуда закамитил'