class Player():

    starting_coins = 3
    starting_establishments = ["Wheat", "Bakery"]
    def __init__(self, player_name, starting_coins) -> None:
        
        self.player_name = player_name
        self.coin_count = starting_coins
        self.unbuilt_landmarks = ['Train Station', 'Shopping Mall', 'Amusement Park', 'Radio Tower']
        self.built_landmarks = []
        self.owned_establishments = []

    def add_or_remove_coins(self, amount, condition="add"):
        if condition == "remove":
            self.coin_count -= amount
        else:
            self.coin_count += amount
    