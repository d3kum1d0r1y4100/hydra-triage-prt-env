from setuptools import setup
setup(
    name='triage-test-env',
    version='1.0.0',
    py_modules=['app'],
    entry_points={
        'console_scripts': [
            'triage-test-env=app:main',
        ],
    },
)
