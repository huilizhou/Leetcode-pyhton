d = {"ok": 1, "no": 2, "hah": 1}
d1 = sorted(d.items(), key=lambda d: d[1], reverse=True)
print(d1)
