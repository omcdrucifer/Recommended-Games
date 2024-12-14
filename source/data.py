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

    blurb = {
            "Space Marine 2": "The sequel of the legendary license space marine,\nby the creators of the best-seller world war z (15m players)",
            "Call of Duty Black Ops 6": "Black Ops 6 features fast, responsive movement on PC,\nallowing players to swiftly navigate the map in search of\ntheir next target and objective.",
            "Street Fighter 6": "Street Fighter 6 offers a highly evolved combat\nsystem with three control types - Classic, Modern and Dynamic",
            "Grand Theft Auto V": "Experience entertainment blockbusters,\nGrand Theft Auto V and GTA Online.",
            "Cyberpunk2077": "Magnificent, confident and loaded with content\nthat other games do not offer.",
            "Elden Ring": "2022 Game of the Year",
            "Final Fantasy XVI": "An epic dark fantasy world where the fate of the\nland is decided by the mighty Eikons and the Dominants who wield them.",
            "Remnant II": "Remnant 2 iterates on the original to phenomenal effect.",
            "Destiny 2": "Destiny 2 takes place in a fictional universe where you will\nassume the role of a Guardian, a protector of Earth's last city.",
            "Elder Scrolls Online": "Go anywhere, do anything, and play your way\nin The Elder Scrolls Online, the award-winning online\nRPG set in the Elder Scrolls universe.",
            "Balatro": "Balatro is one of the most addictive games of the past few years",
            "Cities Skylines II": "Cities: Skylines II is still a long way from perfect.",
            "Stardew Valley": "Stardew Valley is a highly praised farming simulation game",
            "Marvel Snap": "Marvel Snap is a fast-paced mobile collectible card\ngame that features strategic gameplay",
            "Sims 4": "Regardless of environmental aesthetic, the series has\nalways been functionally and fundamentally Californian."
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
