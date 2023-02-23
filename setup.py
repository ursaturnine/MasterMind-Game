from setuptools import setup, find_packages



setup(
    name="Master-Mind-Game",
    version="1.2.2",
    description="MasterMindGame using Click for an interactive CLI GUI",
    author="Tyrah Gullette",
    author_email="tyrah96@gmail.com",
    url="https://github.com/ursaturnine/MasterMind-Game",
    packages=find_packages(),
    install_package_data=True,
    entry_points={
        'console_scripts': [
            'game = src.optionsMenu:menu'
        ]
    }
)
