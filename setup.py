from setuptools import setup, find_packages

setup(
    name='samurai',  # 项目名称
    version='0.4.0',  # 项目版本
    author='NoW0NDER',  # 作者名字
    author_email='nowonder.dw@gmail.com',  # 作者邮箱
    packages=find_packages(),  # 自动发现所有包和子包
    description='侍，待命中',  # 简短描述
    long_description=open('README.md').read(),  # 长描述，通常是读取README.md文件
    long_description_content_type='text/markdown',  # 长描述的格式
    install_requires=[],  # 项目依赖的其他包
)
