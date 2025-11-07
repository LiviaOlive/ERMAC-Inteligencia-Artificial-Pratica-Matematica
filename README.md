# Animações Matemáticas com Manim - ERMAC 2025
![STATUS](https://img.shields.io/static/v1?label=STATUS&message=%20FINALIZADO&color=GREEN&style=for-the-badge)
<p>
Projeto desenvolvido durante o mini curso "Inteligência Artificial na Prática Docente de Matemática: Ferramentas, Exemplos e Criação Guiada de Materiais" no ERMAC (Encontro Regional de Matemática Aplicada e Computacional) na UFCA.

## 📋 Sobre o Projeto

Este projeto demonstra como criar animações matemáticas interativas usando a biblioteca Manim (Mathematical Animation Engine) para auxiliar no ensino de matemática. O foco principal é a visualização dinâmica de funções quadráticas e seus coeficientes.

## 🎯 Conteúdo

- **Parábola Animada**: Visualização da variação do coeficiente `b` em uma função quadrática `f(x) = ax² + bx + c`
- Demonstração do movimento do vértice da parábola
- Animação da linha vertical que passa pelo vértice

## 🚀 Como Executar

### Pré-requisitos

1. Python 3.8 ou superior
2. LaTeX (MiKTeX ou TeX Live) para renderização de fórmulas
3. Biblioteca Manim

### Instalação

```bash
# Clone ou baixe o projeto
cd ERMAC

# Instale o Manim
pip install manim

# Ou instale todas as dependências do projeto
pip install -r requirements.txt
```

### Executar a Animação

```bash
# Renderizar em qualidade baixa (mais rápido)
manim parabola_animada.py ParabolaAnimada -ql

# Renderizar em alta qualidade
manim parabola_animada.py ParabolaAnimada -qh
```

## 📁 Estrutura do Projeto

```
ERMAC/
├── parabola_animada.py    # Código principal da animação
├── requirements.txt       # Dependências do projeto
├── .gitignore             # Arquivos ignorados
└── README.md              # Este arquivo
```

## 🎓 Conceitos Matemáticos Abordados

- **Função Quadrática**: `f(x) = ax² + bx + c`
- **Vértice da Parábola**: `(-b/2a, -Δ/4a)`
- **Variação de Coeficientes**: Impacto do coeficiente `b` na forma da parábola

## 🛠️ Tecnologias Utilizadas

- **Manim**: Biblioteca para animações matemáticas
- **Python**: Linguagem de programação
- **LaTeX**: Sistema de composição tipográfica para fórmulas

## 📚 Recursos Adicionais

- [Documentação do Manim](https://docs.manim.community/)
- [Galeria de Exemplos](https://docs.manim.community/en/stable/examples.html)

## 👥 Autor

Desenvolvido durante o ERMAC 2024 - UFCA

---

*Este projeto faz parte do mini curso sobre uso de IA e ferramentas digitais no ensino de matemática.*
