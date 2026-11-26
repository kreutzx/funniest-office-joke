import os

ENTRY = "Our CEO called us family 11 times in Monday's all-hands, then laid off 23 of us by Friday — my exit email's subject line: 'A difficult family decision.'"


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
