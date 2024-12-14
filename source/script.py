# main script to handle interactions 
from data import load_data
from graph import Graph, Vertex # at this stage I don't know if script.py needs graph interaction itself
from prints import welcome, greeting, line_break, double_line_break, goodbye_message

print(welcome())
print(line_break())
print(greeting())
print(double_line_break())

def get_user_preferences():
    genre = input("  Enter a genre to get recommendations: ").strip().title()
    return genre

def recommend_games(graph, genre):
    games = graph.bfs(genre)
    game_vertices = [game for game in games if game.rating is not None]
    sorted_games = sorted(game_vertices, key=lambda x: x.rating, reverse=True)
    return sorted_games

def main():
    while True:
        graph = load_data()
        genre = get_user_preferences()
        recommendations = recommend_games(graph, genre)
        print(line_break())
        print(f"  Top games in {genre}:\n")
        n = 1
        for game in recommendations:
            print(f"\n{n}. {game.value} with rating {game.rating}\n")
            n += 1
        print(line_break())
        choose = input("  Would you like to look for more recommendations? <yes/no>: ").strip().lower()
        if choose != "yes":
            print(goodbye_message())
            break

if __name__ == "__main__":
    main()
