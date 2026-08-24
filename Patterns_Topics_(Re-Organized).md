# Master Index: Interview Patterns (Reorganized for 60-Day Prep)

> **How to use this playbook:**
> Whenever you open a fresh chat thread for a PDF pattern, copy the Prompt from **pattern_topic_wise_generation_prompt**, insert the corresponding **Pattern ID & Name**, and paste it into the chat prompt.

---
---

## 1. Core SQL & Advanced Data Aggregations

### Basic Aggregation & Filtering
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
|🟢 [PAT-15] | Missing Values Detection | Auditing NULL rates, COALESCE(), NULLIF(), and NULL logic. |
|🟢 [PAT-25] | CASE WHEN Categorization | Conditional logic, bucketing, conditional aggregation. |
|🟢 [PAT-01] | GROUP BY + COUNT | Counting rows per category, handling NULLs vs COUNT(*). |
|🟢 [PAT-02] | GROUP BY + SUM/AVG | Grouped numerical metrics, filtering with HAVING. |

### Joins & Structural Logic
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
|🟢 [PAT-18] | LEFT JOIN vs INNER JOIN | Unmatched row retention, Anti-JOINs (WHERE right.key IS NULL). |
|🟢 [PAT-16] | JOIN Multiple Tables | Chaining 3+ table JOINs, foreign keys, execution order. |
|🟢 [PAT-17] | Self JOIN | Hierarchical data (employee-manager), row comparison within same table. |
|🟢 [PAT-28] | Subquery Pattern | Scalar, correlated, and derived tables; IN vs EXISTS. |
|🟢 [PAT-29] | CTE Pattern | Common Table Expressions (WITH clause) for readable multi-step logic. |
|🟢 [PAT-30] | Recursive Query Pattern | WITH RECURSIVE for organizational hierarchies and date series generation. |

### Window Functions & Ranking
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
|🟢 [PAT-19] | Window Function Ranking | Differences between ROW_NUMBER(), RANK(), and DENSE_RANK(). |
|🟢 [PAT-21] | ROW_NUMBER Pattern | Unique sequential numbering, pagination, single top record per group. |
|🟢 [PAT-22] | Dense Ranking Pattern | Nth highest values with ties, no rank gaps. |
|🟢 [PAT-03] | Top N Records | Global Top N via LIMIT vs per-group Top N via ROW_NUMBER(). |
|🟢 [PAT-04] | Second Highest Value | Nth highest salary without LIMIT; subqueries vs DENSE_RANK(). |
|🟢 [PAT-23] | Percentile Calculation | PERCENT_RANK(), CUME_DIST(), NTILE(), PERCENTILE_CONT(). |

### Time-Series & Cumulative Metrics
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
|🟢 [PAT-07] | Date Difference | Date arithmetic, DATEDIFF, DATE_TRUNC, and duration metrics. |
|🟢 [PAT-20] | LAG and LEAD | Accessing adjacent row values for period-over-period trends. |
|🟢 [PAT-09] | User Growth Over Time | Month-over-Month (MoM) growth calculations using LAG(). |
|🟢 [PAT-05] | Running Total | Cumulative SUM using OVER (ORDER BY date). |
|🟢 [PAT-06] | Rolling Average | Moving averages using ROWS BETWEEN N PRECEDING AND CURRENT ROW. |

### Advanced Analytics & Product Metrics
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
|🟢 [PAT-10] | Daily Active Users (DAU) | Unique daily engagement, DAU/MAU stickiness ratios. |
|🟢 [PAT-11] | Monthly Active Users (MAU) | Counting unique users per month, MoM user retention. |
|🟢 [PAT-14] | Duplicate Removal | Deduplicating records using ROW_NUMBER() PARTITION BY. |
|🟢 [PAT-24] | Median Calculation | Computing median in SQL without built-in MEDIAN() functions. |
|🟢 [PAT-26] | Pivot Table Pattern | Converting long data to wide format using SUM(CASE WHEN). |
|🟢 [PAT-27] | Unpivot Pattern | Reshaping wide data to long format using UNION ALL. |
|🟢 [PAT-12] | Conversion Funnel | Multi-step drop-off analysis using conditional COUNT(DISTINCT CASE). |
|🟢 [PAT-08] | Cohort Retention | User retention matrices, signup cohorts, tracking activity over time. |
|🟢 [PAT-13] | Sessionization | Grouping raw clickstreams into sessions using time gaps & LAG(). |

