import util

def group_by_suit(cards):
    return util.group_by(cards, lambda card: card.suit )


def group_by_value(cards):
    return util.group_by(cards, lambda card: card.value)

def partition_by_color(cards):
    return util.partition(cards, lambda card: card.suit in ["spades", "clubs"])
