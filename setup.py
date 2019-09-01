from setuptools import setup

requirements = [
    'requests==2.22.0',
]

setup(
    name='yap-api',
    version='0.2',
    description='A Python API Wrapper for the YAP Server',
    author="The Open NLP Lab at the Open University of Israel",
    author_email="contact@chelem.co.il",
    url='https://github.com/research-software-company/yap-python-api',
    packages=['yap_api'],
    install_requires=requirements,
    keywords='yap',
    classifiers=[
        'Programming Language :: Python :: 3'
    ]
)
