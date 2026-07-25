# AI/Data Science Interview Preparation — Master Project Charter

## The Interleaved Weekly Routine
* **Monday:** 1 SQL + 1 Python problem | ML & Stats (Competency 2)
* **Tuesday:** 1 SQL + 1 Python problem | Deep Learning & NLP (Competency 3)
* **Wednesday:** 1 SQL + 1 Python problem | Applied LLM Engineering (Competency 4)
* **Thursday:** 1 SQL + 1 Python problem | Lightweight MLOps (Competency 5)
* **Friday:** 1 SQL + 1 Python problem | System Design & Architecture (Competency 6)
* **Saturday:** Rest or light review | Mock Interviews & Project Defense (Competency 7)
* **Sunday:** Rest | Buffer day (catch up on missed topics)

---

## Competency 1: Programming & Data Foundations
**Why interviewers test this:** To ensure you can independently retrieve, clean, and manipulate data, and write code that is efficient enough for production environments. 
**Month-1 Recommendation:** Must Revise (Daily Warm-up)

### 1. SQL (Data Querying & Aggregation)
* **Core Retrieval & Logic:** `WHERE` vs. `HAVING`, `CASE WHEN ... THEN ... ELSE ... END`, `COALESCE()`, and `NULLIF()`.
* **Joins & Architecture:** `INNER`, `LEFT`, `RIGHT`, `FULL OUTER`, Self-joins, and `CROSS JOIN`. Query structuring using Common Table Expressions (CTEs with `WITH`).
* **Window Functions (High Frequency):** Ranking (`ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`), Offsets (`LEAD()`, `LAG()`), and Partitioned Aggregation (`SUM(col) OVER (PARTITION BY col2 ORDER BY col3)`).
* **Skip for Month 1:** Procedures, Triggers, Constraints.

### 2. Python (Core Algorithmic Foundations)
* **Data Structures & Efficiency:** Hash Maps (Dictionaries) for O(1) lookups, Sets for deduplication, Lists/Arrays (comprehensions, `enumerate`, `zip`, slicing).
* **Algorithmic Patterns:** Two-Pointer Technique, Sliding Window, String Manipulation (splitting, joining, basic regex).
* **Complexity Theory:** Big O Notation (Time and Space complexity).

### 3. Pandas & NumPy (Data Manipulation)
* **Pandas Essentials:** Inspection (`info`, `describe`, `value_counts`), Filtering (Boolean indexing), Aggregation (`groupby().agg()`, `pivot_table`), Combining (`merge`, `concat`), and Cleaning (`fillna`, `dropna`, `drop_duplicates`).
* **NumPy Essentials:** Vectorization over loops, Matrix Math (`np.dot`), Array Manipulation (`np.reshape`, `np.where`).

---

## Competency 2: Machine Learning & Statistical Modeling
**Why interviewers test this:** To evaluate your understanding of the math behind models, your ability to diagnose failures, and your skill in translating business problems into applied ML code.
**Month-1 Recommendation:** Must Revise

### 1. Data & Feature Engineering
* **Imbalanced Data:** SMOTE, undersampling, oversampling (avoiding data leakage), class weights.
* **Encoding:** One-Hot vs. Label/Ordinal vs. Target Encoding.
* **Scaling:** Standard vs. Min-Max Scaler (knowing which algorithms require scaling and which do not).
* **Missing Data:** Mean/Median imputation vs. predictive imputation.

### 2. Core Algorithms (Internals & Trade-offs)
* **Linear & Logistic Regression:** Assumptions (linearity, independence, homoscedasticity), coefficients, odds ratios.
* **Decision Trees:** Splitting criteria (Gini vs. Entropy, Variance Reduction).
* **Ensembles:** Bagging (Random Forests, reducing variance) vs. Boosting (AdaBoost, XGBoost, reducing bias, handling missing values natively).
* **Distance-Based:** KNN and K-Means (Curse of dimensionality).
* **Skip for Month 1:** Complex coding from scratch (SVM, XGBoost) and advanced mathematical proofs. Time Series (ARIMA, Prophet) pushed to "If Time".

