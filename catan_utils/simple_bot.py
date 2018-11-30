from abc import ABCMeta, abstractmethod


class Bot(metaclass=ABCMeta):
    def __init__(self):
        self.resources = {'wood': 0, 'wheat':0, 'brick':0, 'ore':0, 'sheep':0}

    @abstractmethod
    def evaluate_trade_request(self):
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

    # def evaluate_trade_request(self):
    #     pass