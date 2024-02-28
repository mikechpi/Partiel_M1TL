import pytest
from Controllers.PlayerController import PlayerController
from Views.PlayerView import PlayerView
from unittest.mock import patch


class TestPlayerController:

    @pytest.fixture
    def player_controller(self):
        return PlayerController()

    @patch.object(PlayerView, 'get_player_info', return_value=('John', 'Doe', '1990-01-01', '123456'))
    def test_add_player(self, mock_get_player_info, player_controller):
        player_controller.add_player()
        assert player_controller.player is not None
        assert player_controller.first_name == 'John'
        assert player_controller.last_name == 'Doe'
        assert player_controller.birth_date == '1990-01-01'
        assert player_controller.national_chess_id == '123456'
