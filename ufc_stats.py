import json
from requests import get
from secret_keys import ufc_api_key

UFC_API_KEY = ufc_api_key  # insert your own api key here


def main():
    BASE_URL = "https://fightingtomatoes.com/API"
    YEAR = "any"
    EVENT = "any"

    fighter = input("Input first and last name of the fighter: ")
    
    json_data = None

    try:
        # url example: https://fightingtomatoes.com/API/{api-key}/any/any/Conor McGregor
        response = get(f"{BASE_URL}/{UFC_API_KEY}/{YEAR}/{EVENT}/{fighter}")
        json_data = response_to_json(response)
    except:
        print("Failed to get the data. Check for spelling errors in the fighter's name.")

    if json_data:
        win_count = count_wins(json_data, fighter)
        total_fights = len(json_data)

        win_rate = int(round((win_count/total_fights), 2) * 100)

        print(f"Between the years 1993 and 2022 {fighter} had won {win_count} fights out of {total_fights} ({win_rate}% win rate).")
    


def response_to_json(response):
    data = response.text
    format_text = ""
    for line in data.split('\n'):
        if 'html' in line:
            break
        format_text += line.strip()

    return json.loads(format_text)


def count_wins(fight_data, fighter):
    win_count = 0
    for fight in fight_data:
        if fighter in fight['winner']:
            win_count += 1
    return win_count


main()

