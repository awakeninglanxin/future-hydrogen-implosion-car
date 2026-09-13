# -*- coding: utf-8 -*-
"""YouTube 代理哨兵：定期检测沙箱代理通道，一旦恢复自动下载磁现象系列字幕。

背景（2026-09-13 16:0x）：
- 沙箱代理 http://127.0.0.1:15748 故障（先是 502 Bad Gateway，后为超时 000）
- 本机无其他翻墙通路（无代理软件/无 TUN 网卡/直连被墙）
- 本哨兵定期探测，恢复后自动续传 8 条磁现象系列字幕
"""
import subprocess, time, sys, os

PROXY = "http://127.0.0.1:15748"
WORKDIR = r"D:/AAA我的文件/未来氢内爆汽车/joe cell/_外部访谈资料/youtube视频字幕"
URLS_FILE = "_urls_batch6.txt"
LOG = r"D:/AAA我的文件/未来氢内爆汽车/_youtube_哨兵_log.txt"
PY = r"D:/Program Files/Python312/python.exe"
TOOL = r"D:/AAA我的文件/youtube视频+字幕下载工具/yt_subtitle_extractor.py"

def log(msg):
    line = "[" + time.strftime("%H:%M:%S") + "] " + msg
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def check_proxy():
    try:
        r = subprocess.run(
            ["curl", "-sI", "--max-time", "10", "-x", PROXY, "https://www.youtube.com/",
             "-o", os.devnull, "-w", "%{http_code}"],
            capture_output=True, timeout=25)
        code = r.stdout.decode("utf-8", errors="replace").strip()
        return code in ("200", "301", "302", "303")
    except Exception:
        return False

MAX_ATTEMPTS = 25
INTERVAL = 55

log("=" * 56)
log("哨兵启动：最多 %d 次检测，间隔 %d 秒（覆盖约 %d 分钟）" % (
    MAX_ATTEMPTS, INTERVAL, MAX_ATTEMPTS * INTERVAL // 60))

for i in range(1, MAX_ATTEMPTS + 1):
    if check_proxy():
        log("★★★ 代理已恢复！开始下载 8 条磁现象系列字幕...")
        try:
            r = subprocess.run(
                [PY, "-X", "utf8", TOOL, URLS_FILE, "--batch", "-s", "en", "-o", "."],
                cwd=WORKDIR, capture_output=True, timeout=900)
            out = r.stdout.decode("utf-8", errors="replace")
            log("下载输出（末 30 行）：")
            for line in out.split("\n")[-30:]:
                log("  " + line)
        except Exception as e:
            log("下载异常: " + str(e)[:300])
        log("哨兵任务结束")
        sys.exit(0)
    else:
        log("第 %d/%d 次检测：代理未恢复" % (i, MAX_ATTEMPTS))
    if i < MAX_ATTEMPTS:
        time.sleep(INTERVAL)

log("哨兵超时退出：%d 次检测均未恢复（约 %d 分钟）" % (MAX_ATTEMPTS, MAX_ATTEMPTS * INTERVAL // 60))
