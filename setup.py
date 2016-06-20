from distutils.core import setup

setup(
    name='jailbreakstatus',
    version='0.0.1',
    author='Andrew Udvare',
    author_email='audvare+jailbreakstatus@gmail.com',
    url='https://github.com/Tatsh/jailbreakstatus',
    license='LICENSE.txt',
    description='Simple check using Jailbreak subreddit for a jailbreak for iOS 9.2+.',
    long_description=open('README.md').read(),
    classifiers=[
        'Environment :: Console',
        'Topic :: Utilities',
    ],
    install_requires=[
        'praw>=3.5.0',
    ],
    py_modules=['jailbreakstatus'],
    entry_points={
        'console_scripts': [
            'jailbreakstatus = jailbreakstatus:jailbreakstatus'
        ]
    }
)
