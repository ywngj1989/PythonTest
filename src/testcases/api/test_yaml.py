import json


def test_json():
    r = json.load(open("calc.json"))
    print(r)


