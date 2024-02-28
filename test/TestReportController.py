from Controllers.ReportController import ReportController
from unittest.mock import patch, MagicMock


class TestReportController:

    @patch('builtins.input', side_effect=['1'])
    def test_select_tournament_from_list(self, mock_input):
        report_controller = ReportController()
        report_controller.list_tournaments = MagicMock(
            return_value=[{'name': 'Tournament 1'}, {'name': 'Tournament 2'}])
        selected_tournament = report_controller.select_tournament_from_list()
        assert selected_tournament == {'name': 'Tournament 1'}
