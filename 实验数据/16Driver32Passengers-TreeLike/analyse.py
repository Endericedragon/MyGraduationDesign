"""
乘车请求提交耗时 = StartingPointWrittenToContract + DestinationWrittenToContract +
                   GettingNearbyRegions(原名FoundIdleCarsNearby) + FoundTheMostNearbyCar
分配车辆耗时 = TheMostNearbyCarConflict(若有) + RepeatlyFoundTheMostNearbyCar(若有) + TheMostNearbyCarIsSelected + PassengerOnBoard
确认到达并支付耗时 = PassengerArriveAtDestination + PassengerPaysAndGetsOff
"""
import json
import os

# file_path: str = os.path.join("实验数据", "8司机16乘客-树状")
file_path = os.path.join("实验数据", "16Driver32Passengers-TreeLike")
passenger_filename_prefix: str = "log_passenger_%s.json"
regions: tuple[str, ...] = (
    "wx4en", "wx4ep", "wx4eq", "wx4er", "all",
    "wx4en_only", "wx4ep_only", "wx4eq_only", "wx4er_only"
)

print("Region\trequest_time\t\tdispatch_time\t\tarrive_pay_time")
for region in regions:
    passenger_filename = passenger_filename_prefix % (region, )
    with open(os.path.join(file_path, passenger_filename), "r", encoding="utf-8") as f:
        obj = json.load(f)
        counter: int = 0
        request_time: int = 0
        dispatch_time: int = 0
        arrive_pay_time: int = 0
        for (_, info) in obj.items():
            counter += 1
            request_time += info["StartingPointWrittenToContract"] \
                + info["DestinationWrittenToContract"] \
                + info.get("GettingNearbyRegions", info.get("FoundIdleCarsNearby", "")) \
                + info["FoundTheMostNearbyCar"]
            dispatch_time += info.get("TheMostNearbyCarConflict", 0) \
                + info.get("RepeatlyFoundTheMostNearbyCar", 0) \
                + info["TheMostNearbyCarIsSelected"] \
                + info["PassengerOnBoard"]
            arrive_pay_time += info["PassengerArriveAtDestination"] \
                + info["PassengerPaysAndGetsOff"]
        print(
            f"{region}\t\t{request_time / counter: .04f}\t\t{dispatch_time / counter:.04f}\t\t{arrive_pay_time / counter:.04f}",
        )
