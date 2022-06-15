import os
from time import sleep


def clear_screen() -> None:
	if os.name == "posix":
		os.system("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system("cls")


def is_int(x) -> bool:
	return x % 1 == 0


def draw_triangle(rows: int, hs: int, vs: int) -> None:
	for i in range(rows + 1):
		margin = " " * (rows - i) * (hs + 1)
		qty_items = 2 * i - 1
		item = "*" + hs * " "
		row = margin + qty_items * item

		print(row, end="")
		print(vs * "\n")


def elastic_triangle(rows: int = 5, hms: int = 3, vs: int = 1, assc = 0.5) -> None:
	if not is_int(rows) or rows <= 0:
		return

	if not is_int(hms) or hms < 0:
		return

	if not is_int(vs) or vs < 0:
		return

	if assc <= 0:
		return

	i = 0

	while True:
		i += 1
		hs = i % (int(hms) + 1)
		draw_triangle(int(rows), int(hs), int(vs))
		sleep(assc)
		clear_screen()

			
def main() -> None:
	rows = 5
	horizontal_max_separation = 3.0
	vertical_separation = 1
	animation_speed_seconds = 0.5

	elastic_triangle(rows, horizontal_max_separation, vertical_separation, animation_speed_seconds)


main()
		