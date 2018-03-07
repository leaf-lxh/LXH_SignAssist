 # LXH_SignAssist is a python script running on CentOS 7. 

###Usage:
 - It can sign in baidu tieba for you automaticly.
 - When one sign in failure happened, it will send an e-mail which include logs to you.
 - Multiple accounts are supported.  It uses mariadb to save user info.


###Install:
 - 1. install git : # yum -y install git
 - 2.download source code :# git clone https://github.com/leaf-lxh/LXH_SignAssist.git	
 - 3. install python3 : 
###About specific mean of some arguments:
 - kw: the name of the bar
 - fid: the bar id in number form
 - BDUSS: an user identification which can be found in cookie
 - tbs: an specific identification which is created when you visited one specific bar web page


###TODO: 
 - (done)1.Use mariadb to store data.
 - (done)2.Sign in user data sourse mariadb supports
 - 3.Send e-mail to user when sign in failure happens.
 - (done)4.Initialize mariadb supports
 - (done)5.daemon process