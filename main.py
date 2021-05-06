import argparse
import os
from colorama import Fore, init
import colorama
colorama.init()

class Format:
	def __init__(self, input_f, output_f, type_h):
		self.input_f = input_f
		self.output_f = output_f
		self.type_h = type_h
	
	def format(self):
		headers = {
			"jpg":bytes([0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46, 0x00, 0X01]
				),
			"gif":bytes([0x47, 0x49, 0x46, 0x38, 0x37, 0x61]
				),
			"png":bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]
			)}

		with open(self.input_f, "rb") as f:
			file_h = f.read()
			f.seek(0, 2)
			size_f = f.tell()

		with open(self.output_f, "wb") as f:
			overwrite_h = f.write(headers[self.type_h] + file_h) 

		print(f"{Fore.GREEN}")
		print("File name: %s" % (self.input_f))
		print("File size: %s" % (size_f))
		print("New headers: %s" % (headers[self.type_h]))
		print("Saved: %s" % (self.output_f))
		print(f"{Fore.RESET}")

def clear():
	os.system("cls" if os.name == "nt" else "clear")

def main():
	parser = argparse.ArgumentParser(description=("Magicheaders Editer"))
	parser.add_argument("-i", "--input", help="Input File/Image", required=True)
	parser.add_argument("-o", "--output", help="Output File/Image", required=True)
	parser.add_argument("-t", "--type", help="Magic Headers", required=True)
	args = parser.parse_args()

	if args.type == "jpg":
		clear()
		jpg = Format(args.input, args.output, args.type)
		jpg.format()

	elif args.type == "png":
		clear()
		png = Format(args.input, args.output, args.type)
		png.format()

	elif args.type == "gif":
		clear()
		gif = Format(args.input, args.output, args.type)
		gif.format()

if __name__ == "__main__":
	main()
