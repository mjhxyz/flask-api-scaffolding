from setuptools import setup, find_packages

setup(
    name='flask-api-scaffolding',
    version='0.1',
    description='sample flask api scaffolding',
    author='Mao',
    author_email='mjhxyz@foxmail.com',
    packages=find_packages(),
    install_requires=[
        'Flask==2.2.5',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
