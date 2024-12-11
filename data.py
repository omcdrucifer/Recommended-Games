# data file to store graph lists and handle auto loading
from graph import Graph, Vertex

def load_data():
    data = {
            "Action": [("Game A1", 4.5), ("Game A2", 4.7],
                       "Adventure": [(etc, etc)],
    } 
            # This will eventually be populated with game data (genre, title, rating)

    graph = Graph()
    for genre, games in data.items():
        genre_vertex = Vertex(genre)
        graph.add_vertex(genre_vertex)
        for game_name, rating in games:
            game_vertex = Vertex(game_name, rating)
            graph.add_vertex(game_vertex)
            graph.add_edge(genre_vertex, game_vertex)
    return graph
