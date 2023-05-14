import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签

data: dict[str, list[float]] = {
    "wx4en": [5109.8438, 19037.3750, 5512.3125],
    "wx4ep": [5549.9688, 29426.7188, 5915.5938],
    "wx4eq": [6248.7500, 29318.7500, 6093.4688],
    "wx4er": [5109.0000, 17056.8125, 6336.8125],
    "区域索引链": [3695.3438, 52921.1719, 4412.3047],
    "仅wx4en": [3800.6250, 7938.7812, 4088.0000],
    "仅wx4ep": [3345.2188, 9134.1562, 4001.6875],
    "仅wx4eq": [4193.4062, 10965.1875, 4424.4375],
    "仅wx4er": [3415.0938, 7601.0625, 4127.4062],
}

# region_names: tuple[str, ...] = ("wx4en", "wx4ep", "wx4eq", "wx4er", "区域索引链",)
region_names: tuple[str, ...] = ("仅wx4en", "仅wx4ep", "仅wx4eq", "仅wx4er", "区域索引链",)
time_consumption = {
    "乘车请求提交耗时": np.array([data[each][0] for each in region_names]),
    "车辆分配耗时": np.array([data[each][1] for each in region_names]),
    "到达并付款耗时": np.array([data[each][2] for each in region_names]),
}
width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(len(region_names))

for boolean, weight_count in time_consumption.items():
    p = ax.bar(region_names, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count
    ax.bar_label(p, label_type="center")

ax.set_title("出租车调度系统乘客端各阶段平均耗时对比(子链单独运转)")
ax.set_ylabel("耗时(ms)")
ax.legend(loc="upper left")

plt.show()
