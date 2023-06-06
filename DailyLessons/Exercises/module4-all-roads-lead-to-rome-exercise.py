connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
rome_list = 0
times = 0
for con in connections:
    if con[1] == 'Rome':
        rome_list += 1
        times += con[2]
av_fl_tm = times / rome_list
print(rome_list, 'connections lead to Rome with and average flight time of', av_fl_tm, 'minutes')








