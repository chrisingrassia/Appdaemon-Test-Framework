from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='appdaemontestframework',
    version='2.0.0',
    description='Clean, human-readable tests for Appdaemon',
    long_description=readme(),
    keywords='appdaemon homeassistant test tdd clean-code home-automation',
    classifiers=[
        'Environment :: Console',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Testing'
    ],
    url='https://floriankempenich.github.io/Appdaemon-Test-Framework',
    author='Florian Kempenich',
    author_email='Flori@nKempenich.com',
    packages=['appdaemontestframework'],
    license='MIT',
    install_requires=[
        'appdaemon',
        'mock',
        'pyyaml>=4.2b1',
        'requests>=2.20.0'
    ],
    include_package_data=True
)
