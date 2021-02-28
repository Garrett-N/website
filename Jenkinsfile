#!/usr/bin/env groovy
pipeline {
    agent {
        node {
            label 'master'
        }
    }
    stages {
        stage('Initialize') {
            steps {
                script {
                    def dockerHome = tool 'myDocker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                }
            }
        }
        stage('build') {
            agent { docker { image 'python:3.9.2-alpine3.13'}}
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                }
            }
        }
        stage('Docker Image') {
            steps {
                sh 'docker build -t gmanzone . '
            }
        }
        stage('Run Image / Container Creation') {
            steps {
                sh 'docker run -p 5000:5000 -d --name gmanzone-container gmanzone'
            }
        }
    }
}