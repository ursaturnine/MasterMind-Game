from setuptools import setup, find_packages



setup(
    name="Master-Mind-Game",
    version="1.1.1",
    description="MasterMindGame using Click for an interactive CLI GUI",
    author="Tyrah Gullette",
    author_email="tyrah96@gmail.com",
    url="https://github.com/ursaturnine/MasterMind-Game",
    packages=find_packages(exclude=["tests*", "testing*"]),
    install_package_data=True,
    install_requires=["click","copy", "pytest", "random"],
    entry_points={
        'console_scripts': [
            'game = src.optionsMenu:menu'
        ]
    }
)
