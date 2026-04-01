import random

ALL_POSSIBLE_ACHIEVEMENTS = {
    'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor',
    'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps',
    'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer',
    'Hidden Path Finder'
}

def gen_player_achievements() -> set:
    num_to_grant = random.randint(5, 10)
    achievements_list = random.sample(list(ALL_POSSIBLE_ACHIEVEMENTS), num_to_grant)
    return set(achievements_list)

def main():
    print("=== Achievement Tracker System ===")

    player_names = ["Alice", "Bob", "Charlie", "Dylan"]
    player_data = {}
    for name in player_names:
        player_data[name] = gen_player_achievements()

    for name, achievements in player_data.items():
        print(f"\nPlayer {name}: {achievements}")

    all_distinct_achievements = set.union(*player_data.values())
    print(f"\nAll distinct achievements: {all_distinct_achievements}")

    common_achievements = set.intersection(*player_data.values())
    print(f"\nCommon achievements: {common_achievements}")

    for player_name, player_achievements in player_data.items():
        other_players_achievements = set()
        for other_name, other_achievements in player_data.items():
            if player_name != other_name:
                other_players_achievements.update(other_achievements)
        
        unique_to_player = player_achievements.difference(other_players_achievements)
        print(f"Only {player_name} has: {unique_to_player}")

    for player_name, player_achievements in player_data.items():
        missing = ALL_POSSIBLE_ACHIEVEMENTS.difference(player_achievements)
        print(f"{player_name} is missing: {missing}")

if __name__ == "__main__":
    main()
