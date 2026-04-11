import json

# gsl - Game State Log
# gsllin - Tellin the gels

with open("./game_state.jsonl", "r") as in_f:
    lines = [line.rstrip() for line in in_f.readlines()]
    print("a line - ", lines[0])
    json_logs = [json.loads(line) for line in lines]

    for log in json_logs:
        print(json.dumps(log, indent=2))


exit()
