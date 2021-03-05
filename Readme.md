# 1. 运行环境

## 1.1 依赖

- click
- face_recognition
- opencv-python
- PIL

# 2. 图片批量脸部打码脚本

## 2.1 脚本信息

脚本为`main.py`, 通过以下指令查看使用信息：

```bash
python main.py -h
```

使用信息如下：

```bash
Usage: main.py [OPTIONS] PATH

  图片头像批量打码.

  path: 要打码的图片的路径

Options:
  -o, --out_dir PATH  结果保存路径, 默认为./run
  -h, --help          Show this message and exit.
```

## 2.2 脚本输出

打码后的照片保存在`-o`指定的路径下, 默认为`./run`.