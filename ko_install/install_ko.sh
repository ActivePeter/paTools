wget https://github.com/ko-build/ko/releases/download/v0.13.0/ko_0.13.0_Linux_x86_64.tar.gz
mv ko_0.13.0_Linux_x86_64.tar.gz ko.tar.gz
tar -zxvf ko.tar.gz ko
chmod +x ./ko
mv ko /usr/local/bin/ko
rm -rf ko.tar.gz