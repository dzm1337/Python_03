from sys import argv

def info_argv():
	print("=== Command Quest ===")
	total_arg = len(argv)
	program_name = print(f"Program name: {argv[0]}")

	if (total_arg == 1):
		print("No arguments provided!")
		program_name
	else:
		program_name
		print(f"Arguments received : {total_arg - 1}")
		i = 1
		for arg in argv[1:]:
			print(f"Argument {i}: {argv[i]}")
			i = i + 1
	print(f"Total Arguments: {total_arg}")
info_argv()
