from setuptools import setup, find_packages

setup(
    name='ada_friend',
    version='0.0.1',
    url='https://github.com/ratopythonista/ada-friend.git',
    author='Catlangos',
    author_email='rodrigoara27@gmail.com',
    description='Projeto do Hackaton CPBSB3 Tempo de Mudanças',
    packages=find_packages(),
    install_requires=[
            'pymongo==3.5.1',
            'flask-restful==0.3.7',
            'flask==1.0.3',
            'telepot==12.7',
            'flasgger==0.9.2',
            'loguru==0.2.5',
            'rasa==1.1.3',
    ],
)