---

## 2. Statistics, Probability & Distributions

### Descriptive Stats & Distributions
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
|🟢 [PAT-31] | Mean vs Median | Central tendency under skewness and outliers, trimmed mean. |
|🟢 [PAT-32] | Standard Deviation | Sample vs population standard deviation, Bessel correction (ddof=1). |
|🟢 [PAT-33] | Outlier Detection | Z-score thresholding vs IQR method (Tukey fences). |
|🟢 [PAT-56] | Normal Distribution | Bell curve PDF, Empirical Rule (68-95-99.7), Z-score standardization. |
|🟢 [PAT-57] | Binomial Distribution | PMF for fixed independent binary trials, A/B test conversion modeling. |
|🟢 [PAT-58] | Poisson Distribution | Modeling rare events in fixed intervals, Mean = Variance = Lambda. |
|🟢 [PAT-59] | Expected Value | Probability-weighted averages, decision tree split evaluation. |

### Probability Basics & Bayes
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
|🟢 [PAT-34] | Probability Basics | Addition rule, multiplication rule, complement rule. |
|🟢 [PAT-35] | Conditional Probability | P(A\|B) formula, contingency tables, independence tests. |
| [PAT-36] | Bayes Theorem | Prior, likelihood, posterior calculation, Base Rate Fallacy. |

### Inferential Stats & Hypothesis Testing
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [PAT-37] | Sampling Distribution | Distribution of sample statistics, Standard Error (SE = sigma/sqrt(n)). |
| [PAT-38] | Central Limit Theorem | CLT mechanics, sample size rules (n >= 30), application to A/B testing. |
| [PAT-39] | Confidence Interval | Margin of error, z* critical values, interpreting 95% CIs correctly. |
| [PAT-41] | Null vs Alternative Hypothesis | Stating H0 and H1, one-tailed vs two-tailed tests. |
| [PAT-43] | Type I and Type II Error | False positives (alpha), false negatives (beta), statistical power (1-beta). |
| [PAT-45] | Power Analysis | Minimum Detectable Effect (MDE), computing required sample size. |
| [PAT-40] | Hypothesis Testing | 7-step testing framework, test selection (z-test vs t-test vs chi-square). |
| [PAT-42] | p-value Interpretation | Definition of p-value, decision rules, statistical vs practical significance. |
| [PAT-44] | A/B Testing | Randomized controlled trial setup, two-proportion z-test, lift metrics. |

### Causation & Relationships
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [PAT-47] | Covariance | Unnormalized co-movement of variables, covariance matrix calculation. |
| [PAT-46] | Correlation vs Causation | Pearson r, confounders, spurious correlation, establishing causality. |
|🟢 [PAT-60] | Simpson's Paradox | Trend reversal in aggregated vs subgroup data, confounding variables. |

---

## 3. Machine Learning Preprocessing, Training & Core Algorithms

### Data Splitting & Leakage
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
|🟢 [PAT-61] | Train-Test Split | Stratified splits, random seed setting, avoiding data leakage. |
|🟢 [PAT-62] | Cross-Validation | K-Fold vs Stratified K-Fold CV, preventing leakage with Pipelines. |
|🟢 [PAT-96] | Data Leakage | Identifying train-test leakage, target leakage, temporal leakage. |

