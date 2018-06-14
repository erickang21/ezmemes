import setuptools

description = "ezmemes - Sync/Async wrapper for Python to easily request memes."
long_description = open("README.md").read()
version="1.0.0"

packages = ['ezmemes']

setuptools.setup(
    name='ezmemes',
    version=version,
    description=description,
    long_description=long_description,
    url='https://github.com/bananaboy21/ezmemes',
    author='Eric Kang',
    author_email='kang.eric.hi@gmail.com',
    license='MIT',
    packages=packages,
    include_package_data=True,
    install_requires=['aiohttp>=2.0.0', 'requests>=2.0.0']
)
