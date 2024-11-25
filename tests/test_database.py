import pytest
from unittest.mock import patch

from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient


class TestDataBase:

    # проверка получения списка булок возвращаемого методом available_buns
    @patch("praktikum.database.Database.available_buns")
    @pytest.mark.parametrize(
        'value',
        [
        (Bun("black", 10)),
        (Bun("white", 20)),
        (Bun("red", 30))
        ]
    )
    def test_available_buns_return_buns(self, mock_available_buns, value):
        
        mock_available_buns.return_value = [value]

        database = Database()

        actually_value = database.available_buns()[0]
        expected_value = value
        assert actually_value == expected_value

    # проверка получения названия булок из списка, возвращаемого методом available_buns
    @patch("praktikum.database.Database.available_buns")
    @pytest.mark.parametrize(
        'value, test',
        [
        [(Bun("black", 10)),"black"],
        [(Bun("white", 20)),"white"],
        [(Bun("red", 30)),"red"]
        ]
    )
    def test_available_buns_return_buns_name(self, mock_available_buns, value, test):
        
        mock_available_buns.return_value = [value]

        database = Database()

        actually_value = database.available_buns()[0].get_name()
        expected_value = test
        assert actually_value == expected_value

    # проверка получения списка ингредиентов возвращаемого методом available_ingredients
    @patch("praktikum.database.Database.available_ingredients")
    @pytest.mark.parametrize(
        'value',
        [
        (Ingredient("SAUCE", "hot", 10)),
        (Ingredient("SAUCE", "sour", 20)),
        (Ingredient("SAUCE", "chili", 30))
        ]
    )

    def test_available_ingredients_return_ingredients(self, mock_available_ingredients, value):
        
        mock_available_ingredients.return_value = [value]
        database = Database() 

        actually_value = database.available_ingredients()[0]
        expected_value = value
        assert actually_value == expected_value
