from ExtensionAnalyzer import compare_file_extension

def main():
    print("=== File Analyzer CLI ===")
    print("Enter the path of a file to analyze.\n")

    while True:
        file_path = input("File path (or 'q' to quit): ").strip()

        if file_path.lower() in ("q", "quit", "exit"):
            print("Exiting analyzer.")
            break

        try:
            result = compare_file_extension(file_path)

            print("\n--- Analysis Result ---")
            print(f"File:               {result['file']}")
            print(f"Declared extension: {result['extension_claim']}")
            print(f"Detected header:    {result['detected_header']}")
            print(f"Match:              {result['match']}")
            print("------------------------\n")

        except FileNotFoundError:
            print("[Error] File not found. Try again.\n")
        except PermissionError:
            print("[Error] Permission denied. Try again.\n")
        except Exception as e:
            print(f"[Error] Unexpected error: {e}\n")

if __name__ == "__main__":
    main()
