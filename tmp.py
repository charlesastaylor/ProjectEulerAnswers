import pip
for package in pip.get_installed_distributions():
    print(package)