from abc import ABCMeta, abstractmethod


class Bot(metaclass=ABCMeta):
    def __init__(self):
        self.resources = {'wood': 0, 'wheat':0, 'brick':0, 'ore':0, 'sheep':0}
        self.dev_cards = {'knight':0, 'monopoly':0, 'year of plenty':0, 'road builder':0, 'victory point':0}
        self.longest_road = False
        self.largest_army = False

    """Phase 0 Functions"""
    @abstractmethod
    def receive_rules(self):
        pass

    """Phase 1 Functions"""
    @abstractmethod
    def place_initial_settlement(self, game_state, available_moves):
        """
        Needs to return a settlement location and a connecting road.  Move needs to be valid.
        Will run twice
        :return: settlement_location, road_location
        """
        pass

    """Phase 2 Functions"""
    @abstractmethod
    def make_a_move(self, game_state, available_moves):
        """
        Returning None will end your turn.  Trade, build, or play dev card.
        Available moves will be structured as:
            availabe_moves = {buy:{road:[available_road_locations],
                                   settlement:[available_settlement_locations],
                                   city:[available_city_locations],
                                   dev_card:True},
                              play:self.dev_cards,
                              trade:[player_ids]}


        :return: move
        """
        pass

    @abstractmethod
    def propose_trade_request(self, game_state, player_id, your_resources):
        """
        Propose two trades to each player. Unless excepted on first one.
        :param player_id:
        :return:
        """
        pass

    @abstractmethod
    def evaluate_trade_request(self, game_state, player_id, your_resources):
        pass

    @abstractmethod
    def event_notification(self, event):
        """
        Each player is notified of all public events.  This function returns nothing.
        :param event:
        :return: None
        """
        pass

class SimpleBot(Bot):
    """Basic Player to make moves essentially randomly.
    
    TODO:
        - Phase 1: Placing Initial Settlements
            - Look at map and see where to place settlement and road. (Eventually add logic base off of order of play)
            - Asked to do this 2 times
            
        - Phase 2: Look at the map and look at the hand and decide which action to take
            - Each Turn:
                - Determine if bot wants to play a knight card (preroll)
                - Actions:
                    - Trade with other players
                    - Trade in for other resources(4 for 1, 3 for 1 port, 2 for 1 port)
                    - Build/Development Card
                    - Use Development Card

    
    """
    def __init__(self):
        super().__init__()
        pass

    """Phase 1 Functions"""
    def place_initial_settlement(self):
        pass

    """Phase 2 Function"""
    def make_a_move(self):
        pass

    def evaluate_trade_request(self):
        pass

    def

