def ft_achivement_tracker() -> None:
    print("=== Achivement Tracker System ===\n")
    players= [
    {"name": "alice", "achivements": {"first_kill", "level_10", "treasure_hunter", "speed_demon"}},
    {"name": "bob", "achivements": {"first_kill", "level_10", "boss_slayer", "collector"}},
    {"name": "charlie", "achivements": {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}}
    ]
    for player in players:
        print(f"Player {player['name']}, achivements: {player['achivements']}")
  
    print("\n=== Achievement Analytics ===")

    all_unique_achivements = set()

    for player in players:
        all_unique_achivements |= player["achivements"]

    print(f"All unique achivements: {all_unique_achivements}")
    print(f"Total unique achivements: {len(all_unique_achivements)}")
    
    common_all_players = players[0]["achivements"]

    for player in players[1:]:
        common_all_players &= player["achivements"]
    print(f"Common to all players: {common_all_players}")
if __name__ == "__main__":
       ft_achivement_tracker()
