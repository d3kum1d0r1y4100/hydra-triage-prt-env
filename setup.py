from setuptools import setup
setup(
    name='triage-test-env',
    version='1.0.0',
    python_requires='>=3.12',
    py_modules=['app', 'deploy'],
    entry_points={
        'console_scripts': ['triage-test-env=app:main'],
    },
)
