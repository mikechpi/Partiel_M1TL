import pytest
from Controllers.MatchController import MatchController
from Models.Match import Match


class TestMatchController:

    @pytest.fixture
    def match_controller(self):
        return MatchController()

    @pytest.fixture
    def players(self):
        return [
            {'first_name': 'Mike', 'last_name': 'Chingpi'},
            {'first_name': 'John', 'last_name': 'Caillard'},
        ]

    def test_create_match_pairs(self, match_controller, players):
        pairs = match_controller.create_match_pairs(players)
        assert len(pairs) == 2
        assert all(isinstance(pair, tuple) and len(pair) == 2 for pair in pairs)

    def test_create_matches(self, match_controller, players):
        pairs = match_controller.create_match_pairs(players)
        matches = match_controller.create_matches(pairs)
        assert len(matches) == 2
        assert all(isinstance(match, Match) for match in matches)

    def test_pair_players(self, match_controller, players):
        sorted_players = sorted(players, key=lambda x: x['first_name'])
        played_matches = []
        paired_players = match_controller.pair_players(sorted_players, played_matches)
        assert len(paired_players) == 2
        assert all(isinstance(pair, tuple) and len(pair) == 2 for pair in paired_players)

    def test_has_played_together(self, match_controller, players):
        player1 = {'first_name': 'Mike', 'last_name': 'chingpi'}
        player2 = {'first_name': 'John', 'last_name': 'test'}
        played_matches = [
            [(player1, player2), (player1, player2)],
            [(player1, {'first_name': 'Leo', 'last_name': 'test'})]
        ]
        assert match_controller.has_played_together(player1, player2, played_matches) is True
        assert match_controller.has_played_together(
            player1,
            {'first_name': 'Leo', 'last_name': 'test'},
            played_matches
        ) is False
