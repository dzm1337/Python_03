def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    alice_achievements = {
        'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'
    }
    bob_achievements = {
        'first_kill', 'level_10', 'boss_slayer', 'collector'
    }
    charlie_achievements = {
        'level_10', 'treasure_hunter', 'boss_slayer',
        'speed_demon', 'perfectionist'
    }

    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}")

    print("\n=== Achievement Analytics ===")

    unique_achievements: set = (
        alice_achievements | bob_achievements | charlie_achievements
    )

    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")

    common_achievements: set = (
        alice_achievements & bob_achievements & charlie_achievements
    )

    print(f"\nCommon to all players: {common_achievements}")

    rare_charlie: set = (
        charlie_achievements - bob_achievements - alice_achievements
    )
    rare_bob: set = (
        bob_achievements - charlie_achievements - alice_achievements
    )
    rare_achievements: set = rare_charlie | rare_bob

    print(f"Rare achievements: {rare_achievements}")

    print(f"\nAlice vs Bob common: {alice_achievements & bob_achievements}")
    print(f"Alice unique: {alice_achievements - bob_achievements}")
    print(f"Bob unique: {bob_achievements - alice_achievements}")


if __name__ == "__main__":
    ft_achievement_tracker()
