import pytest
from unittest.mock import Mock

from praktikum.ingredient import Ingredient


class TestIngredient:
    # Проверка получения цены ингредиента
    @pytest.mark.parametrize(
            'ingredient_price',
        [
            [988.03],
            [988],
            [0],
            [],
            ["123"]
        ]
        )
    def test_get_price_return_ingredient_price(self, ingredient_price):
        
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(ingredient_type="Соусы")
        mock_ingredient.configure_mock(name="Spicy-X")
        mock_ingredient.configure_mock(price=ingredient_price)
        
        ingredient = Ingredient(
            mock_ingredient.ingredient_type,
            mock_ingredient.name,
            mock_ingredient.price
        )
        assert ingredient.get_price() == ingredient_price

    # Проверка получения названия ингредиента
    @pytest.mark.parametrize(
            'ingredient_name',
        [
            ["Spicy-X"],
            ["Spicy-XSpicy-XSpicy-XSpicy-XSpicy-XSpicy-XSpicy-XSpicy-XSpicy-X"],
            ["S"],
            [""],
            [123],
            []
        ]
        )
    def test_get_name_return_ingredient_name(self, ingredient_name):
        
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(ingredient_type="Соусы")
        mock_ingredient.configure_mock(name=ingredient_name)
        mock_ingredient.configure_mock(price=1.2)
        
        ingredient = Ingredient(
            mock_ingredient.ingredient_type,
            mock_ingredient.name,
            mock_ingredient.price
        )
        assert ingredient.get_name() == mock_ingredient.name

    # Проверка получения Типа ингредиента
    @pytest.mark.parametrize(
            'ingredient_type',
        [
            ["Spicy-X"],
            ["Spicy-XSpicy-XSpicy-XSpicy-XSpicy-XSpicy-XSpicy-XSpicy-XSpicy-X"],
            ["S"],
            [""],
            [123],
            []
        ]
        )
    def test_get_type_return_ingredient_type(self, ingredient_type):
        
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(ingredient_type=ingredient_type)
        mock_ingredient.configure_mock(name="Spicy-X")
        mock_ingredient.configure_mock(price=1.2)
        
        ingredient = Ingredient(
            mock_ingredient.ingredient_type,
            mock_ingredient.name,
            mock_ingredient.price
        )
        assert ingredient.get_type() == mock_ingredient.ingredient_type
