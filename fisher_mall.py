"""KT Cycle exercise"""


def fisher(text: str) -> int:
    """"You are a free spirit, living by the sea, and your daily work depends on the size of the waves. There are four different types of waves.

    During the first category, you catch fish in your canoe (" ______/ ") and sell them at the market (" (-(-(--)-)-) ") for $100 (" [$(100)$] "), which you then spend all on beer in the evening (" []b ").

    In the second category, sharks appear in the sea (" ^~~ "), whom you scare away with your sword (" <%%%|====> ").

    During the third category, you doze off (" {zzz}°°° "), charge batteries (" 0% |IIII| 100% "), and drink tea (" c(_) ").

    During the fourth category, you must be brave (" ∠ ･`_´･ ") and escape to the middle of the island among the tigers (" =^..^= ") for safety, where your only entertainment is playing dominoes (" [::|:::] ").

    Your task is to find out based on the keywords which category of waves the day is and return that number. However, since the waves can change, you must always return the highest number corresponding to the category of waves present that day.
    If there are no keywords present, return 0.

    print(fisher(“ Sa jood [_]b ja naudid elu. “ )) -> "1”
    print_vetemees(“ Hommikul on meres on palju ^~~, kuid sa läksid ikka  \______/-> "2"
    print_vetemees(“Sa {zzz}°°° “)ning hiljem ning kalakäsiraamatust uusi õngetrikke õppida”) -> "3”
    """
