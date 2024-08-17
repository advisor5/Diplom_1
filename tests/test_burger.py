import pytest
from unittest.mock import Mock 

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:

    # проверка получения стоимости булки в бургере
    @pytest.mark.parametrize(
            'price',
        [
            [988.03],
            [988],
            [0],
            []
        ]
        )
    def test_get_price_bun_in_burger_return_price_two_buns(self, price):
        
        mock_bun = Mock()
        mock_bun.configure_mock(name="Флюоресцентная булка R2-D3")
        mock_bun.configure_mock(price=price)
        bun = Bun(
            mock_bun.name,
            mock_bun.price
        )
        
        burger = Burger()
        burger.set_buns(bun)
        
        actually_value = burger.get_price()
        expected_value = bun.get_price() * 2
        assert actually_value == expected_value

    # проверка получения стоимости булки с игредиентом в бургере
    @pytest.mark.parametrize(
            'bun_price, ingredient_price',
        [
            [988.03, 988.03],
            [988, 988],
            [0, 0],
            [(),()],
            ["123", "123"]
        ]
        )
    def test_get_price_bun_whith_ingredient_return_total_price(self, bun_price, ingredient_price):
        
        mock_bun = Mock()
        mock_bun.configure_mock(name="Флюоресцентная булка R2-D3")
        mock_bun.configure_mock(price=bun_price)
        bun = Bun(
            mock_bun.name,
            mock_bun.price
        )

        mock_ingredient = Mock()
        mock_ingredient.configure_mock(ingredient_type="Соусы")
        mock_ingredient.configure_mock(name="Spicy-X")
        mock_ingredient.configure_mock(price=ingredient_price)
        
        ingredient = Ingredient(
            mock_ingredient.ingredient_type,
            mock_ingredient.name,
            mock_ingredient.price
        )
        
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        
        actually_value = burger.get_price()
        expected_value = bun.get_price() * 2 + ingredient.get_price()
        assert actually_value == expected_value
