# -*- coding: utf-8 -*-
"""提取《矩阵-意识的几何语言 优化排版.doc》：
   - 全文 + 头部识别信息
   - 关键词页码定位（以西结/飞碟/外星/内爆/飞行器）
   - p538-566 区段文本（对老师给的 p544/p552 提示）
   只读打开（WPS COM，失败回退 Word COM）。"""
import sys, os, time
import win32com.client

ROOT = r"D:\AAA我的文件\未来氢内爆汽车"
SRC = os.path.join(ROOT, "HHO书本精读", "矩阵-意识的几何语言 优化排版.doc")
OUTDIR = os.path.join(ROOT, "_HHO书本提取")
os.makedirs(OUTDIR, exist_ok=True)
OUT_FULL = os.path.join(OUTDIR, "矩阵-意识的几何语言_全文.txt")
OUT_SEG = os.path.join(OUTDIR, "矩阵_p538-566.txt")
OUT_HEAD = os.path.join(OUTDIR, "矩阵_头部识别.txt")

def log(m):
    print(m, flush=True)

app = None
for progid in ["KWps.Application", "wps.Application", "Word.Application"]:
    try:
        app = win32com.client.Dispatch(progid)
        log("COM 接口 OK: " + progid)
        break
    except Exception as e:
        log("COM 失败 %s: %s" % (progid, str(e)[:120]))
if app is None:
    sys.exit("无可用 COM 接口")

try: app.Visible = False
except Exception: pass
try: app.DisplayAlerts = 0
except Exception: pass

t0 = time.time()
doc = app.Documents.Open(SRC)
log("打开完成 %.1fs" % (time.time() - t0))
try:
    log("页数: %s" % doc.ComputeStatistics(2))
except Exception as e:
    log("页数统计失败: %s" % e)

# 文档属性（找原书名线索）
try:
    for pi in ["Title", "Subject", "Author", "Last Author", "Company"]:
        try:
            v = doc.BuiltInDocumentProperties(pi).Value
            log("属性 %s: %r" % (pi, v))
        except Exception:
            pass
except Exception as e:
    log("属性块失败: %s" % e)

# 1) 全文 + 头部
full = doc.Content.Text
log("全文长度: %d 字符" % len(full))
open(OUT_HEAD, "w", encoding="utf-8").write(full[:2600])
open(OUT_FULL, "w", encoding="utf-8").write(full)
log("已写: %s" % OUT_FULL)

# 2) 关键词页码
for kw in ["以西结", "飞碟", "外星", "内爆", "飞行器"]:
    try:
        rng = doc.Content
        f = rng.Find
        f.Text = kw
        f.Forward = True
        f.Wrap = 0
        pages, guard = [], 0
        while f.Execute() and guard < 100:
            guard += 1
            pages.append(int(rng.Information(3)))
            rng.Collapse(0)
            f = rng.Find
            f.Text = kw
            f.Forward = True
            f.Wrap = 0
        log("「%s」共 %d 处  页码: %s" % (kw, len(pages), pages[:60]))
    except Exception as e:
        log("搜索 %s 出错: %s" % (kw, e))

# 3) p538-566 区段
try:
    start = doc.GoTo(1, 1, 538).Start
    end = doc.GoTo(1, 1, 566).End
    seg = doc.Range(start, end).Text
    open(OUT_SEG, "w", encoding="utf-8").write(seg)
    log("p538-566 区段: %d 字符 -> %s" % (len(seg), OUT_SEG))
except Exception as e:
    log("区段提取失败: %s" % e)

doc.Close(False)
app.Quit()
log("DONE")
