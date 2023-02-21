from setuptools import setup, find_packages



setup(
    name="Master-Mind-Game",
    version="1.0",
    packages=find_packages(),
    install_package_data=True,
    install_requires=["click"],
    entry_points={
        'console_scripts': [
            'mastermind = src.optionsMenu:menu'
        ]
    }
)
