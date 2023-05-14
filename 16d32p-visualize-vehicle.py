import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签

data: dict[str, list[float]] = {
    "wx4en(并行)": [2412.0000, 5429.1250, 2796.4062],
    "wx4ep(并行)": [2567.1562, 5534.2500, 2989.0625],
    "wx4eq(并行)": [2875.5000, 6039.2812, 3154.1562],
    "wx4er(并行)": [3045.7500, 6011.4688, 3064.4062],
    "wx4en(单独)": [1902.6250, 4006.3750, 2280.3125],
    "wx4ep(单独)": [1930.0000, 4022.4688, 2051.9062],
    "wx4eq(单独)": [2185.6875, 4633.6250, 2065.3438],
    "wx4er(单独)": [2023.4688, 4186.8125, 1742.6875],
    "区域索引链": [2225.0859, 4432.6953, 2167.7422],
}

region_names: tuple[str, ...] = (
    "wx4en(并行)", "wx4ep(并行)", "wx4eq(并行)", "wx4er(并行)", "wx4en(单独)", "wx4ep(单独)", "wx4eq(单独)", "wx4er(单独)", "区域索引链",)
# region_names: tuple[str, ...] = ("仅wx4en", "仅wx4ep", "仅wx4eq", "仅wx4er", "区域索引链",)
time_consumption = {
    "接单并导航至上车点耗时": np.array([data[each][0] for each in region_names]),
    "导航至目的地耗时": np.array([data[each][1] for each in region_names]),
    "确认乘客下车并付款耗时": np.array([data[each][2] for each in region_names]),
}
width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(len(region_names))

for boolean, weight_count in time_consumption.items():
    p = ax.bar(region_names, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count
    ax.bar_label(p, label_type="center")

ax.set_title("出租车调度系统司机端各阶段平均耗时对比")
ax.set_ylabel("耗时(ms)")
ax.legend(loc="upper left")

plt.show()
