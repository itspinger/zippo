import os, config as cfg

# List of approved versions to download
# Downloaded from here: https://getbukkit.org/download/spigot
versions = [
    "1.8", "1.8.3", "1.8.4", "1.8.5", "1.8.6", "1.8.7", "1.8.8",
    "1.9", "1.9.2", "1.9.4",
    "1.10", "1.10.2",
    "1.11", "1.11.1", "1.11.2",
    "1.12", "1.12.1", "1.12.2",
    "1.13", "1.13.1", "1.13.2",
    "1.14", "1.14.1", "1.14.2", "1.14.3", "1.14.4",
    "1.15", "1.15.1",
    "1.16.1", "1.16.2", "1.16.3", "1.16.4", "1.16.5",
    "1.17", "1.17.1",
    "1.18", "1.18.1", "1.18.2",
    "1.19", "1.19.1", "1.19.2", "1.19.3",
    "latest", "all" # latest is the latest version, all will download all from this list
]

# This method validates the version to install
# Allowed versions are defined in the list above
def validateInstallVersion(version):
    # Check if the version is valid from the above list
    if not(version in versions):
        print("Error: Unknown server version -> " + version)
        print("See allowed versions here: " + str(versions))
        exit()

    # The installation is valid
    print("Found a valid installation for the `" + version + "` version")
    return version

# This method validates the output directory
# This directory must be defined, otherwise the program will exit
def validateOutputDirectory():
    # Return the updated data
    return cfg.installdir()
    
