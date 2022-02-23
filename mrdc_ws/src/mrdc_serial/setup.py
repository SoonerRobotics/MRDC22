from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'mrdc_serial'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
         glob(os.path.join('launch', '*.xml')))
    ],
    install_requires=['setuptools'],
    maintainer='Dylan Zemlin',
    maintainer_email='dylan.zemlin@gmail.com',
    description='The MRDC Serial package that controls communication to the arduino',
    license='MIT License',
    entry_points={
        'console_scripts': [
            'remote = mrdc_serial.remote:main',
            'serial = mrdc_serial.serial:main'
        ],
    },
)
