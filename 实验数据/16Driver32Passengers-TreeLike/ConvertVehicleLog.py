from collections import defaultdict
import json
import os
import sys


class Event:
    def __init__(self, event_type: str, driver: str, timestamp: int):
        self.type: str = event_type
        self.driver: str = driver
        self.timestamp: int = timestamp
        self.passenger: str = ""


def main():
    for file in sys.argv[1:]:
    # for file in ["log_vehicle_wx4en.log"]:
        logs: defaultdict[str, list[Event]] = defaultdict(list)
        filename, _ = os.path.splitext(file)
        with open(file, "r", encoding="utf-8") as f:
            while line := f.readline():
                elements = line.split('@')
                event = Event(
                    elements[3].strip(),
                    elements[2],
                    int(elements[0]),
                )
                if event.type == "PickUp":
                    event.passenger = elements[-1][:40]
                logs[elements[2]].append(event)

        res: defaultdict[str, dict[str, dict[str, int]]] = defaultdict(dict)
        for driver_addr, events in logs.items():
            passenger_addr: str = ""
            i: int = 1
            while i < len(events):
                if events[i].type == "PickUp":
                    passenger_addr = events[i].passenger
                    res[driver_addr][passenger_addr] = dict()
                    i += 1
                    while True:
                        res[driver_addr][passenger_addr][events[i].type] = events[i].timestamp - events[i - 1].timestamp
                        i += 1
                        if i >= len(events) or events[i].type == "PickUp":
                            break
            # for i in range(1, len(events)):
            #     res[driver_addr][events[i].type] = events[i].timestamp - events[i - 1].timestamp

        with open(f"{filename}.json", "w") as f:
            json.dump(res, f, indent=4)


if __name__ == "__main__":
    main()
