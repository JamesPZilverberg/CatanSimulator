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
    def game_state(self):
        """
        Game state will be a dictionary that will contain map, resource count, etc.  Contains all of the public
        information.
        :return:
        """
        return

    def one_round(self):
        """
        To Do:
        Will need to define trade protocol object
        :return:
        """
        for player in self.players:
            self.award_resources(self.roll_dice())
            while True:
                available_moves = self.get_available_moves(player)
                if len(available_moves) == 0:
                    break
                move = player.make_a_move(self.game_state, available_moves)
                if move is None:
                    break
                self._apply_move(player, move)

    def get_available_moves(self, player):
        """
        availabe_moves = {buy:{road:[available_road_locations],
                               settlement:[available_settlement_locations],
                               city:[available_city_locations],
                               dev_card:True},
                          play:self.dev_cards,
                          trade:[player_ids]}

        buy:
            - look at player resources
            - see what can be built with those resources
            - road:
                - check if road is already there
                - check if path is blocked
            - settlement:
                - check to see if road connected
                - check to see if space is two away from all settlements
            - city:
                - check to see if any settlements on board
        play:
            - return all active dev cards (can't use on current turn)
            - check to see if dev card has been played this turn
            - can't play victory point
        trade:
            - initiated trade protocol which
            - list of player_ids
            - max trade proposals per player argument (start with 2)
            - max completed trades per player (start with 1)

        """
        can_buy = {
            'road': player.lumber > 0 and player.brick > 0,
            'settlement': player.lumber > 0 and player.brick > 0 and player.wool > 0 and player.grain > 0,
            'city': player.ore > 2 and player.grain > 1,
            'dev_card': player.ore > 0 and player.grain > 0 and player.wool > 0
        }

        can_buy['road'] = self._get_available_roads(player.id) if can_buy['road'] else []
        can_buy['settlement'] = self._get_available_settlements(player.id) if can_buy['settlements'] else []
        can_buy['city'] = self._get_available_cities(player.id) if can_buy['city'] else []

        return {'buy': can_buy}

    def _get_available_roads(self, player_id):
        road_positions = []
        return road_positions

    def _get_available_settlements(self, player_id):
        settlement_positions = []
        return settlement_positions
    
    def _get_available_cities(self, player_id):
        cities_positions = []
        return cities_positions


    def _apply_move(self, player, moves):
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