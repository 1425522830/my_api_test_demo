# common/yaml_util.py
import yaml
import os

# 解析为python字典
def read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:   # 保证close()函数被调用，防止文件一直占用句柄
        return yaml.safe_load(f)

def get_login_data():
    # 便于代码移植，但依赖项目目录结构的固定层级
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))      # 得到根目录
    yaml_path = os.path.join(base_dir, 'data', 'login_data.yaml')               # 目录拼接
    data = read_yaml(yaml_path)                 # 返回解析成python格式的文本内容
    return data['login_cases']