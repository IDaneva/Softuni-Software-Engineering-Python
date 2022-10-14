text = input()
ch_times = {}

for ch in text:
    if ch not in ch_times:
        ch_times[ch] = 0
    ch_times[ch] += 1

for key in sorted(ch_times):
    print(f"{key}: {ch_times[key]} time/s")
