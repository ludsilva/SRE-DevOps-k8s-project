# Estudos de Kubernetes | DevOps/SRE

## Objetivo

Este repositório foi criado como parte de uma mentoria de DevOps/SRE com foco em Kubernetes com a Dara Aragão, com o objetivo de consolidar conhecimentos práticos através da construção de projeto prático. A proposta é evoluir gradualmente de conceitos básicos até cenários mais próximos de produção.

## Tecnologias utilizadas

- Git e GitHub
- Python (Flask) e Redis
- Docker
- Kubernetes
- KIND (ambiente de testes locais)
- Helm
- ArgoCD

## Estrutura do repositório
```
├── app/
│   ├── src/
│   │   ├── app.py
│   │   ├── routes.py
│   │   ├── storage.py
│   │   └── metrics.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── README.md
│
├── k8s/
│   ├── namespace.yaml
│   ├── app-deployment.yaml
│   ├── app-service.yaml
│   ├── redis-deployment.yaml
│   └── redis-service.yaml
│
├── helm/
│   └── app-python/
│       ├── templates/
│       ├── Chart.yaml
│       └── values.yaml
│
├── kind-config.yaml
├── cosign.pub
├── LICENSE
└── README.md
```

## Arquitetura atual
O projeto consiste em:

- Uma aplicação com frontend, API REST em Flask e persistência com Redis;
- Containerização com Docker, imagem distroless (chainguard) com multi-stage;
- Deploy em Kubernetes;
- Exposição via Service do tipo NodePort (o cluster local foi criado utilizando o KIND com configuração customizada para expor portas no host)
- Gerenciamento via Helm;
- Deploy via ArgoCD (GitOps).


## Como utilizar este projeto
1. Clone o repositório para sua máquina local:
```bash
git clone https://github.com/ludsilva/SRE-DevOps-k8s-project.git
```

2. Navegue até o diretório do projeto:
```bash
cd SRE-DevOps-k8s-project
```

3. Criar o cluster KIND:
```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 30080
    hostPort: 8080
    protocol: TCP
- role: worker
- role: worker
```

4. Instalar o Argo e obter a senha

```bash
## Criar ns
kubectl create namespace argocd

## Instalar argo
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

## Aguardar subir
kubectl get pods -n argocd

## Obter a secret
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath='{.data.password}' | base64 -d

## Fazer o port forward
kubectl port-forward svc/argocd-server -n argocd 8081:443
```

5. Acessar o ArgoCD
```
https://localhost:8081
```
- User: admin

6. Deploy da aplicação
```bash
kubectl apply -f application.yaml
```
7. Acessar a aplicação
Via NodePort:
```
http://localhost:8080
```

## Observações importantes
- O NodePort no KIND não é exposto automaticamente no host. Foi necessário mapear a porta manualmente via `extraPortMappings`
- Para ambientes reais, o ideal seria utilizar **Ingress Controller**


## Próximos passos (desafios)
- Implementar HPA (Horizontal Pod Autoscaler);
- Configurar PodDisruptionBudget (PDB);
- Realizar testes e validar resiliência e auto healing;
- Evoluir observabilidade (Prometheus + Grafana).


## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.