### 3. Model Diagnostics & Validation
* **Bias-Variance Tradeoff:** Diagnosing underfitting vs. overfitting via learning curves.
* **Regularization:** L1 (Lasso/feature selection) vs. L2 (Ridge/shrinkage).
* **Cross-Validation:** K-Fold vs. Stratified K-Fold.

### 4. Evaluation Metrics
* **Classification:** Precision vs. Recall, F1-Score, ROC Curve & AUC (and when to use PR-AUC for imbalanced data).
* **Regression:** RMSE vs. MAE, R-Squared.

---

## Competency 3: Deep Learning & Applied NLP
**Why interviewers test this:** To see if you understand representation learning and the structural mechanics under the hood of neural networks before using APIs.
**Month-1 Recommendation:** Must Revise

### 1. Neural Network Fundamentals
* **Mechanics:** Forward & Backpropagation, gradient descent, chain rule.
* **Activation Functions:** ReLU, Leaky ReLU, Sigmoid, Softmax, GELU (knowing when to use which and how they impact gradients).
* **Loss Functions:** Cross-Entropy (binary/categorical) vs. MSE.
* **Optimization & Training:** SGD vs. Adam, learning rates, batch size, epochs, diagnosing vanishing/exploding gradients.

### 2. Embeddings & Vector Spaces
* **Representations:** Sparse (One-hot, TF-IDF) vs. Dense (Word2Vec, transformer embeddings).
* **Similarity:** Cosine Similarity vs. Dot Product.

### 3. Architecture Internals
* **CNNs:** Convolutional filters, stride, padding, pooling, receptive fields.
* **RNNs & LSTMs:** Recurrent connections, hidden states, gating mechanisms (forget/input/output).
* **Transformers (Crucial):** Self-Attention Mechanism (Q, K, V matrices), Multi-Head Attention, Positional Encoding, Encoder (BERT) vs. Decoder (GPT).

### 4. Applied NLP & Frameworks
* **Tokenization:** BPE, WordPiece, subword tokenization, handling out-of-vocabulary words.
* **Frameworks:** Building PyTorch/TensorFlow pipelines, loading Hugging Face weights, layer freezing for transfer learning.
* **Skip for Month 1:** Coding complex custom architectures (e.g., custom LSTMs) from scratch.

---

## Competency 4: Applied LLM Engineering
**Why interviewers test this:** To prove you can build reliable, automated software systems around foundation models, bypass hallucinations, and adapt models securely.
**Month-1 Recommendation:** Must Revise

### 1. Retrieval-Augmented Generation (RAG) Architecture
* **Data & Chunking:** Document loaders, fixed-size vs. recursive vs. semantic chunking.
* **Vector Databases & Retrieval:** Dense (Embedding) vs. Sparse (BM25) vs. Hybrid search.
* **Advanced Retrieval:** Re-ranking (Cross-Encoders), Query Expansion.
* **Evaluation:** Measuring relevance and context precision (e.g., RAGAS).

### 2. Fine-Tuning & Adaptation Techniques
* **Decision Making:** Prompting vs. RAG vs. Fine-Tuning (cost, latency, knowledge vs. behavior).
* **PEFT:** LoRA (Low-Rank Adaptation math and mechanics), QLoRA (quantization).
* **Alignment Basics:** Instruction tuning, SFT, conceptual understanding of RLHF/DPO.
* **Skip for Month 1:** Pre-training foundation models from scratch.

### 3. Prompt Engineering & Mechanics
* **Advanced Techniques:** Few-Shot, Chain-of-Thought (CoT), Tree of Thoughts.
* **Mitigations:** Guardrails for hallucinations and toxicity.
* **Context Windows:** Token limits and the "lost in the middle" phenomenon.

### 4. Agentic Workflows & Tool Calling
* **Function Calling:** Structuring JSON outputs to trigger APIs.
* **Frameworks:** ReAct framework, LangChain, LlamaIndex (and their abstractions/drawbacks).

