# 3.8.1: Create a binary number.
import pkg_resources

thing = pkg_resources.resource_filename('pkg_resources', '__init__.py')
print(thing)
