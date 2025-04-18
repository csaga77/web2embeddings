# web2embeddings

[YouTube视频](https://youtu.be/mH1aTzKLGQM)

[B站视频](https://www.bilibili.com/video/BV1Z2ZEYiE4s)

一个完整的流程，用于下载、处理和从文档创建向量嵌入。该项目允许您从网页内容创建可搜索的语义嵌入，并在2D/3D空间中可视化。

> **注意：** 已处理的Godot网站已包含在仓库中（`artifacts/curated/godotengine`），因为下载和处理需要较长时间。如果您想使用Godot文档，可以直接从文本分块步骤开始。

![可视化截图](assets/visualization_screenshot.png)

## 安装

1. 克隆此仓库：
   ```bash
   git clone https://github.com/zivshek/web2embedding.git
   cd web2embedding
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 快速开始

该仓库包含预处理的Godot文档，因此您可以快速尝试此流程：

### 使用现有数据快速开始

1. 从已处理的Godot文档生成文本块：
   ```bash
   python chunker.py --input artifacts/curated/godotengine --chunk-size 400 --chunk-overlap 20
   ```

2. 创建向量嵌入：
   ```bash
   python vectorizer.py --input artifacts/chunks/godotengine_chunks_SZ_400_O_20.jsonl
   ```
   它将在artifacts/collections.txt中记录集合名称，您可以在以后使用时复制此名称。

3. 可视化嵌入：
   ```bash
   python visualizer.py --collection godotengine_chunks_SZ_400_O_20_all-MiniLM-L6-v2
   ```

### 从头处理新内容的完整流程

要从头开始处理新的网页内容：

1. 在`websites_to_download.txt`中添加URL，然后下载内容：
   ```bash
   python downloader.py
   ```

2. 按照下面"工作流程"部分的步骤2-5操作。

## 概述

该项目提供了一个综合工作流程，用于：

1. 下载网页内容（如Godot文档）
2. 通过清理和转换为markdown来整理内容
3. 将文本分割成可管理的段落
4. 创建文本块的向量嵌入
5. 在2D/3D空间中可视化嵌入

## 前提条件

- Python 3.8+
- 所需的Python包（通过requirements.txt安装）
- 足够的磁盘空间用于下载内容和向量数据库

## 项目结构

```
website2embedding/
├── downloader.py       # 下载网页内容
├── page_curator.py     # 清理HTML并转换为markdown
├── chunker.py          # 将文本分割成块
├── vectorizer.py       # 创建向量嵌入
├── visualizer.py       # 在2D/3D中可视化嵌入
├── websites_to_download.txt  # 要下载的网站列表
├── artifacts/         # 所有生成文件的目录
    ├── downloaded_sites/  # 原始下载的HTML
    ├── curated/         # 清理后的markdown文件
    ├── chunks/          # JSONL格式的文本块
    ├── chroma_db/       # 向量数据库
    └── visualizations/  # 2D/3D可视化
```

## 工作流程

### 1. 下载网页内容

从`websites_to_download.txt`中列出的网站下载HTML内容：

```bash
python downloader.py --delay 1.0
```

选项：
- `--delay` / `-d`: 请求之间的延迟（秒）（默认：1.0）

### 2. 整理内容

清理HTML并转换为markdown格式：

```bash
python curator.py --input artifacts/downloaded_sites/site_domain
```

选项：
- `--input` / `-i`: 包含下载HTML的输入目录

### 3. 创建文本块

将markdown文件分割成可管理的块：

```bash
python chunker.py --input artifacts/curated/site_domain --chunk-size 400 --chunk-overlap 20
```

选项：
- `--input` / `-i`: 包含markdown文件的输入目录
- `--chunk-size` / `-s`: 块的最大字符大小（默认：400）
- `--chunk-overlap` / `-v`: 块之间的重叠字符数（默认：20）

### 4. 创建向量嵌入

生成嵌入并存储在ChromaDB中：

```bash
python vectorizer.py --input artifacts/chunks/chunks_SZ_400_O_20.jsonl --db artifacts/vector_stores/chroma_db
```

选项：
- `--input` / `-i`: 包含文本块的JSONL文件
- `--db` / `-d`: ChromaDB向量数据库目录（默认：artifacts/vector_stores/chroma_db）
- `--model` / `-m`: sentence-transformer模型名称（默认：sentence-transformers/all-MiniLM-L6-v2）
- `--batch-size` / `-b`: 嵌入生成的批处理大小（默认：32）

> **注意:** **集合**名会被写入 artifacts/vector_stores/collections.txt 以备日后使用。

### 5. 可视化嵌入

创建嵌入的交互式2D/3D可视化：

```bash
python visualizer.py --collection chunks_SZ_400_O_20_sentence-transformers_all-MiniLM-L6-v2
```

选项：
- `--db` / `-d`: ChromaDB数据库目录（默认：artifacts/vector_stores/chroma_db）
- `--collection` / `-c`: ChromaDB中的集合名称
- `--max-points` / `-m`: 要可视化的最大点数（默认：2000）
- `--seed` / `-s`: 用于可重现性的随机种子（默认：42）
- `--clusters` / `-k`: 用于着色的集群数量（默认：10）

## 示例用例

该项目设计用于处理Godot文档，但可以适用于任何网页内容。潜在应用包括：
- 技术文档探索
- 语义搜索引擎
- 内容组织和发现
- 文档相似性分析

## 注意事项

- `.gitignore`设置为排除artifacts目录，以避免提交大型文件。
- 对于大型网站，考虑在`downloader.py`中调整延迟以避免速率限制。
- 大型集合的向量嵌入需要大量内存。