### Preprocessing & Feature Engineering
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
|🟢 [PAT-64] | Missing Value Imputation | Mean/Median vs KNN/Iterative imputation, fitting only on train set. |
|🟢 [PAT-63] | Feature Engineering | Creating ratios, log transformations, date extractions, binning. |
|🟢 [PAT-65] | Encoding Categoricals | Choosing between Nominal (OHE) and Ordinal (Label/Ordinal) encoding. |
|🟢 [PAT-66] | One-Hot Encoding | Binary columns, Dummy Variable Trap (drop_first=True). |
|🟢 [PAT-67] | Label Encoding | Mapping categories to integers, tree model compatibility. |
|🟢 [PAT-68] | Feature Scaling | When algorithms require scaling (distance/gradient-based vs tree-based). |
|🟢 [PAT-69] | Standardization vs Normalization | Z-score (StandardScaler) vs Min-Max (MinMaxScaler), handling outliers. |
|🟢 [PAT-50] | Multicollinearity | Variance Inflation Factor (VIF > 10), unstable regression coefficients. |

### Regression & Linear Models
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
|🟢 [PAT-48] | Linear Regression Interpretation | OLS coefficients, R-squared vs Adjusted R-squared, LINE assumptions. |
|🟢 [PAT-49] | Logistic Regression Interpretation | Log-odds, sigmoid transformation, interpreting Odds Ratios exp(beta). |
|🟢 [PAT-72] | Regularization | Loss penalties, controlling model complexity via hyperparameter lambda/C. |
|🟢 [PAT-73] | L1 vs L2 | Lasso (L1) feature selection vs Ridge (L2) coefficient shrinkage. |

### Distance-Based & Probabilistic Models
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
|🟢 [GAP-ML-02] | K-Nearest Neighbors & Distance Metrics | KNN classification/regression, Curse of Dimensionality, distance metrics (Euclidean, Manhattan, Cosine, Mahalanobis). |
|🟢 [GAP-ML-03] | Naive Bayes Classifier | Bayes Theorem applied to classification, Independence assumption, Gaussian vs. Multinomial NB, Laplace Smoothing. |
|🟢 [GAP-ML-01] | Support Vector Machines (SVM) | Maximum margin hyperplanes, support vectors, soft margins (C hyperparameter), Kernel Trick (RBF, Polynomial). |

### Tree-Based Models & Ensembles
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [PAT-74] | Decision Tree | Impurity split criteria (Gini vs Entropy), controlling depth to prevent overfit. |
| [PAT-75] | Random Forest | Bagging ensemble, bootstrap sampling, feature randomness, OOB score. |
| [PAT-76] | Gradient Boost | Sequential boosting, residual fitting, learning rate shrinkage. |
| [PAT-77] | XGBoost | Optimized boosting, built-in L1/L2 regularization, early stopping. |

### Unsupervised Learning
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [PAT-78] | Clustering | Unsupervised grouping, metric evaluation (Silhouette score vs Inertia). |
| [PAT-79] | K-Means | Centroid-based partitioning, Elbow Method, K-Means++ initialization. |
| [PAT-80] | Hierarchical | Agglomerative tree clustering, dendrograms, Ward linkage. |
| [PAT-81] | PCA Dimensionality Reduction | Max variance projections, eigenvectors/values, cumulative variance plot. |

---

## 4. Evaluation Metrics & Explainability

### Model Diagnostics
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
|🟢 [PAT-51] | Bias-Variance Tradeoff | Underfitting vs overfitting, total error decomposition. |
|🟢 [PAT-70] | Overfitting Detection | Diagnostic learning curves, monitoring train vs test accuracy gap. |
|🟢 [PAT-71] | Underfitting Detection | High bias symptoms, increasing model capacity and feature set. |

### Classification Metrics
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
|🟢 [PAT-55] | Imbalanced Dataset | SMOTE oversampling, class_weight='balanced', threshold shifting. |
|🟢 [PAT-52] | Precision vs Recall | Tradeoffs when FP cost differs from FN cost, classification threshold tuning. |
|🟢 [PAT-53] | F1 Score | Harmonic mean of Precision and Recall, F-beta score variants. |
|🟢 [PAT-54] | ROC-AUC | Receiver Operating Characteristic curve, threshold-independent ranking evaluation. |

