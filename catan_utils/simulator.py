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

    def generate_random_map(self):
        ##### CHECK TO MAKE SURE SIDES ARE CORRECT
        points = {}
        tiles = {}
        roads = {}
        opposite_side = {1: 4, 2: 5, 3: 6, 4: 1, 5: 2, 6: 3}

        available_sides = {0: [1, 2, 3, 4, 5, 6]}
        num_layers = 4
        first_tile_last_layer = 0
        last_tile_last_layer = 0
        currently_placing_tile = 0
        for layer in range(1, num_layers):
            placed = 0
            num_to_place = 6 * layer
            print(num_to_place)
            currently_wrapping_tile = first_tile_last_layer
            currently_viewing_side = 1
            while placed < num_to_place:
                currently_placing_tile += 1
                print(f'Currently placing tile {currently_placing_tile} on side {currently_viewing_side}')

                # Place one tile
                _available = [_ for _ in [1, 2, 3, 4, 5, 6] if _ != opposite_side[currently_viewing_side]]
                available_sides[currently_placing_tile] = _available
                del available_sides[currently_wrapping_tile][0]
                # done placing tile

                if currently_viewing_side + 1 in available_sides[currently_wrapping_tile]:
                    currently_viewing_side += 1
                    print('Incrementing side')
                else:
                    currently_wrapping_tile += 1
                    print('Incrementing wrapped tile')

                placed += 1
            first_tile_last_layer = currently_placing_tile


if __name__ == '__main__':
    Simulator().generate_random_map()

