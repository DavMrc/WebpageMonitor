import argparse
import sys

from gui import Gui
from checker import Checker
from monitor import Monitor


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--gui', help='Activates the gui. Default: false', action='store_true')
	parser.add_argument('--from-yaml', help='Reads the parameters from the specified YAML file',
						required=False, type=str, metavar='PATH_TO_YAML')
	args = parser.parse_args()

	if args.gui:
		gui = Gui()
		gui.mainloop()
	else:
		try:
			if args.from_yaml:
				params = Checker.check_yaml(args.from_yaml)
			else:
				params = Checker.check_input()
			
			monitor = Monitor(params)
			monitor.start_sync()
			monitor.join()

		except KeyboardInterrupt:
			sys.exit(1)
		except FileNotFoundError:
			print(f"YAML file '{args.from_yaml}' could not be found.")
		except TypeError as e:
			if str(e) == "cannot unpack non-iterable NoneType object":
				print("There were errors in the YAML file. Check the input file and correct the errors.")


if __name__ == "__main__":
	main()