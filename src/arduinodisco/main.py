from arduinodisco import discover_boards

def main():
    for entry in discover_boards():
        #if entry.board is None:
        #    continue
        print(
            entry.port.device,
            entry.board.name if entry.board else "Unknown",
            entry.board.fqbn if entry.board else "-",
            entry.reason
        )

if __name__ == "__main__":
    main()