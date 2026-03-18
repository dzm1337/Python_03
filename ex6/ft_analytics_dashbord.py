def ft_analytics_dashbord() -> None:
    players_info: list[dict] = [
        {
            "name": "alice",
            "score": 5300,
            "achievements": {"first_kill", "level_10", "speed_demon"},
            "active": True,
            "position": "north",
        },
        {
            "name": "bob",
            "score": 1800,
            "achievements": {"first_kill", "level_10", "boss_slayer"},
            "active": True,
            "position": "east",
        },
        {
            "name": "charlie",
            "score": 5150,
            "achievements": {
                "level_10",
                "treasure_hunter",
                "boss_slayer",
                "speed_demon",
            },
            "active": True,
            "position": "central",
        },
        {
            "name": "diana",
            "score": 2050,
            "achievements": {"level_10"},
            "active": False,
            "position": "central",
        }
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    high_scores = []
    double_scores = []
    active_players = []

    for player in players_info:
        double_scores.append(player["score"] * 2)
        if player["score"] > 2000:
            high_scores.append(player["name"])
        if player["active"] is True:
            active_players.append(player["name"])

    print(f"High scores (>2000): {high_scores}")
    print(f"Scores doubled: {double_scores}")
    print(f"Active playes: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores: dict[str, int] = {}

    categories = {
        "high": 0,
        "medium": 0,
        "low": 0,
    }

    medium_counter = 0
    high_counter = 0
    low_counter = 0

    for player in players_info:
        if player["active"] is True:
            player_scores.update({player["name"]: player["score"]})

        if player["score"] > 2000:
            high_counter += 1
            categories.update({"high": high_counter})
        elif 1500 <= player["score"] <= 2000:
            medium_counter += 1
            categories.update({"medium": medium_counter})
        else:
            low_counter += 1
            categories.update({"low": low_counter})

    print(f"Player scores : {player_scores}")
    print(f"Score categories: {categories}")

    achievements: dict[str, int] = {}

    for player in players_info:
        achievements.update({player["name"]: len(player["achievements"])})
    print(f"Achievements counts: {achievements}")

    print("\n=== Set Comprehension Examples ===")

    unique_players: set[str] = set()
    unique_achievements: set[str] = set()
    active_regions: set[str] = set()
    count_achievements = 0

    for player in players_info:
        unique_players.add(player["name"])
        if player["active"] is True:
            active_regions.add(player["position"])
        for ach in player["achievements"]:
            count_achievements += 1
            unique_achievements.add(ach)

    print(f"Unique players: {sorted(unique_players)}")
    print(f"Unique achievements: {sorted(unique_achievements)}")
    print(f"Active regions: {sorted(active_regions)}")

    print("\n=== Combined Analysis ===")
    total_players: int = len(players_info)
    total_score: int = 0

    for player in players_info:
        total_score += player["score"]

    top_name = players_info[0]["name"]
    top_score = players_info[0]["score"]
    top_ach = len(players_info[0]["achievements"])

    for player in players_info:
        if player["score"] > top_score:
            top_name = player["name"]
            top_score = player["score"]
            top_ach = len(player["achievements"])

    print(f"Total Players: {total_players}")
    print(f"Total unique achievements: {count_achievements}")
    print(f"Average score: {total_score / total_players}")
    print(
        f"Top performer: {top_name} "
        f"({top_score} points, {top_ach} achievements)"
    )


if __name__ == "__main__":
    ft_analytics_dashbord()
