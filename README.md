# 🏦 Bank Simulation API test (Kubernetes + Ingress + Traefik)
A simple banking simulation application (for API test) built to learn **Kubernetes orchestration**, **Ingress**, **service networking**, and **DevOps fundamentals**. This project demonstrates how a multi-tier application (Frontend, Backend, Database) is deployed and connected inside a Kubernetes cluster.
<img width="3232" height="3000" alt="image" src="https://github.com/user-attachments/assets/88780c07-a306-4e73-9649-1c8600377758" />


---

## ✨ Technology

- Frontend (HTML + JavaScript)
- Backend API (Python/FlaskAPI)
- PostgreSQL database
- Kubernetes Deployment & Service
- Ingress with Traefik
- Port-forwarding for local development

---

## 🏗️ Architecture Overview
`user -> localhost:8000 -> K8s API server -> Traefik -> Ingress rules -> FE -> BE -> Database`

---

## 🧱 Detail Components

### Frontend
- Static HTML + JavaScript
- Calls backend API via `/api/*`
- Served by NGINX inside a Kubernetes Pod

### Backend
- Python-based (FastAPI) REST API
- Handles:
  - Create account
  - Get balance
  - Add balance
  - Transfer balance
  - List of accounts & transactions

### Database
- PostgreSQL
- Persistent storage using PVC (Persistent Volume Claim)
- Tables:
  - `accounts`
  - `transactions`

---

## 🚀 How to Run (Local Development)

### 1. Prerequisites

- Kubernetes cluster (tested on Rancher Desktop)
- kubectl
- Docker
- Git

---

### 2. Clone Repository

```bash
git clone https://github.com/FajarRamadhanBBX/orchestrate-bank-api-test.git
cd orchestrate-bank-api-test
```

### 3. Deploy
```bash
kubectl apply -f kubernetes/
```
you can check the status of resources with:
```bash
kubectl get pods -n development-bank-app
```

### 4. Port-Forwarding
```bash
kubectl port-forward -n kube-system svc/traefik 8080:80
```
**Notes**: Keep this terminal running.

### 5. Open application
Open browser and go to:
```bash
http://localhost:8080
```

---

## 📚 Key Learnings
- How Ingress works with Traefik to serve request to right service
- Service -> targetPort -> containerPort mapping
- Rolling updates and replica management