---

## Competency 5: Engineering Foundations & Lightweight MLOps
**Why interviewers test this:** To ensure you can take a trained model, package it, and wrap it in a code interface that other systems can securely interact with.
**Month-1 Recommendation:** Targeted Net-New Learning (Strictly bounded)

### 1. API Development (FastAPI)
* **The Framework:** Why FastAPI (async, automatic docs, speed).
* **Data Validation:** Pydantic `BaseModel` classes for strict input typing.
* **Endpoints:** Creating `@app.post("/predict")` routes to handle JSON payloads and return model predictions.
* **Error Handling:** Standard HTTP status codes.

### 2. Containerization Basics (Docker)
* **Concepts:** Solving the "works on my machine" problem; Images vs. Containers.
* **Dockerfile Commands:** `FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD`.
* **Port Mapping:** Exposing container ports locally.

### 3. Experiment Tracking (MLflow)
* **Core Functions:** Logging parameters (`log_param`), logging metrics (`log_metric`), and saving artifacts/models to a registry.

### 4. Code Packaging & GitHub Hygiene
* **Repository Structure:** Clean local directories (`src/`, `data/`, `models/`).
* **Environment Management:** `requirements.txt` or `environment.yml`.
* **Skip for Month 1:** Kubernetes, Spark, Airflow, complex distributed cloud deployment.

---

## Competency 6: AI/ML System Design
**Why interviewers test this:** To see if you can translate ambiguous business goals into concrete, end-to-end technical architectures while communicating trade-offs.
**Month-1 Recommendation:** Must Learn (Focus on framework and case studies)

### 1. Problem Framing
* **Clarifying:** Translating business goals into ML objectives.
* **Constraints:** Identifying latency and scale requirements.
* **Metrics:** Defining Offline (RMSE, F1) vs. Online (Conversion Rate, Revenue) metrics.

### 2. Data Engineering & Features
* **Pipelines:** Data sources, feature engineering, and the role of Feature Stores in preventing training-serving skew.

### 3. Model Selection
* **Strategy:** Always starting with a simple baseline/heuristic before proposing complex architectures. Justifying model choice based on constraints.

### 4. Serving & Deployment Strategy
* **Inference:** Batch (offline) vs. Real-Time (online/API).
* **Releases:** A/B Testing, Shadow Mode, Canary Deployment.

### 5. Monitoring & Maintenance
* **Drift:** Detecting Data Drift vs. Concept Drift.
* **Feedback:** Explicit vs. Implicit feedback loops for retraining.

### 6. LLM-Specific System Design
* **Architecture:** Diagramming RAG flows.
* **Optimization:** Semantic caching to reduce cost/latency.
* **Safety:** Guardrail models before and after LLM inference.
* **Skip for Month 1:** Deep backend software engineering architecture (load balancers, database sharding).

---

## Competency 7: Project Defense & Behavioral Communication
**Why interviewers test this:** To verify authenticity, assess cross-functional communication skills, and determine culture fit.
**Month-1 Recommendation:** Must Revise

### 1. The Technical Project Deep-Dive
* **The "Why":** Defending architectural choices over simpler baselines (e.g., CNNs vs. Random Forests, local WSL setups vs. cloud).
* **The Data & Infrastructure:** Explaining data collection, bias handling, cleaning, and deployment choices.
* **The Impact:** Quantifying final results (accuracy, speed, business value).

### 2. The STAR Method Arsenal
* **Stories to Prepare:** A specific Success, a specific Failure (and lessons learned), a Conflict resolution, and a Pivot/adapting to changing requirements. 

### 3. Cross-Functional Translation
* **Communication:** Explaining deep technical concepts (like Transformers or p-values) to non-technical stakeholders without jargon. Framing technical work in terms of business ROI.

### 4. Behavioral Red Flags to Avoid
* Blaming others (using "We" for team successes, owning your own actions).
* Over-claiming (admitting when a standard architecture or tutorial was used as a baseline).