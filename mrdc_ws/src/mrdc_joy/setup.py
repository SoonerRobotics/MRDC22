from setuptools import find_packages, setup

package_name = 'mrdc_joy'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/all_launch.xml'])
    ],
    install_requires=['setuptools'],
    maintainer='Dylan Zemlin',
    maintainer_email='dylansmrw@gmail.com',
    description='TODO: Package description',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'driver = src.driver:main'
        ],
    },
)
