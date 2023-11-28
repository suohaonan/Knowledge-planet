# -*- coding:UTF-8 -*-
import jenkins
import datetime

class Jenkins:
    def __init__(self):
        """
        初始化Jenkins类，使用Jenkins服务器的URL、用户名和密码。
        """
        url = ''
        username = ''
        password = ''
        self.server = jenkins.Jenkins(url, username=username, password=password)

    def get_all_jobs(self):
        """
        检索Jenkins服务器中所有作业的列表。

        返回：
        - jobs_list (list): 作业名称的列表。
        """
        jobs = self.server.get_jobs()
        jobs_list = []
        for job in jobs:
            if job['_class'] == "com.cloudbees.hudson.plugins.folder.Folder":
                child_jobs = job['jobs']
                for child_job in child_jobs:
                    if child_job['_class'] == "com.cloudbees.hudson.plugins.folder.Folder":
                        grand_jobs = child_job['jobs']
                        for grand_job in grand_jobs:
                            job_name = job['name'] + '/' + child_job['name'] + '/' + grand_job['name']
                            jobs_list.append(job_name)
                    else:
                        job_name = job['name'] + '/' + child_job['name']
                        jobs_list.append(job_name)
            else:
                jobs_list.append(job['name'])
        return jobs_list
    
    def get_build_info(self, job_name, build_number):
        """
        检索特定作业和构建编号的构建信息。

        参数：
        - job_name (str): 作业名称。
        - build_number (int): 构建编号。

        返回：
        - build_info (dict): 构建信息。
        """
        build_info = self.server.get_build_info(job_name, build_number)
        return build_info
    
    def get_job_info(self, job_name):
        """
        检索特定作业的信息。

        参数：
        - job_name (str): 作业名称。

        返回：
        - job_info (dict): 作业信息。
        """
        job_info = self.server.get_job_info(job_name)
        return job_info


js = Jenkins()
jobs_list = js.get_all_jobs()
total_build_time = 0
days_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).timestamp() * 1000
for job in jobs_list:
    job_name = job
    job_info = js.get_job_info(job)
    builds = job_info['builds']
    job_build_time = 0
    job_build_count = 0
    job_success_count = 0
    job_failure_count = 0
    job_aborted_count = 0
    
    for build in builds:
        build_number = build['number']
        build_info = js.get_build_info(job_name, build_number)
        build_duration = build_info['duration']
        build_result = build_info['result']
        build_timestamp = build_info['timestamp']  


        if build_timestamp > days_ago:

            if build_result == 'SUCCESS':
                job_success_count += 1
            elif build_result == 'FAILURE':
                job_failure_count += 1
            elif build_result == 'ABORTED':
                job_aborted_count += 1

            job_build_time += build_duration
            job_build_count += 1

    print(f'Job: {job_name}, Build Time: {job_build_time}, Build Count: {job_build_count}, Success Count: {job_success_count}, Failure Count: {job_failure_count}, Aborted Count: {job_aborted_count}')


    total_build_time += job_build_time
    total_build_time_minutes = total_build_time / 1000 / 60 


print(f'Total Build Time: {total_build_time}')
