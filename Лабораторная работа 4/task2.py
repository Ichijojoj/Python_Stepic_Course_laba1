import json

def task() -> float:
    FILENAME = "input.json"

    with open(FILENAME) as f:
        json_data = json.load(f)

    total_sum = sum(item["score"] * item["weight"] for item in json_data)
    return round(total_sum, 3)

if __name__ == '__main__':
    result = task()
    print(result)
