from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='flaskProject',
    version='1.0.0',
    packages=find_packages(),
    author='isaacvt01',
    author_email='isaacvt2001@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/isaacvt01/Ollivanders-Flask.git',
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'attrs==22.2.0',
        'click==8.1.3',
        'colorama==0.4.6',
        'coverage==7.2.2',
        'dnspython==2.3.0',
        'flask==2.2.3',
        'flask-testing==0.8.1',
        'iniconfig==2.0.0',
        'itsdangerous==2.1.2',
        'jinja2==3.1.2',
        'markupsafe==2.1.2',
        'packaging==23.0',
        'pluggy==1.0.0',
        'pymongo==4.3.3',
        'pytest==7.2.2',
        'python-dotenv==1.0.0',
        'werkzeug==2.2.3',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
