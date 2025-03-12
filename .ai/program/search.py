#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DuckDuckGo を利用した Web 検索、上位5件の URL 情報取得、各 URL から情報を抜き出すサンプルコード。

必要なライブラリ:
    pip install duckduckgo_search beautifulsoup4 requests
"""

import argparse
from googlesearch import search
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

def search_google(query, num_results=5, search_sites=5):
    """
    Google で検索し、上位 num_results 件の結果を返す。
    search_sites で検索するサイト数を指定
    戻り値は各結果が辞書形式で格納されたリスト。
    """
    results = []
    for url in search(query, num_results=search_sites): # using google package's search function
        results.append({'href': url})  # title is not available in google search
    return results[:num_results] # limit results to num_results


def search_duckduckgo(query, num_results=5):
    """
    DuckDuckGo で検索し、上位 num_results 件の結果を返す。
    戻り値は各結果が辞書形式で格納されたリスト。
    """
    ddgs = DDGS()
    results = list(ddgs.text(query, max_results=num_results)) # using duckduckgo_search package
    if not results:
        return []
    return results

def extract_text_from_url(url, keep_tags=False, max_chars=None):
    """
    指定された URL に接続し、Web ページからテキスト情報を抽出する。
    スクリプトやスタイルタグの除去も行う。
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        if not keep_tags:
            # 不要なタグを削除
            for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
                tag.decompose()

        # ページ内テキストを取得
        text = soup.get_text(separator="\n")
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        text = "\n".join(lines)

        if max_chars is not None:
            text = text[:max_chars]

        return text
    except Exception as e:
        print(f"URL取得エラー: {url}\\nエラー: {e}")
        return ""

def main():
    parser = argparse.ArgumentParser(description="Web search and URL information extraction tool.")
    parser.add_argument("keyword", help="Search keyword")
    parser.add_argument("-n", "--num_results", type=int, default=5, help="Number of search results to fetch (default: 5)")
    parser.add_argument("-e", "--search_engine", type=str, default="google", choices=['google', 'duckduckgo'], help="Search engine to use (google or duckduckgo, default: duckduckgo)")
    parser.add_argument("-ss", "--search_sites", type=int, default=5, help="Number of search sites to consider (only for google, default: 5)")
    parser.add_argument("-c", "--max_chars", type=int, default=1000, help="Maximum characters to extract from each URL (default: 1000)")
    parser.add_argument("--keep_tags", action="store_true", help="Keep header, footer, nav, aside tags (default: remove)")


    args = parser.parse_args()
    query = args.keyword
    num_results = args.num_results
    search_engine = args.search_engine
    search_sites = args.search_sites
    max_chars = args.max_chars
    keep_tags = args.keep_tags


    if search_engine == "duckduckgo":
        results = search_duckduckgo(query, num_results=num_results)
    else: # default to duckduckgo
        results = search_google(query, num_results=num_results, search_sites=search_sites) # use search_sites



    print(f"上位{num_results}件の検索結果 ({search_engine}):")
    for i, res in enumerate(results, start=1):
        # 結果の URL は通常 "href" キーに格納される
        url = res.get("href", "")
        title = res.get("title", "No Title") # title is only available for duckduckgo
        print(f"{i}. {title}: {url}")

    print("\\n各 URL から情報を抽出します...\\n")
    for i, res in enumerate(results, start=1):
        url = res.get("href", "")
        if not url:
            continue
        print(f"URL {i}: {url} の情報を抽出中...")
        text = extract_text_from_url(url, keep_tags=keep_tags, max_chars=max_chars) # pass keep_tags and max_chars
        if text:
            print(f"    全文:\\n{text}\\n")
        else:
            print("    情報の抽出に失敗しました。\\n")
        print("-" * 80)

if __name__ == "__main__":
    main()
