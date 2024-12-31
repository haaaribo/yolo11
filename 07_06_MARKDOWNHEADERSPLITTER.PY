# 파일을 읽고 전체 내용을 출력
from langchain_text_splitters import MarkdownHeaderTextSplitter

with open("textresume.md", "r", encoding="utf-8") as file:
    content = file.read()

print(content)

headers_to_split_on = [  # 문서를 분할할 헤더 레벨과 해당 레벨의 이름을 정의합니다.
    (
        "#",
        "Header 1",
    ),  # 헤더 레벨 1은 '#'로 표시되며, 'Header 1'이라는 이름을 가집니다.
    (
        "##",
        "Header 2",
    ),  # 헤더 레벨 2는 '##'로 표시되며, 'Header 2'라는 이름을 가집니다.
    (
        "###",
        "Header 3",
    ),  # 헤더 레벨 3은 '###'로 표시되며, 'Header 3'이라는 이름을 가집니다.
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, strip_headers=False,)

md_header_splits = markdown_splitter.split_text(content)

for header in md_header_splits:
    print(f"{header.page_content}")
    print(f"{header.metadata}", end="\n=====================\n")