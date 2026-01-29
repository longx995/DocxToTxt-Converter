```markdown
![GitHub release](https://img.shields.io/github/v/release/longx995/DocxToTxt-Converter)
![GitHub downloads](https://img.shields.io/github/downloads/longx995/DocxToTxt-Converter/total)
```
# DocxToTxt 批量转换工具

一个简单易用的批量文档转换工具，可以将doc/docx格式的文档批量转换为纯文本txt格式。

## 功能特点

✅ **批量转换** - 一次性转换整个文件夹中的所有doc/docx文件  
✅ **保持段落** - 保留原文档的段落结构  
✅ **中文支持** - 完美支持中文编码（GBK/GB18030/GB2312/UTF-8/Big5）  
✅ **独立运行** - exe版本无需安装Python环境  
✅ **简单易用** - 支持命令行参数和交互式输入  

## 使用方法

### 方法一：双击运行（推荐）

1. 双击 `DocxToTxt转换工具.exe`
2. 根据提示输入包含doc/docx文件的文件夹路径
3. 按回车开始转换
4. 转换完成后，txt文件会保存在原文件夹中

### 方法二：命令行运行

打开命令提示符（CMD）或PowerShell，使用以下命令：

```bash
# 使用-d参数指定目录
DocxToTxt转换工具.exe -d "D:\jiangji"

# 或使用完整参数名
DocxToTxt转换工具.exe --directory "C:\Documents"

# 查看帮助信息
DocxToTxt转换工具.exe --help
```

## 系统要求

- **操作系统**: Windows 7 / 8 / 10 / 11
- **硬盘空间**: 至少50MB可用空间
- **内存**: 建议512MB以上

## 文件说明

```
Convert_DocxtoTxt/
├── dist/
│   └── DocxToTxt转换工具.exe    # 可执行文件（主程序）
├── extract_text.py               # Python源代码
├── README.md                     # 使用说明（本文件）
└── requirements.txt              # Python依赖（无额外依赖）
```

## 使用示例

**示例1：转换单个文件夹**
```bash
DocxToTxt转换工具.exe -d "D:\我的文档"
```

**示例2：转换包含子文件夹的目录**
```bash
# 注意：本工具只转换指定目录下的文件，不包括子目录
DocxToTxt转换工具.exe -d "C:\Users\用户名\Documents"
```

## 转换结果

- 每个doc/docx文件会生成一个同名的.txt文件
- txt文件保存在原文件所在目录
- 原始doc/docx文件不会被修改或删除

## 注意事项

⚠️ **重要提示**：
- 仅转换指定目录下的文件，**不包括子目录**
- 转换过程中会丢失文档的格式信息（字体、颜色、表格等）
- 仅保留纯文本内容和段落结构
- 建议在转换前备份重要文件

## 支持的文件格式

- ✅ `.docx` - Microsoft Word 2007及以后版本
- ✅ `.doc` - Microsoft Word 97-2003版本（以GBK编码保存的文件）

## 兼容性说明

本工具使用字节级文本提取技术，适用于：
- 旧版Word格式（.doc）的文档，特别是GBK编码的中文文档
- 某些无法使用标准Office工具打开的特殊格式文档

**不适用于**：
- 包含复杂格式、图片、表格的文档（仅提取文本部分）
- 需要保留完整格式的文档转换

## 常见问题

**Q: 为什么有些文档转换后乱码？**  
A: 本工具优先使用GBK编码，适合大多数中文文档。如遇乱码，可能是文档使用了其他编码。

**Q: 可以转换子文件夹中的文件吗？**  
A: 当前版本只转换指定目录下的文件，不包括子目录。

**Q: 转换速度有多快？**  
A: 每秒可处理约10-50个文档，具体速度取决于文档大小和电脑配置。

**Q: 是否支持批量重命名？**  
A: 本工具不支持重命名，只进行格式转换。

## 技术支持

如遇到问题或有改进建议，请通过以下方式联系：

- 📧 issues: 在项目仓库提交issue
- 📝 源代码: `extract_text.py`

## 版本信息

- **当前版本**: v1.0
- **发布日期**: 2026-01-29
- **Python版本**: 3.11

```markdown
## 下载
📥 **最新版本**: [v1.0](https://github.com/longx995/DocxToTxt-Converter/releases/tag/v1.0)
直接下载exe文件：[DocxToTxt转换工具.exe](https://github.com/longx995/DocxToTxt-Converter/releases/download/v1.0/DocxToTxt转换工具.exe)
```

## 开源许可

本项目采用MIT许可证开源。

---

**感谢使用DocxToTxt转换工具！**
