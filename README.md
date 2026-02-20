🚀 Kubernetes Profile-Based Deployment Generator

projet réalisé par :
-Rai Hibet Allah
-Moulhabbas Hayette
-Challal sabine
-Fatou Bintou Sow

## 📌 Description

Ce projet permet de générer automatiquement :

* 🐳 Une image Docker personnalisée
* ☸️ Un Deployment Kubernetes
* 🌐 Un Service Kubernetes
* 🔐 Une NetworkPolicy sécurisée (default deny + règles d’ingress)

À partir d’un simple fichier **profil YAML**, le système génère tous les fichiers nécessaires au déploiement d’une application sur Kubernetes.

---

## 🎯 Objectif du Projet

L’objectif est de simplifier le déploiement d’environnements conteneurisés en automatisant :

* La génération d’un `Dockerfile`
* La création des manifestes Kubernetes
* L’application des bonnes pratiques de sécurité réseau

---

## 🏗️ Architecture du Projet

```
projet-k8s-generator/
│
├── profiles/
│   └── web-debian.yaml
│
├── generated/
│   ├── Dockerfile
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   └── networkpolicy.yaml
│
└── generator.py
```

---

## ⚙️ Technologies Utilisées

* 🐧 Ubuntu Desktop
* 🐳 Docker
* ☸️ Kubernetes (via Minikube)
* 🐍 Python 3
* YAML

---

## 🛠️ Prérequis

Avant d’utiliser ce projet, installez :

* Docker
* Kubectl
* Minikube
* Python 3 + pip

---

## 📥 Installation

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/ton-username/projet-k8s-generator.git
cd projet-k8s-generator
```

### 2️⃣ Installer les dépendances Python

```bash
pip install pyyaml
```

---

## 📝 Exemple de Profil YAML

`profiles/web-debian.yaml`

```yaml
profile_id: web-debian-v1

os: debian:12-slim

packages:
  - nginx
  - curl

network:
  default_deny: true
  ingress:
    - from: ingress
      protocol: TCP
      port: 80
```

---

## ⚡ Génération des Fichiers

```bash
python3 generator.py
```

Cela génère automatiquement :

* Dockerfile
* Manifestes Kubernetes

---

## 🐳 Build de l’Image Docker

```bash
eval $(minikube docker-env)
cd generated
docker build -t web-debian:v1 .
```

---

## ☸️ Déploiement Kubernetes

```bash
kubectl apply -f generated/
```

Vérifier :

```bash
kubectl get all -n web-debian
```

---

## 🌐 Test du Service

```bash
kubectl port-forward svc/web-service 8080:80 -n web-debian
```

Puis ouvrir :

```
http://localhost:8080
```

---

## 🔐 Sécurité Réseau

Le projet implémente :

* ✅ Default Deny Policy
* ✅ Autorisation uniquement du trafic TCP/80
* ❌ Blocage de tout autre trafic entrant

---

## 📊 Fonctionnement Global

1. Lecture du profil YAML
2. Génération automatique du Dockerfile
3. Build de l’image
4. Génération des manifests Kubernetes
5. Déploiement sur le cluster
6. Application des règles réseau

