from pathlib import Path

from src.graph import app


def main():
    file_path = input(
        "Enter the path of your .txt file: "
    ).strip().strip('"')

    path = Path(file_path)

    if not path.is_file():
        print("Error: File not found.")
        return

    if path.suffix.lower() != ".txt":
        print("Error: Please upload a .txt file.")
        return

    try:
        text = path.read_text(encoding="utf-8").strip()

        if not text:
            print("Error: The text file is empty.")
            return

        result = app.invoke({
            "text": text
        })

        print("\n===== SUMMARY =====")
        print(result["result"])

    except UnicodeDecodeError:
        print("Error: The file must use UTF-8 text encoding.")
    except OSError as error:
        print(f"Error reading file: {error}")


if __name__ == "__main__":
    main()