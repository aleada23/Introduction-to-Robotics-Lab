from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ItR_lab_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # The line below handles your launch files
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='email@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 
            "test_node = ItR_lab_pkg.my_first_node:main",
            "draw_circle = ItR_lab_pkg.draw_circle:main",
            "pose_subscriber = ItR_lab_pkg.pose_subscriber:main",
            "turtle_controller = ItR_lab_pkg.turtle_controller:main",
            "turtle_controller_2 = ItR_lab_pkg.turtle_controller_2:main"
        ],
    },
)
