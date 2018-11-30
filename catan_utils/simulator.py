import numpy as np


class Simulator:
    """ Simulates the game of Catan.

    TODO:
        - Implement the opening phase(s)
            - roll die for each player
            - call Bot.place_settlement(self)
            -
        - Have the state of the game in the simulator
        - create correct data-structure to represent the game
        - On each turn, tell every player what's happened for every other player


    """
    def __init__(self, *players):
        self.players = players

    @staticmethod
    def roll_dice(num_dice=2):
        return sum(np.random.randint(1, 7) for _ in range(num_dice))

    @property
    def map(self):
        return

    def one_round(self):
        for player in self.players:
            self.award_resources(self.roll_dice())
            while True:
                available_moves = self.available_moves(player)
                if len(available_moves) == 0:
                    break
                move = player.move(self.state, available_moves)
                if move is None:
                    break
                self.apply_move(player, move)

    def get_player_move(self, player):
        available_actions = self.available_actions(player)
        return player.move(available_actions)

    def available_moves(self, player):
        """
        returns list(moves)
        Move types:
          -
        """
        available_actions = {}
        return available_actions

    def apply_move(self, player, moves):
        # apply moves
        pass

    def award_resources(self, dice_value):
        # look for matching tiles
        # look for housed on tiles
        # 1 resource per house, 2 resource per city
        # no resources if robber
        for tile in self.map:
            if tile.number == dice_value and not tile.has_robber:
                for house in tile.houses:
                    house.reward_resource(tile.resource, 1)
                for city in tile.cities:
                    city.reward_resource(tile.resource, 2)