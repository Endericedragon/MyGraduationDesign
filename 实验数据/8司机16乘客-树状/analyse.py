"""
乘车请求提交耗时 = StartingPointWrittenToContract + DestinationWrittenToContract + FoundIdleCarsNearby
分配车辆耗时 = FoundTheMostNearbyCar + TheMostNearbyCarConflict(若有) + TheMostNearbyCarIsSelected + PassengerOnBoard
确认到达并支付耗时 = PassengerArriveAtDestination + PassengerPaysAndGetsOff
"""
import json
import os

print(os.getcwd())
file_path = os.path.join("实验数据", "8司机16乘客-树状")
passenger_filename = "log_passenger_wx4er.json"

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
            + info["FoundIdleCarsNearby"]
        dispatch_time += info["FoundTheMostNearbyCar"] \
            + info.get("TheMostNearbyCarConflict", 0) \
            + info["TheMostNearbyCarIsSelected"] \
            + info["PassengerOnBoard"]
        arrive_pay_time += info["PassengerArriveAtDestination"] \
            + info["PassengerPaysAndGetsOff"]
    print(request_time / counter, dispatch_time / counter, arrive_pay_time / counter)

