pipeline {
    agent any // Diz que a pipeline pode rodar em qualquer executor disponível

    parameters {
        // Define padrões, mas permite que você mude na hora de rodar
        string(name: 'DOCKER_USER', defaultValue: 'mateusr1', description: 'Usuário do Docker Hub')
        string(name: 'APP_NAME', defaultValue: 'meu-app', description: 'Nome da Imagem/App')
    }

    environment {
        // Puxa a senha do cofre usando o ID 
        DOCKER_CREDS = credentials('docker-hub-credentials')
        DOCKER_IMAGE = "${params.DOCKER_USER}/${params.APP_NAME}"
        // A tag v1, v2... será o número do build do Jenkins
        IMAGE_TAG = "v${env.BUILD_ID}"
    }

    stages {
        stage('Checkout') {
            steps {
                // Baixa o código mais recente do GitHub
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    echo "Iniciando fabricação da imagem: ${DOCKER_IMAGE}:${IMAGE_TAG}"
                    // O comando 'docker.build' lê o seu Dockerfile local
                    appImage = docker.build("${DOCKER_IMAGE}:${IMAGE_TAG}")
                }
            }
        }

        stage('Docker Push') {
            steps {
                script {
                    echo "Enviando imagem para o Docker Hub..."
                    // Faz o login automático, envia a imagem e faz logout
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        appImage.push()
                        // marcar como 'latest' para facilitar testes rápidos
                        appImage.push("latest")
                    }
                }
            }
        }

        stage('Update GitOps (Kustomize)') {
            steps {
                script {
                    echo "Atualizando a tag na imagem no ArgoCD..."
                    
                    withCredentials([usernamePassword(credentialsId: 'github-token-jenkins', passwordVariable: 'GIT_PASS', usernameVariable: 'GIT_USER')])
                    sh """
                    cd overlays/producao
                    sed -i 's/newTag: .*newTag: ${IMAGE_TAG}/' kustomization.yaml

                    git config --global user.mail "jenkins@lab-gitops.local"
                    git config --global user.name "Jenkins"
                    git add kustomization.yaml
                    git commit -m "CI: Deploy automático da versão ${IMAGE_TAG}" 
                    git push https://\${GIT_USER}:\${GIT_PASS}https://github.com/Mateus-R-Silva/lab-gitops.git HEAD:main
                    """
                }
            }
        }

        stage('Notificação') {
            steps {
                echo "Pipeline finalizado com sucesso! Imagem ${DOCKER_IMAGE}:${IMAGE_TAG} disponível."
            }
        }
    }
}