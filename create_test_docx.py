
import zipfile
import os

def create_minimal_docx(filename, text_content):
    # Minimal document.xml content
    document_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    <w:p>
      <w:r>
        <w:t>{text_content}</w:t>
      </w:r>
    </w:p>
  </w:body>
</w:document>"""

    with zipfile.ZipFile(filename, 'w') as docx:
        docx.writestr('word/document.xml', document_xml)
        # Add a minimal content types file just in case, though my extractor only cares about document.xml
        docx.writestr('[Content_Types].xml', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"></Types>')

if __name__ == "__main__":
    create_minimal_docx("test_doc.docx", "你好，这是一个测试文档。")
    print("test_doc.docx created.")
