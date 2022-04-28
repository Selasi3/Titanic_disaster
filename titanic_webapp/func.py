from input_model import Gender


def check_prediction(data):
    if data == 1:
        return "Survived"
    else:
        return "Died"

def convert_gender(info):
    if info == Gender.Female:
        return 0
    else:
        return 1

def journey_embarked(journey):
    embarked = {
        "Queenstown": 1,
        "Cherborg": 2,
        "Southampthon":3
    }
    return embarked.get(journey)
