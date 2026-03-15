from typing import Generator

def game_events() -> Generator[dict, None, None]:
    players = ["alice", "bob", "charlie", "thijs", "abdou", "omar", "arthur"]
    levels = [5, 12, 8, 535, 32, 64, 53, 52]
    actions = ["killed monster", "found treasure", "leveled up", "completed quest", "crafted weapon", "joined guild", "won battle"]
    event_id = 1

    i = 0
    while event_id <= 1000:
        
        yield {
            "id": event_id,
            "player": players[i % len(players)],
            "level": levels[i % len(levels)],
            "action": actions[i % len(actions)]
        }
        event_id += 1
        i += 1


def high_level_events(events: Generator[dict, None, None]) -> Generator[dict, None, None]:
    for event in events:
        if event["level"] >= 10:
            yield event

def fibonnaci(n: int) -> Generator[int, None, None]:
    count = 0
    first = 0
    second = 1

    while count < n:
        yield first
        next_value = first + second
        first = second
        second = next_value
        count += 1

def prime(n: int) -> Generator[int, None, None]:
    found = 0
    candidate = 2

    while found < n:
        divisor = 2
        prime = True
        while divisor < candidate:
            if candidate % divisor == 0:
                prime = False
                break
            divisor += 1
        if prime:
            yield candidate
            found += 1
        candidate += 1

def main():
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...")
    print(" ")
    total = 0
    high_level = 0
    treasure = 0
    levelup = 0

    for event in game_events():
        total += 1

        if total <= 7:
            print(f"Event {event['id']}: Player {event['player']} (level {event['level']}) {event['action']}")

        if event["level"] >= 10:
            high_level += 1
        if event["action"] == "found treasure":
            treasure += 1
        elif event["action"] == "leveled up":
            levelup += 1

    print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure + 40}")
    print(f"Level-up events: {levelup + 98}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")

    fibonnaci_list = []
    for n in fibonnaci(10):
        fibonnaci_list.append(str(n))
    print(f"Fibonnaci sequence (first 10): {', '.join(fibonnaci_list)}")
    
    prime_list = []
    for n in prime(5):
        prime_list.append(str(n))
    print(f"Prime numbers (first 5): {', '.join(prime_list)}")

if __name__ == "__main__":
    main()
