import requests
import sys
from bs4 import BeautifulSoup

def format_text(soup):
    formatted_lines = []
    for element in soup.recursiveChildGenerator():
        if isinstance(element, str):
            text = element.strip()
            if text:
                formatted_lines.append(text)
        elif element.name == 'br':
            formatted_lines.append('')
        elif element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            formatted_lines.append('\n' + element.get_text().strip() + '\n')
        elif element.name == 'li':
            formatted_lines.append('  * ' + element.get_text().strip())
        elif element.name == 'p':
            formatted_lines.append(element.get_text().strip() + '\n')


    return '\n'.join(formatted_lines)

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

        text = format_text(soup) # Use format_text for formatting

        if max_chars is not None:
            text = text[:max_chars]

        return text
    except Exception as e:
        print(f"URL取得エラー: {url}\\nエラー: {e}")
        return ""


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python read_url.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTPエラーをチェック (4xx または 5xx エラーの場合に例外を発生)

        soup = BeautifulSoup(response.text, 'html.parser') # HTMLを解析
        formatted_content = format_text(soup)

        print(formatted_content) # 整形後のテキストを標準出力に表示

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        sys.exit(1)
