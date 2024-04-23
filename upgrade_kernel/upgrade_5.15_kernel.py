# wget -c https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.15/amd64/linux-headers-5.15.0-051500_5.15.0-051500.202110312130_all.deb
# wget -c https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.15/amd64/linux-headers-5.15.0-051500-generic_5.15.0-051500.202110312130_amd64.deb
# wget -c https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.15/amd64/linux-image-unsigned-5.15.0-051500-generic_5.15.0-051500.202110312130_amd64.deb
# wget -c https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.15/amd64/linux-modules-5.15.0-051500-generic_5.15.0-051500.202110312130_amd64.deb
# dpkg -i *.deb

# check exist
import os

pkgs=[
    'linux-headers-5.15.0-051500_5.15.0-051500.202110312130_all.deb',
    'linux-headers-5.15.0-051500-generic_5.15.0-051500.202110312130_amd64.deb',
    'linux-image-unsigned-5.15.0-051500-generic_5.15.0-051500.202110312130_amd64.deb',
    'linux-modules-5.15.0-051500-generic_5.15.0-051500.202110312130_amd64.deb'
]

for pkg in pkgs:
    if not os.path.exists(pkg):
        os.system(f'wget -c https://kernel.ubuntu.com/~kernel-ppa/mainline/v5.15/amd64/{pkg}')
    if not os.path.exists(pkg):
        print(f'Error: {pkg} download failed')
        exit(1)

for pkg in pkgs:
    os.system(f'dpkg -i {pkg}')