#Sehll脚本输出调试信息
set -o xtrace
set -o verbose

#Shell 脚本语法检查
bash -n script.sh	
bash -v script.sh	#追踪脚本里每个命令的执行
bash -x script.sh	#追踪脚本里每个命令的执行并附加扩充信息

#fail fast
set -o errexit	#执行出错退出
set -o nounset	#遇到不存在的变量退出
