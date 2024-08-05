import zmq


def main():
    # ZeroMQ context
    context = zmq.Context()

    # Create a REQ (request) socket
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    while True:
        num_players = input("Enter the number of players: ")

        # Send the number of players to the server
        socket.send_string(num_players)

        # Receive the filtered list of games
        filtered_games = socket.recv_json()

        print("Filtered Games:")
        for index, game in enumerate(filtered_games):
            print(f"{index + 1}. {game['title']}")


if __name__ == "__main__":
    main()
