from setuptools import setup

setup(
    name='triage-test-env',
    version='1.0.0',
    py_modules=['app'],
    python_requires='>=3.12',
    entry_points={
        'console_scripts': [
            'triage-test=app:main',
        ],
    },
)
