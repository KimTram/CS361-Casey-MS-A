import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the JSON file path from an environment variable
json_file_path = os.getenv('/Users/kimtram/Development/CS 361 Software Engineering I /CS361-Casey-MS-A/boardgame.json', 'boardgame.json')


def load_games():
    with open(json_file_path, 'r') as file:
        return json.load(file)["default"]


@app.route('/games', methods=['GET'])
def get_games():
    num_players = request.args.get('num_players', type=int)

    if num_players is None:
        return jsonify({"error": "num_players parameter is required"}), 400

    data = load_games()
    games = data['default']
    filtered_games = []
    for game in games:
        min_players = int(game['min_players'])
        max_players = int(game['max_players'])
        if min_players <= num_players <= max_players:
            filtered_games.append(game)

    return jsonify(filtered_games)


if __name__ == '__main__':
    app.run(debug=True)