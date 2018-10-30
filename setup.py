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
        'requests>=2.20.0',
    ],
    py_modules=['jailbreakstatus'],
    entry_points={
        'console_scripts': [
            'jailbreakstatus = jailbreakstatus:jailbreakstatus'
        ]
    }
)
