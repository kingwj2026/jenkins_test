#!/usr/bin/env groovy
import groovy.transform.Field

@Field def job_name=""

node()
{
    // 获取当前job名称。也可以按需自定义
    job_name="${env.JOB_NAME}".replace('%2F', '/').split('/')
    job_name=job_name[0]

    // 自定义workspace
    workspace="/data/jenkins/workspace/CI"

    ws("$workspace")
    {
        dir("pipeline")
        {   
            // clone Jenkinsfile项目
            git url: 'git@XXYY.com:pipeline.git'

            // 根据job name、构建分支，自动加载对应的Jenkinsfile
            def check_groovy_file="${job_name}/${env.BRANCH_NAME}/Jenkinsfile"
            load "${check_groovy_file}"
        }
    }
}
