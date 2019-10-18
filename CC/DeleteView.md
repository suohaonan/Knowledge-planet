#强制undo视图checkout、删除某视图
1.cleartool lsview -long 视图名         #用该命令得到视图的UUID 号。
2.cleartool rmview -force -vob Z:\administrator_main\RC3000-6-Z（或者 -avobs） -uuid uuid  #对每一个VOB 都进行这种操作，删除VOB 和该视图的关联信息。

cleartool rmview -force  -avobs  -uuid uuid  #对所有VOB 都进行这种操作，删除VOB 和该视图的关联信息。

3.checkout的文件自动取消，修改内容消失。
4.cleartool unregister -view -uuid uuid          #删除视图的view-object 注册信息；
5.cleartool rmtag -view -all 视图名           #view tag 的完全删除；