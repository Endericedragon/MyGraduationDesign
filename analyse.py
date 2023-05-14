"""
接单并导航至上车点耗时 = FinishedAStarToStartingPoint + StoreRouteToStartingPointThroughAStarSuccess
导航至目的地耗时 = DestinationReady + FinishedAStarToDestination + StoreRouteToDestinationSuccess
确认乘客下车并付款耗时 = PassengerPaid + CarReleased
"""
import json
import os

# file_path: str = os.path.join("实验数据", "8司机16乘客-树状")
file_path = os.path.join("实验数据", "16Driver32Passengers-TreeLike")
passenger_filename_prefix: str = "log_vehicle_%s.json"
regions: tuple[str, ...] = (
    "wx4en", "wx4ep", "wx4eq", "wx4er", "all",
    "wx4en_only", "wx4ep_only", "wx4eq_only", "wx4er_only"
)

print("Region\t\tclaim_order\t\tgoto_dest\t\tget_off")
for region in regions:
    passenger_filename = passenger_filename_prefix % (region, )
    with open(os.path.join(file_path, passenger_filename), "r", encoding="utf-8") as f:
        obj = json.load(f)
        counter: int = 0
        claim_order: int = 0
        goto_dest: int = 0
        get_off: int = 0
        for (_, info) in obj.items():
            for (_, info) in info.items():
                # print(info)
                counter += 1
                claim_order += info["FinishedAStarToStartingPoint"] \
                    + info["StoreRouteToStartingPointThroughAStarSuccess"]
                goto_dest += info["DestinationReady"] \
                    + info["FinishedAStarToDestination"] \
                    + info["StoreRouteToDestinationSuccess"]
                get_off += info["PassengerPaid"] \
                    + info["CarReleased"]
        print(
            f"{region}\t\t{claim_order / counter: .04f}\t\t{goto_dest / counter:.04f}\t\t{get_off / counter:.04f}",
        )
