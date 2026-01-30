# 如何将项目提交到GitHub

本文档指导你将DocxToTxt项目上传到GitHub。

## 前提条件

1. ✅ 已完成：Git仓库已初始化
2. ✅ 已完成：首次提交已创建
3. ⚠️ 需要：GitHub账号（如果没有，请访问 https://github.com 注册）

## 提交步骤

### 方法一：使用GitHub Desktop（推荐新手）

1. **下载并安装GitHub Desktop**
   - 访问：https://desktop.github.com/
   - 下载并安装

2. **添加现有仓库**
   - 打开GitHub Desktop
   - 点击 `File` → `Add local repository`
   - 选择文件夹：`d:\anti\Convert_DocxtoTxt`

3. **发布到GitHub**
   - 点击 `Publish repository`
   - 填写仓库信息：
     - Name: `DocxToTxt-Converter`（或你喜欢的名字）
     - Description: `批量将doc/docx文件转换为txt格式的工具`
     - ☐ Keep this code private（取消勾选=公开仓库）
   - 点击 `Publish repository`

### 方法二：使用命令行

#### 步骤1：在GitHub创建新仓库

1. 访问 https://github.com
2. 登录你的账号
3. 点击右上角的 `+` → `New repository`
4. 填写信息：
   - Repository name: `DocxToTxt-Converter`
   - Description: `批量将doc/docx文件转换为txt格式的工具`
   - Public/Private: 选择Public（公开）
   - ⚠️ 不要勾选 "Initialize this repository with a README"
5. 点击 `Create repository`

#### 步骤2：连接本地仓库到GitHub

复制GitHub上显示的命令，或使用以下命令（替换你的用户名）：

```bash
# 添加远程仓库（替换YOUR_USERNAME为你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/DocxToTxt-Converter.git

# 推送代码到GitHub
git branch -M main
git push -u origin main
```

**完整示例**：
```powershell
cd d:\anti\Convert_DocxtoTxt
git remote add origin https://github.com/YOUR_USERNAME/DocxToTxt-Converter.git
git branch -M main
git push -u origin main
```

#### 步骤3：输入GitHub凭据

首次推送时会要求输入：
- GitHub用户名
- 个人访问令牌（Personal Access Token）

**如何获取个人访问令牌**：
1. 访问：https://github.com/settings/tokens
2. 点击 `Generate new token` → `Generate new token (classic)`
3. 设置：
   - Note: `DocxToTxt`
   - Expiration: `90 days`（或自选）
   - 勾选：`repo`（完整控制权限）
4. 点击 `Generate token`
5. **重要**：复制生成的令牌（只显示一次）
6. 在命令行提示输入密码时，粘贴这个令牌

## 当前Git状态

```
✅ Git仓库已初始化
✅ 已创建首次提交（commit: 36ac8ef）
✅ 包含5个文件：
   - extract_text.py（主程序）
   - README.md（使用文档）
   - LICENSE（MIT许可证）
   - .gitignore（Git忽略规则）
   - requirements.txt（依赖说明）
```

## 后续更新

将来如果修改了代码，可以使用以下命令更新GitHub：

```bash
# 添加修改的文件
git add .

# 提交更改
git commit -m "描述你的修改"

# 推送到GitHub
git push
```

## 建议的仓库设置

提交到GitHub后，建议：

1. **添加Topics（主题标签）**
   - 在仓库页面点击 `Add topics`
   - 添加：`python`, `converter`, `docx`, `txt`, `file-conversion`

2. **添加Release（发布版本）**
   - 点击 `Releases` → `Create a new release`
   - Tag: `v1.0`
   - Release title: `v1.0 - 首次发布`
   - 上传 `dist\DocxToTxt转换工具.exe` 作为发布附件

3. **更新README.md**
   - 在GitHub页面会自动显示README.md
   - 可以添加徽章（badges）让项目更专业

## 常见问题

**Q: 为什么dist文件夹没有被提交？**  
A: dist文件夹中的exe文件很大（8MB），不适合放在Git仓库中。建议通过GitHub Releases发布。

**Q: 如何更改仓库为私有？**  
A: 仓库页面 → Settings → Danger Zone → Change visibility

**Q: 忘记了个人访问令牌怎么办？**  
A: 重新生成一个新的令牌即可。

## 需要帮助？

如果遇到问题：
1. 检查Git是否正确安装：`git --version`
2. 检查网络连接
3. 查看GitHub官方文档：https://docs.github.com

---

**准备好了吗？按照上面的步骤开始提交吧！** 🚀
