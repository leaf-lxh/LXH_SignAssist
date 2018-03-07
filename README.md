 # LXH_SignAssist is a python script running on CentOS 7. 

 ### Usage:
 - It can sign in baidu tieba for you automaticly.
 - When one sign in failure happened, it will send an e-mail which include logs to you.
 - Multiple accounts are supported.  It uses mariadb to save user info.


 ### Install:
 - install git `# yum -y install git`
 - download source code `# git clone https://github.com/leaf-lxh/LXH_SignAssist.git` 
 - use Python 3.x to run main.py

 ### TODO: 
 - (done)1.Use mariadb to store data.
 - (done)2.Sign in user data sourse mariadb supports
 - 3.Send e-mail to user when sign in failure happens.
 - (done)4.Initialize mariadb supports
 - (done)5.daemon process

 ### Files:
>There are some files will be created will this script is running
 - Log: /var/log/lxh/output.log
 - Config: /etc/lxh/config.json
