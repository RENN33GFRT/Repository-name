import os

import pytest

from src.decorators import log  # Замените your_module на имя вашего файла


# Пример функции для тестирования
@log(filename="test.log")
def my_function(a, b):
    return a + b


@log()
def my_function_no_file(a, b):
    return a + b


@log(filename="test.log")
def my_function_with_error(a, b):
    raise ValueError("Test error")


@log()
def my_function_with_error_no_file(a, b):
    raise ValueError("Test error")


def setup_method():
    # Очищаем файл лога перед каждым тестом
    if os.path.exists("test.log"):
        os.remove("test.log")


def teardown_method():
    # Удаляем файл лога после каждого теста
    if os.path.exists("test.log"):
        os.remove("test.log")


def test_log_success_with_file(capsys):
    """Тест успешного выполнения функции и записи в файл."""
    setup_method()  # Вызываем setup перед тестом
    result = my_function(2, 3)
    assert result == 5

    # Проверяем, что файл существует и содержит ожидаемую строку
    assert os.path.exists("test.log")
    with open("test.log", "r") as f:
        content = f.read()
        assert "my_function ok\n" in content

    # Проверяем, что ничего не было выведено в stdout
    captured = capsys.readouterr()
    assert captured.out == ""
    teardown_method()  # Вызываем teardown после теста


def test_log_success_no_file(capsys):
    """Тест успешного выполнения функции и вывода в stdout."""
    setup_method()
    result = my_function_no_file(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert captured.out == "my_function_no_file ok\n"
    teardown_method()


def test_log_error_with_file(capsys):
    """Тест обработки ошибки и записи в файл."""
    setup_method()
    with pytest.raises(ValueError, match="Test error"):
        my_function_with_error(1, 2)

    # Проверяем, что файл существует и содержит информацию об ошибке
    assert os.path.exists("test.log")
    with open("test.log", "r") as f:
        content = f.read()
        assert "my_function_with_error error: ValueError. Inputs: args=(1, 2), kwargs={}\n" in content

    # Проверяем, что ничего не было выведено в stdout
    captured = capsys.readouterr()
    assert captured.out == ""
    teardown_method()


def test_log_error_no_file(capsys):
    """Тест обработки ошибки и вывода в stdout."""
    setup_method()
    with pytest.raises(ValueError, match="Test error"):
        my_function_with_error_no_file(1, 2)

    captured = capsys.readouterr()
    assert "my_function_with_error_no_file error: ValueError. Inputs: args=(1, 2), kwargs={}\n" in captured.out
    teardown_method()


def test_file_writing_error(capsys, monkeypatch):
    """Тест обработки ошибки при записи в файл."""
    setup_method()

    # Мокируем open, чтобы вызвать исключение при записи
    def mock_open(*args, **kwargs):
        raise IOError("Mocked file writing error")

    monkeypatch.setattr(os, "open", mock_open)

    with pytest.raises(ValueError, match="Test error"):
        my_function_with_error(1, 2)

    captured = capsys.readouterr()
    assert "" in captured.out
    teardown_method()


"n"