### Explainability
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [PAT-97] | Feature Importance | Tree-based Gini importance vs model-agnostic Permutation importance. |
| [PAT-98] | SHAP Values | Game-theoretic Shapley explanations, global summary vs local waterfall plots. |

---

## 5. Applied ML: RecSys, Time Series & Anomaly Detection

| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [PAT-82] | Recommendation Systems | Personalization overview, user-item interaction matrix, ranking metrics. |
| [PAT-84] | Content-Based Filtering | Item feature matching, TF-IDF + Cosine similarity, filter bubble risk. |
| [PAT-83] | Collaborative Filtering | User-User vs Item-Item CF, Matrix Factorization (SVD, ALS). |
| [PAT-85] | Time Series Forecasting | Trend, seasonality, stationarity (ADF test), chronological splits. |
| [PAT-86] | ARIMA Pattern | AutoRegressive Integrated Moving Average, selecting (p, d, q) via ACF/PACF. |
| [PAT-90] | Anomaly Detection | Unsupervised outlier finding: Isolation Forest, contamination parameter. |

---

## 6. Deep Learning, CNNs & Network Optimization

### Neural Network Foundations & Optimization
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [PAT-91] | Neural Network Basics | Dense layers, forward pass, backpropagation, gradient updates. |
| [PAT-92] | Activation Functions | Non-linearity: ReLU, Sigmoid, Tanh, Softmax, Vanishing Gradient problem. |
| [GAP-DL-01] | Vanishing & Exploding Gradients | Weight Initialization (He/Xavier), Gradient Clipping, mathematical intuition of the chain rule and vanishing gradients. |
| [GAP-DL-02] | Advanced Optimizers | Adam vs. RMSprop vs. SGD with Momentum; adaptive learning rates, exponentially weighted moving averages. |
| [GAP-DL-03] | Normalization Techniques | Batch Normalization vs. Layer Normalization; when to use which (CNNs vs. Transformers), internal covariate shift. |
| [GAP-DL-04] | Regularization Strategies | Dropout mechanics, L1 (Lasso) vs. L2 (Ridge) Weight Decay, Early Stopping implementation and trade-offs. |

### Convolutional Neural Networks
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [PAT-93] | CNN Basics | Convolutional filters, stride, padding, Max Pooling, spatial hierarchies. |
| [GAP-CNN-01] | Advanced Convolutions | 1x1 Convolutions (dimensionality reduction), Depthwise Separable Convolutions (computational efficiency, MobileNet). |
| [GAP-CNN-02] | Residual Networks (ResNet) | Skip/Residual connections, solving the vanishing gradient problem in ultra-deep networks, identity mapping. |
| [GAP-CNN-03] | Transfer Learning & Fine-Tuning | Freezing base layers vs. unfreezing, replacing the classification head, feature extraction vs. full fine-tuning trade-offs. |
| [GAP-CNN-04] | Object Detection Mechanics | Intersection over Union (IoU), Anchor boxes, Non-Maximum Suppression (NMS), high-level YOLO vs. R-CNN differences. |

---

## 7. NLP, Sequential Data & Attention Mechanisms

### Traditional NLP & Embeddings
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [PAT-87] | NLP Basics | Text preprocessing pipeline: tokenization, stop words, lemmatization. |
| [PAT-88] | TF-IDF | Term Frequency x Inverse Document Frequency formula, sparse vectors. |
| [PAT-89] | Word Embeddings | Dense semantic vectors: Word2Vec (CBOW/Skip-gram), GloVe, Sentence-BERT. |
| [GAP-ATTN-04] | Word Embeddings & Latent Space | Static (Word2Vec/GloVe) vs. Contextual embeddings; semantic mapping and linear relationships in high-dimensional space. |

