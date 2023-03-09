import os
from glob import glob

from setuptools import setup

package_name = 'turtle_tf2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Cristobal Arroyo',
    maintainer_email='cristobal.arroyo@ekumenlabs.com',
    description='Turtle TF2 Demo. Taken from: https://docs.ros.org/en/foxy/Tutorials/Intermediate/Tf2/Tf2-Main.html',
    license='Apache Licence 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_tf2_broadcaster = turtle_tf2.turtle_tf2_broadcaster:main',
            'turtle_tf2_listener = turtle_tf2.turtle_tf2_listener:main',
        ],
    },
)
