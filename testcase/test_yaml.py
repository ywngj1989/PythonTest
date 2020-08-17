import json
import yaml


def test_json():
    f = open("calc.json")
    r = json.load(f)
    print(r)


def test_yaml():
    print(yaml.load(open("calc2.yaml")))
