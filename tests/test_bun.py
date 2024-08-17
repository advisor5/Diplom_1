import pytest
from unittest.mock import Mock
from praktikum.bun import Bun


class TestBuns:

    # Проверка получения названия булочки
    @pytest.mark.parametrize(
            'name',
        [
            ["Флюоресцентная булка R2-D3"],
            ["Флюоресцентная булка R2-D3 Флюоресцентная булка R2-D3"],
            ["Ф"],
            [""],
            [123],
            []

        ]
        )
    def test_get_name_bun_return_name(self, name):
        
        mock_bun = Mock()
        mock_bun.configure_mock(name=name)
        mock_bun.configure_mock(price=10.2)
        
        bun = Bun(mock_bun.name, mock_bun.price)
        assert bun.get_name() == name

    # Проверка получения стоимости булочки
    @pytest.mark.parametrize(
            'price',
        [
            [988.03],
            [988],
            [0],
            [],
            ["123"]
        ]
        )
    def test_get_price_bun_return_price(self, price):

        mock_bun = Mock()
        mock_bun.configure_mock(name="Флюоресцентная булка R2-D3")
        mock_bun.configure_mock(price=price)
        
        bun = Bun(mock_bun.name, mock_bun.price)
        assert bun.get_price() == price
