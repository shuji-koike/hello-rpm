# docker rmi centos:6-devel
docker build -t centos:6-devel .
docker run -it --rm -v ${PWD}/rpmbuild:/root/rpmbuild --name centos centos:6-devel
docker diff centos | grep -v /usr/local/src | less

mkdir -p /root/rpmbuild/{SPECS,SOURCES}
curl http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz -o /root/rpmbuild/SOURCES/yasm-1.3.0.tar.gz

rpmbuild -ba /root/rpmbuild/SPECS/yasm.spec
rm -rf /root/rpmbuild/BUILD/*

rpm -qlp /root/rpmbuild/RPMS/x86_64/yasm-1.3.0-1.x86_64.rpm

rpm -ivh /root/rpmbuild/RPMS/x86_64/yasm-1.3.0-1.x86_64.rpm
rpm -e yasm-1.3.0-1.x86_64.rpm
