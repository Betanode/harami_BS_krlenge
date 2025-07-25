# Volatility Generation using Conditional GANs (cGAN) and Quantum GANs (qGAN)
This project explores the application of Generative Adversarial Networks (GANs)—both classical and quantum—to model and generate market volatility based on real-world option chain data.

We are using Conditional GANs (cGANs) to learn a mapping between key financial features (such as strike price, open interest, premium values, and days to expiry) and the corresponding market volatility. The generator learns to simulate realistic volatility values conditioned on these features, while the discriminator distinguishes between real and generated values to improve training quality.

To further investigate the potential of Quantum Machine Learning in financial data modeling, we are planning to implement a Quantum GAN (qGAN) using IBM Qiskit. This allows us to evaluate and compare the performance of classical vs quantum models in terms of distribution matching, training stability, and sample efficiency on small, structured datasets.

🔍 Key Highlights
Input Data: Real option chain data with temporal awareness via DATE feature

Goal: Generate realistic volatility values conditioned on market features

Models:

Conditional GAN (cGAN) – implemented in PyTorch

Quantum GAN (qGAN) – implemented using Qiskit and hybrid quantum-classical setup

Output: Continuous volatility estimates for given feature vectors

Comparison: Classical vs Quantum performance on structured data generation

Planned Extensions:

Feature importance analysis

Streamlit/React dashboard for simulation and visualization

🛠 Tech Stack
Deep Learning: PyTorch

Quantum Computing: IBM Qiskit

Data Processing: Pandas, NumPy

Visualization: Matplotlib, Seaborn

(Planned) Frontend: Streamlit / React.js

Let me know if you want a shorter version or want to add contributors, licensing, or project structure sections.
