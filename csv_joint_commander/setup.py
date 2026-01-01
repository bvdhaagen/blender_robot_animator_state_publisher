

from setuptools import setup
import os
from glob import glob

package_name = 'csv_joint_commander'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bart',
    maintainer_email='bart@todo.todo',
    description='Publish joint positions from CSV',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'position_publisher = csv_joint_commander.position_publisher:main',
        ],
    },
)
