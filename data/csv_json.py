import csv
import json

DATA_ADS = "ads.csv"
JSON_ADS = "ads.json"
DATA_CATEGORIES = "categories.csv"
JSON_CATEGORIES = "categories.json"


def run_convert(csv_file, json_file, model_name):
    result = []

    with open(csv_file, encoding='utf-8') as csv_f:
        for value in csv.DictReader(csv_f):
            to_add = {'model': model_name, 'pk': int(value['Id'] if 'Id' in value else value['id'])}
            if 'Id' in value:
                del value['Id']
            else:
                del value['id']
            if 'is_published' in value:
                if value['is_published'] == 'TRUE':
                    value['is_published'] = True
                else:
                    value['is_published'] = False
            if 'price' in value:
                value['price'] = int(value['price'])
            to_add['fields'] = value
            result.append(to_add)
    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))


run_convert(DATA_CATEGORIES, JSON_CATEGORIES, 'ads.category')
run_convert(DATA_ADS, JSON_ADS, 'ads.ad')
