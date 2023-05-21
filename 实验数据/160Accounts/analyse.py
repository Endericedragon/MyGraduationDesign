start_time: int = 1681712431

with open("tx_result_w11.txt", "r", encoding="utf-8") as f:
    end_times: list[int] = [int(each.split()[1].strip()) for each in f.readlines()]

end_times.sort()
end_times.insert(0, start_time)

delta: list[int] = []
for i in range(1, len(end_times)):
    delta.append(end_times[i] - end_times[i-1])

average = sum(delta) / len(delta)
print(average)

