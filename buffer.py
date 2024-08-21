1. Пререквизиты:
а) установленный и керберизированный кластер hadoop
б) установленный кластер opensearch
в) 3 сервера для компонентов графовой платформы: fastgraph, bigraph, gss-rest
2. Установка hadoop кластера
Кластер устанавливается на основе ambari, для установки необходимо:
a) сделать локальный репозиторий с пакетами сборки hadoop и ambari и прописать его в настройках
всех хостов кластера:
понадобятся пакеты nginx, createrepo, yum-utils
Создаем папку
mkdir -p /usr/share/nginx/html/repos/7/{os,updates}/x86_64
Создаем репозитории:
createrepo -v /usr/share/nginx/html/repos/7/os/x86_64
createrepo -v /usr/share/nginx/html/repos/7/updates/x86_64
А также разрешаем группы:
createrepo /usr/share/nginx/html/repos/7/os/x86_64 -g /usr/share/nginx/html/repos/7/os/x86_64/repodata/
repomd.xml
createrepo /usr/share/nginx/html/repos/7/updates/x86_64 -g /usr/share/nginx/html/repos/updates/os/
x86_64/repodata/repomd.xml
Настраиваем nginx:
vi /etc/nginx/conf.d/default.confvi /etc/nginx/conf.d/default.conf
...
location / {
root /usr/share/nginx/html;
index index.html index.htm;
autoindex on;
}
...
Перезапускаем nginx: sudo systemctl restart nginx
Создаем файл с настройкой репозитория:
vi /etc/yum.repos.d/local.repo
[local]
name=Local Yum Repo
baseurl=http://192.168.0.10/repos/$releasever/os/$basearch/
enabled=1
gpgcheck=0
terepo yum-utils creat