### Sequential Models
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [GAP-SEQ-01] | RNNs & Long-Term Dependency Limits | Backpropagation through time (BPTT), why standard RNN architectures fail at capturing long-range context. |
| [GAP-SEQ-02] | LSTM & GRU Architectures | Forget, Input, and Output gates in LSTMs; Update and Reset gates in GRUs; how they solve the vanishing gradient problem. |
| [GAP-SEQ-03] | Seq2Seq Models & Context Vectors | Encoder-Decoder architecture mechanics, the information bottleneck problem of fixed-length context vectors. |

### Attention & Transformer Basics
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [GAP-ATTN-01] | Traditional Attention Mechanisms | Bahdanau (Additive) vs. Luong (Multiplicative) attention; moving from fixed to dynamic context vectors. |
| [GAP-ATTN-02] | Self-Attention Mechanics | Q, K, V matrices; calculating attention weights; scaled dot-product formula and softmax operations. |
| [GAP-ATTN-03] | Transformer Architecture Core | Positional Encoding (Sine/Cosine intuition), Encoder vs. Decoder blocks, Masked Self-Attention in decoders. |

---

## 8. LLM Architecture & Fine-Tuning

### Core LLM Architecture & Inference
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [GAP-LLM-01] | Transformer Mechanics & Self-Attention | Self-Attention math (Q, K, V), O(N^2) sequence complexity, Scaled Dot-Product Attention. |
| [GAP-LLM-02] | Attention Variants (MHA vs. GQA vs. MQA) | Multi-Head vs. Grouped-Query vs. Multi-Query Attention; memory bandwidth vs. quality trade-offs. |
| [GAP-LLM-03] | Positional Embeddings (RoPE, ALiBi, Absolute) | Absolute vs. Relative embeddings, Rotary Position Embeddings (RoPE) mechanics, context window extension. |
| [GAP-LLM-04] | Tokenization Algorithms | Byte-Pair Encoding (BPE), WordPiece, SentencePiece, handling Special Tokens, OOV token problems. |
| [GAP-LLM-05] | Inference Optimization (KV Cache, FlashAttention) | Key-Value Caching memory bottleneck, PagedAttention (vLLM), FlashAttention IO-awareness, Quantization (INT8/INT4). |

### Fine-Tuning & Alignment
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [GAP-FT-04] | Dataset Preparation for Instruction Tuning | Formatting chat templates (ShareGPT, Alpaca), system prompt alignment, synthetic data generation. |
| [GAP-FT-01] | Full Fine-Tuning vs. PEFT | Computational & memory requirements of full SFT vs. Parameter-Efficient Fine-Tuning; memory estimation formulas. |
| [GAP-FT-02] | LoRA & QLoRA Mechanics | Low-Rank Matrices (A x B), Rank r, Alpha scaling, 4-bit NormalFloat (NF4), Double Quantization, Paged Optimizers. |
| [GAP-FT-03] | Alignment (RLHF vs. DPO vs. KTO) | Reward modeling, PPO mechanics, Direct Preference Optimization (DPO) without reward models, Kahneman-Tversky Optimization. |

---

## 9. Prompting, RAG & LLM Agents

### Prompt Engineering & Retrieval
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| **[GAP-PRM-01]** | **Advanced Prompt Engineering** | **Zero-shot, Few-shot, Chain-of-Thought (CoT), output formatting (JSON schemas), and prompt caching fundamentals.** |
| [GAP-RAG-01] | Document Chunking Strategies | Fixed-size vs. Recursive Character vs. Semantic vs. Agentic chunking; chunk overlap selection. |
| [GAP-RAG-05] | Vector Database Selection & Benchmarking | Detailed comparison: ChromaDB, FAISS, Pinecone, Qdrant, Weaviate (In-memory vs. Cloud vs. Self-hosted). |
| [GAP-RAG-02] | Dense vs. Sparse Retrieval (Hybrid Search) | Dense Embeddings vs. BM25 (sparse); Reciprocal Rank Fusion (RRF) for combining vector + keyword search. |
| [GAP-RAG-03] | Reranking & Context Compression | Bi-Encoders vs. Cross-Encoders; using rerankers (Cohere/BGE) to optimize context window and reduce noise. |
| [GAP-RAG-04] | Advanced RAG Architectures | HyDE (Hypothetical Document Embeddings), Parent-Child Chunking, Sentence-Window Retrieval, Multi-Query Expansion. |

