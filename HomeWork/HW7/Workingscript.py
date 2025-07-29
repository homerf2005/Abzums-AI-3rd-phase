import requests
import json


def mastermind():
    url = "https://mastermind.darkube.app/"

    def start_game(url):
        url = f"{url}game"
        response = requests.post(url, timeout=10)
        data = response.json()
        return data.get("game_id")

    def send_guess(url, game_id):
        body = {
            "game_id": game_id,
            "guess": input()
        }
        url = f"{url}guess"
        response = requests.post(url, json=body, timeout=10)
        data = response.json()
        data = dict(data)
        return data

    game_id = start_game(url)
    count = 0
    print(f"Hi, Game started with ID: {game_id}")
    while True:
        res = send_guess(url, game_id)
        if "error" in res:
            print(res["error"])
            continue
        print(f"Black: {res.get("black", "invalid input")}")
        print(f"White: {res.get("white", "")}")
        if res.get("black") == 4:
            print("You win!")
            break
        count += 1
        if count != 12:
            print(f"Guess remaining: {12 - count}")
        if count == 12:
            print("You lose!")
            break


if __name__ == "__main__":
    mastermind()
