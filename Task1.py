from bs4 import BeautifulSoup

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup, soup.prettify()

def find_text_by_tag(soup, tag_name):
    result = []
    for tag in soup.find_all(tag_name):
        text = tag.get_text(strip=True)
        if text:
            result.append(text)
    return result

html_content = """
<html>
  <body>
    <h1>Title</h1>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
    <div>
      <p>Inside Div</p>
    </div>
  </body>
</html>
"""

parsed_html, prettified_html = parse_html(html_content)
tag_name_to_search = 'p'
found_texts = find_text_by_tag(parsed_html, tag_name_to_search)

if found_texts:
    print(f"Знайдений текст за тегом '{tag_name_to_search}': {found_texts}")
else:
    print(f"Текст за тегом '{tag_name_to_search}' не знайдений.")

print("\nHTML дерево:")
print(prettified_html)
