# main script to handle interactions 
from data import load_data
from graph import Graph, Vertex # at this stage I don't know if script.py needs graph interaction itself

def get_user_preferences():
    genre = input("Enter a genre to get recommendations: ").strip().title()
    return genre

def recommend_games(graph, genre):
    games = graph.bfs(genre)
    game_vertices = [game for game in games if game.rating is not None]
    sorted_games = sorted(game_vertices, key=lambda x: x.rating, reverse=True)
    return sorted_games

def main():
    graph = load_data()
    genre = get_user_preferences()
    recommendations = recommend_games(graph, genre)
    print(f"\nTop games in {genre}:\n")
    for game in recommendations:
        print(f"\n{game.value} with rating {game.rating}\n")

if __name__ == "__main__":
    main()
