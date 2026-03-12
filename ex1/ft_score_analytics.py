from sys import argv

def score_parser(scores: list[str]) -> bool:
	args_len: int = len(argv)
	if (args_len == 1):
		print(f"No scores provided. Usage: python3 {argv[0]} <score1> <score2> ...")
		return
	try:
		for arg in argv[1:]:
			int(arg)
			scores.append(int(arg))
	except ValueError:
		print(f"Error: {arg} is not a valid number!")
		return
	return True

def display_info_scores() -> None:
	scores = []
	print("=== Player Score Analytics ===")
	if score_parser(scores) == True:
		sum_score: int = sum(scores)
		len_score: int = len(scores)
		print(f"""Scores processed: {scores}
Total Players: {len_score}
Total score: {sum_score}
Average score: {sum_score / len_score}
High score: {max(scores)}
Low score: {min(scores)}
Score range: {max(scores) - min(scores)}\n""")
display_info_scores()
