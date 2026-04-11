import json
import argparse
from time import sleep

# gsl - Game State Log
# gsllin - Tellin the gels

USAGE = """python3 gsl.py -x <type>
type: ["player", "asteroid", "asteroidfield", "shot"]

"""

parser = argparse.ArgumentParser(usage=USAGE)
parser.add_argument(
    "-x", "--exclude", action="append", type=str, help="type to exclude"
)
args = parser.parse_args()
print(args.exclude)
## Open file of state logs
with open("./game_state.jsonl", "r") as in_f:
    lines = [line.rstrip() for line in in_f.readlines()]
    print("a line - ", lines[0])
    json_logs = [json.loads(line) for line in lines]

    exclusions = [arg.lower() for arg in args.exclude]
    ## For event print the seconds elapsed and the updatables, minus exclusions
    for event in json_logs:
        print(" Seconds elapsed: --> ", event["elapsed_s"], " <-- ")
        print("====================================")

        print("===Updatable===")
        for item in event["updatable"]["sprites"]:
            if item["type"].lower() in exclusions:
                continue

            print("\ttype: ", item["type"])

            print("\tvel: ", item.get("vel", "No velocity"))
            print("\tpos: ", item.get("pos", "No pos"))
            print("\trot: ", item.get("rot", "No rot"))
        print("====================================")
        print("sleeping...")
        sleep(1)
exit()
