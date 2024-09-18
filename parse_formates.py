import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='')
    parser.add_argument('--input', default='')
    return parser.parse_args()


def main():
    args = parse_args()
    tokens = []
    with open(args.input + "det.txt", "r") as f:
        data = f.read()
        lines = data.split("\n")
    content = {}
    for line in lines:
        tokens = line.split(",")
        if len(tokens) < 6:
            continue
        line_num = tokens[0]
        items = content.get(line_num, [])
        coords = tokens[2:]
        result = line_num + "," + ",".join(coords)
        items.append(result)
        content[line_num] = items

    for line_num in content:
        filename = "0" * (6 - len(line_num)) + line_num + ".txt"
        file_content = "\n".join(content[line_num])
        with open(args.input + filename, "w") as f:
            f.write(file_content)


if __name__ == '__main__':
    main()
