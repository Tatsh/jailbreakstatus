from distutils.core import setup

setup(
    name='jailbreakstatus',
    version='0.0.2',
    author='Andrew Udvare',
    author_email='audvare+jailbreakstatus@gmail.com',
    url='https://github.com/Tatsh/jailbreakstatus',
    license='LICENSE.txt',
    description='Simple check for the latest jailbreak.',
    long_description=open('README.md').read(),
    classifiers=[
        'Environment :: Console',
        'Topic :: Utilities',
    ],
    install_requires=[
        'beautifulsoup4==4.5.1',
        'html5lib==0.999999999',
        'requests==2.11.1',
    ],
    py_modules=['jailbreakstatus'],
    entry_points={
        'console_scripts': [
            'jailbreakstatus = jailbreakstatus:jailbreakstatus'
        ]
    }
)
