import zmq
import json
import os


# Load the game data from the JSON file
def load_game_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


# Filter the games based on the number of players
def filter_games_by_players(games, num_players):
    filtered_games = []
    for game in games:
        min_players = int(game['min_players'])
        max_players = int(game['max_players'])
        if min_players <= num_players <= max_players:
            filtered_games.append(game)
    return filtered_games


def main():
    # Define the file path
    # filepath = os.path.join(os.path.dirname(__file__), 'boardgame.json')
    filepath = '/Users/kimtram/Development/CS 361 Software Engineering I /CS361-Casey-MS-A/boardgame.json'

    # Load the game data
    data = load_game_data(filepath)
    games = data['default']

    # ZeroMQ context
    context = zmq.Context()

    # Create a REP (reply) socket
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        # Wait for the next request from the client
        message = socket.recv_string()
        num_players = int(message)

        # Filter the games
        filtered_games = filter_games_by_players(games, num_players)

        # Send the filtered list back to the client
        socket.send_json(filtered_games)


if __name__ == "__main__":
    main()
