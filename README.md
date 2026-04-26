# Estudos de Kubernetes | DevOps/SRE

## Objetivo

Este repositório foi criado como parte de uma mentoria de DevOps/SRE com foco em Kubernetes com a Dara Aragão, com o objetivo de consolidar conhecimentos práticos através da construção de projeto prático. A proposta é evoluir gradualmente de conceitos básicos até cenários mais próximos de produção.

## Tecnologias utilizadas

- Git e GitHub
- Python
- Docker
- Kubernetes
- KIND (para testes locais)

## Estrutura do repositório
```
├── script.py
├── README.md
```

## Arquitetura atual
O projeto consiste em:

- Uma aplicação python simples com Flask;
- Containerização com Docker, imagem distroless (chainguard) com multi-stage;
- Deploy em Kubernetes;
- Exposição via Service do tipo NodePort (o cluster local foi criado utilizando o KIND com configuração customizada para expor portas no host)

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

4. Deploy da aplicação
```bash
kubectl apply -f k8s/
```

5. Acessar à aplicação via localhost:
```bash
http://localhost:8080
```
6. (opcional) Setar o namespace como current

```bash
kubectl config set-context --current --namespace=dev
```

### Validações realizadas

* Deployment criado com sucesso
* Pods em estado Running
* Healthchecks configurados (`/health`)
* Service funcionando corretamente
* Aplicação acessível via navegador/curl

## Observações importantes

* O NodePort no KIND não é exposto automaticamente no host
* Foi necessário mapear a porta manualmente via `extraPortMappings`
* Para ambientes reais, o ideal seria utilizar **Ingress Controller**


## Próximos passos (desafios)

* Evoluir a aplicação (opcional);
* Implementar HPA, PDB
* Utilizar Helm
* GitOps com Argo
* Adicionar observabilidade (logs e métricas)


## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.