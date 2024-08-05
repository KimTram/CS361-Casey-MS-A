# CS361-Casey-MS-A

# Game Filter Microservice

## Overview
This microservice filters playable board games based on the number of players. It uses ZeroMQ for messaging.

## Communication Contract

### Requesting Data
To request data from the microservice, follow these steps:

1. Establish a ZeroMQ REQ (request) socket.
2. Connect to the microservice at `tcp://localhost:5555`.
3. Send the number of players as a string message.

#### Example Request
```python
import zmq

# ZeroMQ context
context = zmq.Context()

# Create a REQ (request) socket
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Send the number of players to the server
num_players = "4"
socket.send_string(num_players)
```

### Receiving Data
To receive data from the microservice, follow these steps:

Wait for the response from the microservice.
The response will be a JSON array of filtered games.

#### Example Response
```python
# Receive the filtered list of games
filtered_games = socket.recv_json()

print("Filtered Games:")
for index, game in enumerate(filtered_games):
    print(f"{index + 1}. {game['title']}")
```


