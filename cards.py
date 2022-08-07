class Card():

    def __init__(self, card_type, build_cost, card_name, effect) -> None:
        self.card_type = card_type
        self.build_cost = build_cost
        self.card_name = card_name
        self.effect = effect


class Landmark(Card):
    
    def __init__(self, card_type, build_cost, card_name, effect) -> None:
        super().__init__(card_type, build_cost, card_name, effect)


class Establishment(Card):

    def __init__(self, card_type, build_cost, card_name, effect, establishment_type, activation_num) -> None:
        super().__init__(card_type, build_cost, card_name, effect)
        self.estab_type = establishment_type
        self.activation_num = activation_num
