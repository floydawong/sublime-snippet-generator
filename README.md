# Auto Complete Keyword

## 环境
- Python 2.6 2.7 or 3.3

## 使用说明
修改`GenerateSnippet.py`中的
```Python
KEYWORD_FILE_PATH = r"./matlab_function_list.txt" # 关键字列表文件路径
OUTPUT_DIR_PATH = r"./snippet" # snippet输出目录
SUFFIX = "matlab" # 在哪个语言里面补全
```

首先, 需要一个单词列表文件
一个单词一行
将文件放到当前目录下
执行`GenerateSnippet.py`

得到一个snippet目录
将该目录放到Sublime的安装路径下的`./Package/User/`里面