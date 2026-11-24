import os

TEXT = "Today in Gloomburg: scattered showers, highs of 11, and a 90% chance the bus is late again. Pack an umbrella and low expectations."

def main():
    assert 1 <= len(TEXT) <= 140, len(TEXT)
    assert TEXT.strip(), "entry must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
