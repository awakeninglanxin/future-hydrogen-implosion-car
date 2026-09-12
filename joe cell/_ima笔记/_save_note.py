# -*- coding: utf-8 -*-
"""把 agent-browser eval 导出的 JSON 字符串落成干净的纯文本快照。"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "_raw.json")
OUT = os.path.join(BASE, "20260912_ima笔记_H2分子组合方式_原文快照.txt")

raw = open(RAW, "r", encoding="utf-8", errors="replace").read().strip()
try:
    text = json.loads(raw)
except Exception as exc:  # 保底：原样落盘
    print("json 解析失败，原样落盘：", exc)
    text = raw

header = (
    "《H₂ 的组合方式：不是两个相同的变体，而是各取其一（Variety 1 + Variety 2）》\n"
    "来源：ima 笔记分享页\n"
    "分享链接：https://ima.qq.com/note/share/_A0YMbGP9gqeKZMQZlNhMQ?channel=4\n"
    "创建人：🙏明锜🤲\n"
    "更新时间：2026.09.12 09:13\n"
    "抓取方式：agent-browser 渲染 + eval document.body.innerText\n"
    "抓取时间：2026-09-12\n"
    "=" * 72 + "\n\n"
)

with open(OUT, "w", encoding="utf-8", newline="\r\n") as fh:
    fh.write(header + text + "\n")

print("已写出：", OUT)
print("字符数 =", len(text))
