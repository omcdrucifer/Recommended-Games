# data file to store graph lists and handle auto loading
from graph import Graph, Vertex

def load_data():
    data = {
            "Action": [("Space Marine 2", 8.1), ("Call of Duty Black Ops 6", 6.7), ("Street Fighter 6", 7.5), ("Grand Theft Auto V", 8.5), ("Cyberpunk2077", 8.0)],
            "Adventure": [("Elden Ring", 8.2), ("Final Fantasy XVI", 8.4), ("Remnant II", 7.2), ("Destiny 2", 7.6), ("Elder Scrolls Online", 5.7)],
            "Casual": [("Balatro", 8.2), ("Cities Skylines II", 4.0), ("Stardew Valley", 8.8), ("Marvel Snap", 6.6), ("Sims 4", 4.3)],
            "Sports": [("EA FC 25", 2.4), ("NBA 2K25", 5.8), ("Forza Horizon 5", 8.2), ("Forza Motorsport", 7.0), ("WWE 2K24", 6.6)],
            "Strategy": [("Civilization VI", 7.2), ("DOTA 2", 6.5), ("Stellaris", 8.0), ("Yu Gi Oh Master Duel", 6.0), ("Age of Empires IV", 7.8)],
            } 
    # I limited the graph to 5 titles in 5 genres to keep it from getting too large
    graph = Graph()
    for genre, games in data.items():
        genre_vertex = Vertex(genre)
        graph.add_vertex(genre_vertex)
        for game_name, rating in games:
            game_vertex = Vertex(game_name, rating)
            graph.add_vertex(game_vertex)
            graph.add_edge(genre_vertex, game_vertex)
    return graph
