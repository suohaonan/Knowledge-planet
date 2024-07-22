#! /bin/bash

git_repo=$1
branch=$2

git clone -b ${branch} $git_repo stat

cd stat
# 查询Q1最后一次提交
first_commit=$(git log --after="2024-01-01 23:59:59" --before="2024-03-31 23:59:59" --topo-order --pretty=format:"%H" --date=short ${branch} | head -n 1)
# 查询Q2最后一次提交
last_commit=$(git log --after="2024-03-31 23:59:59" --before="2024-06-30 23:59:59" --topo-order --pretty=format:"%H" --date=short ${branch} | head -n 1)

# git diff --stat commit1 commit2 统计两次提交之间的文件变化
# 得到的数据如：434 files changed, 1922 insertions(+), 26989 deletions(-)
# 修改文件总数
changed_files=$(git diff --stat $first_commit $last_commit | awk '{print $1}' | tail -n 1)
# 新增行数
added_lines=$(git diff --stat $first_commit $last_commit | awk '{print $4}' | tail -n 1)
# 删除行数
deleted_lines=$(git diff --stat $first_commit $last_commit | awk '{print $6}' | tail -n 1)
# 变化总行数
total_lines=$(git diff --stat $first_commit $last_commit | awk '{print $4+$6}' | tail -n 1)

# 输出结果
echo "Q1最后一次提交：$first_commit"
echo "Q2最后一次提交：$last_commit"
echo "修改文件总数：$changed_files"
echo "新增行数：$added_lines"
echo "删除行数：$deleted_lines"
echo "变化总行数：$total_lines"

cd ../
rm -rf stat