import Flattener
import os

def main():
    print("Welcome to PDF Flattener.")
    input_path = input("Please enter the path of the PDF file: ")

    output_path = input_path

    while True:
        match input("Do you want to overwrite this file [Y/N]:\n"):
            case "N":
                output_path = input("Please enter the path of the output PDF file: ")
                break
            case "n":
                output_path = input("Please enter the path of the output PDF file: ")
                break
            case "Y":
                break
            case "y":
                break
            case _:
                continue

    try:
        Flattener.flatten_pdf(input_path, output_path)
    except FileNotFoundError:
        print("Path does not exist.")
        main()

main()