### LLM Agents
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [GAP-AGT-02] | Tool Use & Function Calling | JSON Schema generation, API parsing, handling tool invocation failures, structured output enforcement (Pydantic/Instructor). |
| [GAP-AGT-01] | Agentic Reasoning Patterns | ReAct (Reasoning + Acting), Plan-and-Solve, Self-Correction/Reflection loops, Tree of Thoughts. |
| [GAP-AGT-03] | Multi-Agent Systems & State Management | Hierarchical vs. Sequential agent graphs, state persistence, handling context window blowup, avoiding infinite loops. |

---

## 10. LLM Evaluation, MLOps & System Design

### GenAI Evaluation & Security
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [GAP-EVAL-01] | RAG Evaluation Frameworks (RAGAS) | Measuring RAG Triad: Faithfulness, Answer Relevance, Context Precision, Context Recall; automated test generation. |
| [GAP-EVAL-02] | LLM-as-a-Judge & G-Eval | Pairwise comparison vs. Single-answer scoring, mitigating position bias and verbosity bias in evaluator LLMs. |
| [GAP-EVAL-03] | Guardrails, Moderation & Security | Prompt Injection attacks, PII redaction, input/output filtering, NeMo Guardrails / Llama Guard implementations. |

### MLOps & Deployment
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [PAT-99] | Experiment Tracking | Logging parameters, metrics, artifacts, and model versions via MLflow. |
| [PAT-94] | Model Deployment | Serving models via Flask/FastAPI REST APIs, Docker containerization. |
| [PAT-95] | Batch vs Real-Time Prediction | Low-latency streaming/API inference vs high-throughput batch scoring. |
| **[GAP-SYS-05]** | **Model Deployment & Rollout Strategies** | **A/B testing deployments, Canary rollouts, Shadow deployments, and resolving model registry consistency.** |
| [PAT-100] | Dashboard Metrics | Monitoring production performance, detecting Population Stability Index (PSI) drift. |

### System Design
| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
| [GAP-SYS-01] | ML System Design Framework | Standard 5-step framework: Business Requirements, Data Pipeline, Feature Engineering/Embeddings, Model Architecture, Serving & Monitoring. |
| [GAP-SYS-02] | Design a Real-Time Recommendation System | Candidate Generation (Two-Tower models/Embeddings), Ranking (XGBoost/Deep Learning), Re-ranking, cold-start handling. |
| [GAP-SYS-04] | Design a Real-Time Fraud Detection System | Streaming data pipelines (Kafka), Feature Stores, low-latency scoring (<50ms), concept drift monitoring. |
| [GAP-SYS-03] | Design an Enterprise RAG Search System | Ingestion pipeline, async embedding generation, vector DB scaling, access control (RBAC), multi-tenant isolation, latency SLAs. |

---

## 11. Interview Execution, Python Coding & Strategy

| Pattern ID | Topic Name | Core Focus & Key Syntax / Interview Questions |
| :--- | :--- | :--- |
|🟢 **[GAP-PY-01]** | **Pandas & Data Vectorization** | **Core dataframe manipulation (merge, groupby, apply, pivot_table), handling missing data, and replacing iterative loops with efficient vectorization.** |
| [GAP-INT-01] | Python Data Structures & Whiteboarding | Dictionary/hashmap manipulation, list comprehensions, string parsing, sliding windows, and lightweight algorithmic puzzles. |
| [GAP-INT-02] | Product Sense, Metrics & Root Cause Analysis | Systematically diagnosing metric drops (e.g., "DAU dropped 10%"), defining primary/guardrail metrics, product tradeoff frameworks. |
| [GAP-INT-03] | Behavioral Framing & Narrative Crafting | Structuring past projects/gap story using STAR framework, handling "Tell me about yourself", framing self-directed execution as a strength. |