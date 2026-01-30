## 🎉 v1.1 更新说明

### ✨ 新功能
- **智能 docx 解析**：自动识别标准 docx 格式（ZIP 包），直接解析 XML 提取文本
- **自动回退机制**：解析失败时自动使用二进制提取，兼容旧版特殊格式文档

### 🐛 Bug 修复
- **彻底解决 docx 转换乱码问题**：以往版本中 docx 文件转换后出现 "PK..." 乱码的问题已完全修复

### 🔄 优化改进
- 保留原有的二进制提取功能作为回退方案
- 提升了标准 docx 文件的转换准确性和速度

## 📦 下载说明
下载 `DocxToTxt转换工具v1.1.exe` 后即可直接运行，无需安装 Python 环境。

## 💡 使用方法
详见 [README.md](https://github.com/longx995/DocxToTxt-Converter/blob/main/README.md)

---

## 技术细节
- 新增 `zipfile` 和 `xml.etree.ElementTree` 解析标准 docx 文件
- 智能识别文件扩展名，优先使用结构化解析
- 保持向后兼容，自动回退到二进制提取模式
