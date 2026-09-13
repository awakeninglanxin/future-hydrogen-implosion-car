# -*- coding: utf-8 -*-
import os
import win32com.client
ROOT = r"D:/AAA我的文件/未来氢内爆汽车"
SRC = os.path.join(ROOT, "HHO书本精读", "矩阵-意识的几何语言 优化排版.doc")
OUT = os.path.join(ROOT, "_HHO书本提取", "矩阵_p540-558_分页.txt")
app = win32com.client.Dispatch("KWps.Application")
try: app.Visible = False
except Exception: pass
try: app.DisplayAlerts = 0
except Exception: pass
doc = app.Documents.Open(SRC)
total = int(doc.ComputeStatistics(2))
print("总页数:", total)
parts = []
for p in range(540, min(total, 559) + 1):
    r1 = doc.GoTo(1, 1, p)
    if p < total:
        r2 = doc.GoTo(1, 1, p + 1)
        t = doc.Range(r1.Start, r2.Start).Text
    else:
        t = doc.Range(r1.Start, doc.Content.End).Text
    parts.append("===== P%d（%d 字符）=====\n%s" % (p, len(t), t))
    print("P%d: %d 字符" % (p, len(t)))
open(OUT, "w", encoding="utf-8").write("\n".join(parts))
doc.Close(False)
app.Quit()
print("已写:", OUT)
