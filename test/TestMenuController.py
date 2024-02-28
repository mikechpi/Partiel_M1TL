from Controllers.PlayerController import PlayerController
from Controllers.TournamentController import TournamentController
from Views.ReportView import ReportView
from Controllers.MenuController import MenuController
from unittest.mock import patch


class TestMenuController:

    @patch('builtins.input', side_effect=['1', '0'])
    def test_user_choice_add_player(self, mock_input):
        menu_controller = MenuController()
        with patch.object(PlayerController, 'add_player') as mock_add_player:
            menu_controller.user_choice()
            mock_add_player.assert_called_once()

    @patch('builtins.input', side_effect=['2', '0'])
    def test_user_choice_create_tournament(self, mock_input):
        menu_controller = MenuController()
        with patch.object(TournamentController, 'create_tournament') as mock_create_tournament:
            menu_controller.user_choice()
            mock_create_tournament.assert_called_once()

    @patch('builtins.input', side_effect=['3', '0'])
    def test_user_choice_add_player_to_tournament(self, mock_input):
        menu_controller = MenuController()
        with patch.object(TournamentController, 'add_player_to_tournament') as mock_add_player_to_tournament:
            menu_controller.user_choice()
            mock_add_player_to_tournament.assert_called_once()

    # Ajoutez d'autres tests pour couvrir les autres choix du menu et les méthodes de rapport si nécessaire

    @patch('builtins.input', side_effect=['5', '0'])
    def test_report_menu_choice_display_rounds_and_matches(self, mock_input):
        menu_controller = MenuController()
        with patch.object(ReportView, 'display_rounds_and_matches') as mock_display_rounds_and_matches:
            menu_controller.report_menu_choice()
            mock_display_rounds_and_matches.assert_called_once()

    # Ajoutez d'autres tests pour couvrir les autres options du sous-menu de rapport si nécessaire
