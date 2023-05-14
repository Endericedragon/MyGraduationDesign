from collections import defaultdict
import json
import os
import sys


class Event:
    def __init__(self, event_type: str, initiator: str, timestamp: int):
        self.type: str = event_type
        self.initiator: str = initiator
        self.timestamp: int = timestamp


def main():
    for file in sys.argv[1:]:
        logs: defaultdict[str, list[Event]] = defaultdict(list)
        filename, _ = os.path.splitext(file)
        with open(file, "r", encoding="utf-8") as f:
            while line := f.readline():
                elements = line.split('@')
                logs[elements[2]].append(Event(
                    elements[-1].strip(),
                    elements[2],
                    int(elements[0]),
                ))

        res: dict[str, dict[str, int]] = dict()
        for account_addr, events in logs.items():
            res[account_addr] = defaultdict(int)
            is_first_dispatch: bool = True
            for i in range(1, len(events)):
                if events[i].type == "FoundTheMostNearbyCar":
                    if is_first_dispatch:
                        is_first_dispatch = False
                        res[account_addr]["FoundTheMostNearbyCar"] = events[i].timestamp - events[i - 1].timestamp
                    else:
                        res[account_addr]["RepeatlyFoundTheMostNearbyCar"] += events[i].timestamp - events[i - 1].timestamp
                elif events[i].type == "TheMostNearbyCarConflict":
                    res[account_addr][events[i].type] += events[i].timestamp - events[i - 1].timestamp
                else:
                    res[account_addr][events[i].type] = events[i].timestamp - events[i - 1].timestamp

        with open(f"{filename}.json", "w") as f:
            json.dump(res, f, indent=4)


if __name__ == "__main__":
    main()
