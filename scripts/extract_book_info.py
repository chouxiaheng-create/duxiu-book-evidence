#!/usr/bin/env python3
"""从读秀 URL 中提取书目信息（页码、dxNumber 等）。

用法：
    python extract_book_info.py <duxiu_url_or_query_string>

示例：
    python extract_book_info.py "https://qw.duxiu.com/goreadqw.jsp?kid=...&pagenum=468&epage=468&spgno=468&dxNumber=000000584475&zjid=..."
    python extract_book_info.py "pagenum=468&epage=468&spgno=468&dxNumber=000000584475"

输出：JSON 格式的书目信息
"""

import sys
import re
import json
from urllib.parse import urlparse, parse_qs, unquote


def extract_from_url(url: str) -> dict:
    """从读秀 URL 中提取书目信息。"""
    info = {}

    # 解析 URL 查询参数
    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    # 提取各字段
    if "pagenum" in params:
        info["起始页"] = int(params["pagenum"][0])
    if "epage" in params:
        info["终止页"] = int(params["epage"][0])
    if "spgno" in params:
        info["命中页"] = int(params["spgno"][0])
    if "dxNumber" in params:
        info["读秀标识"] = params["dxNumber"][0]
    if "zjid" in params:
        info["章节标识"] = params["zjid"][0]
    if "sch" in params:
        info["章节标题"] = unquote(params["sch"][0])
    if "sKey" in params:
        info["检索关键词"] = unquote(params["sKey"][0])
    if "qwkey" in params:
        info["全文键"] = params["qwkey"][0]
    if "kid" in params:
        info["资源标识"] = params["kid"][0]

    # 计算页码范围
    if "起始页" in info and "终止页" in info:
        if info["起始页"] == info["终止页"]:
            info["页码范围"] = f"第{info['起始页']}页"
        else:
            info["页码范围"] = f"第{info['起始页']}-{info['终止页']}页"

    return info


def extract_from_query_string(qs: str) -> dict:
    """从纯查询字符串中提取书目信息。"""
    if not qs.startswith("http"):
        qs = "?" + qs
    return extract_from_url("https://qw.duxiu.com/goreadqw.jsp" + qs)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    arg = sys.argv[1]

    if arg.startswith("http"):
        info = extract_from_url(arg)
    else:
        info = extract_from_query_string(arg)

    if info:
        print(json.dumps(info, ensure_ascii=False, indent=2))
    else:
        print("未从输入中提取到书目信息。请检查 URL 或查询字符串格式。")
        sys.exit(1)


if __name__ == "__main__":
    main()
