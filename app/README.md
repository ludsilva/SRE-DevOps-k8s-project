# Flask API - Python Distroless

Minimal REST API com segurança via imagem Chainguard distroless e scan de vulnerabilidades com Trivy.

## Stack

- Python 3.14
- Flask 3.1.3 (atualizado de 3.0.3)
- Chainguard distroless image (wolfi)
- Multi-stage Docker build
- Trivy para vulnerability scanning

## API Routes - `script.py`

| Route | Method | Response | Description |
|-------|--------|----------|-------------|
| `/` | GET | `200 HTML` | Hello World |
| `/health` | GET | `200 {"status": "ok"}` | Health check |
| `<qualquer inválida>` | * | `404 {"error": "Route not found"}` | Rota não encontrada |

## Dockerfile

Multi-stage build: a stage de build usa a variante `-dev` para instalar dependências; a stage de runtime usa a imagem distroless mínima.

### Run

```bash
docker build -t ludsilva/app-python-distroless:1.0 .
docker run -p 5000:5000 ludsilva/app-python-distroless:1.0
```

## Security - Trivy Scan

Dois scans foram executados. O primeiro detectou uma vulnerabilidade LOW no Flask. Após o upgrade, o segundo scan retornou zero findings.

### Scan 1 - Vulnerabilidade Encontrada

| Library | CVE | Severity | Status | Installed | Fixed |
|---------|-----|----------|--------|-----------|-------|
| Flask | CVE-2026-27205 | LOW | fixed | 3.0.3 | 3.1.3 |

**Descrição:** Information disclosure via improper caching of session data.  
**Referência:** https://avd.aquasec.com/nvd/cve-2026-27205

### Scan 2 - Zero Vulnerabilidades

Após o upgrade do Flask para 3.1.3, o scan retornou 0 vulnerabilidades em todos os 9 pacotes escaneados.

```
Total: 0 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0)
```

---

## Fix Aplicado

```txt
# Antes
flask==3.0.3

# Depois
flask==3.1.3
```
