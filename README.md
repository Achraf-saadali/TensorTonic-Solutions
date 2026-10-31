# TensorTonic Solutions

Welcome to my TensorTonic solutions repository!

Here you'll find my solutions to various machine learning and deep learning problems from [TensorTonic](https://tensortonic.com).

## What is TensorTonic?

TensorTonic is a platform where you can implement core algorithms of Machine Learning from scratch.

This repository contains my personal solutions to these problems, automatically synchronized from the platform.

<!-- tensortonic:start -->
# ACHRAF SAADALI's TensorTonic Solutions

Verified machine learning implementations completed on [TensorTonic](https://www.tensortonic.com).

<p align="center">
  <img src="https://www.tensortonic.com/api/badge/achraf.svg" alt="TensorTonic Verified Solutions" width="100%" />
</p>

| Problem | Description | Link |
|---|---|---|
| Implement Cosine Similarity | Implement cosine similarity from scratch with NumPy. Covers dot products, Euclidean norms and zero-vector handling, with tests in the browser. | https://www.tensortonic.com/problems/cosine-similarity |
| Implement Cross-Entropy Loss | Compute multiclass cross-entropy loss from class probabilities and integer labels with stable logarithms. | https://www.tensortonic.com/problems/cross-entropy-loss |
| Implement Dot Product | Implement the dot product of equal-length numeric vectors by summing element-wise products without library shortcuts. | https://www.tensortonic.com/problems/dot-product |
| Calculate Eigenvalues of a Matrix | Calculate the eigenvalues of a square matrix and return them in the format required by the numerical contract. | https://www.tensortonic.com/problems/eigenvalues |
| Implement Euclidean Distance | Compute Euclidean distance between equal-length NumPy vectors as the square root of summed squared differences. | https://www.tensortonic.com/problems/euclidean-distance |
| Implement GELU Activation (Gaussian Error Linear Unit) | Implement the exact Gaussian Error Linear Unit activation element-wise with the erf function, with the formula and tests in the browser. | https://www.tensortonic.com/problems/gelu |
| Implement Gradient Descent for a 1D Quadratic | Optimize a one-dimensional quadratic with iterative gradient descent and return the parameter trajectory. | https://www.tensortonic.com/problems/gradient-descent-quadratic |
| Implement Huber Loss | Compute Huber loss with quadratic errors near zero and linear penalties beyond a configurable threshold. | https://www.tensortonic.com/problems/huber-loss |
| Implement Leaky ReLU (with α) | Apply Leaky ReLU element-wise with a configurable negative slope while retaining positive inputs. | https://www.tensortonic.com/problems/leaky-relu |
| Linear Regression Closed Form | Fit linear regression with the closed-form normal equation and return coefficients for the supplied design matrix. | https://www.tensortonic.com/problems/linear-regression-closed-form |
| Logistic Regression Training Loop | Train binary logistic regression in NumPy using sigmoid probabilities, gradient descent, and learned weight and bias parameters. | https://www.tensortonic.com/problems/logistic-regression-training |
| Matrix Factorization SGD Step | Perform one matrix-factorization SGD update for a rated user-item pair with latent factors and regularization. | https://www.tensortonic.com/problems/matrix-factorization-sgd-step |
| Matrix Inverse | Compute a square matrix inverse in NumPy while returning no result for invalid, non-square, or singular inputs. | https://www.tensortonic.com/problems/matrix-inverse |
| Implement Matrix Normalization | Normalize a NumPy matrix using the specified axis and norm while safely handling zero-magnitude slices. | https://www.tensortonic.com/problems/matrix-normalization |
| Matrix Trace | Compute the trace of a square matrix by summing its main diagonal entries without changing the input. | https://www.tensortonic.com/problems/matrix-trace |
| Matrix Transpose | Implement matrix transpose in NumPy without built-in transpose helpers, preserving rectangular shapes and the original input. | https://www.tensortonic.com/problems/matrix-transpose |
| Missing Value Imputation | Impute missing numeric values with column-wise mean, median, or most-frequent statistics while preserving observed values. | https://www.tensortonic.com/problems/ml-imputation |
| Linear Regression from Scratch | Train linear regression from scratch with mean squared error gradients for weights and bias. | https://www.tensortonic.com/problems/ml-linear-regression-from-scratch |
| Logistic Regression from Scratch | Train binary logistic regression from scratch using sigmoid probabilities, cross-entropy gradients, and gradient descent. | https://www.tensortonic.com/problems/ml-logistic-regression |
| Ridge Regression | Train Ridge regression with gradient descent, L2-regularized weights, and an unregularized bias term. | https://www.tensortonic.com/problems/ml-ridge-regression |
| Model Versioning | Select a production model by highest accuracy, then lower latency, then the most recent timestamp. | https://www.tensortonic.com/problems/model-versioning-basics |
| Bag of Words | Build an alphabetical vocabulary and document-term count matrix from a corpus of tokenized documents. | https://www.tensortonic.com/problems/nlp-bag-of-words |
| Padding and Truncation | Pad or truncate integer token sequences to a fixed length with configurable padding value and alignment direction. | https://www.tensortonic.com/problems/nlp-padding-truncation |
| Regex Patterns for NLP | Implement Regex Patterns for NLP, and return the list of matched strings in order of appearance. | https://www.tensortonic.com/problems/nlp-regex-patterns |
| Stemming vs Lemmatization | Produce a rule-based stem and dictionary-backed lemma for a supplied word with deterministic fallback behavior. | https://www.tensortonic.com/problems/nlp-stemming-lemmatization |
| Text Normalization | Normalize text by applying an ordered pipeline of lowercase, punctuation, whitespace, digit, and accent transformations. | https://www.tensortonic.com/problems/nlp-text-normalization |
| TF-IDF | Build a vocabulary V sorted alphabetically and compute the TF-IDF score for every term in every document. | https://www.tensortonic.com/problems/nlp-tfidf |
| Tokenization | Tokenize raw text by scanning characters into words, punctuation marks, and supported special token forms. | https://www.tensortonic.com/problems/nlp-tokenization |
| Fancy Indexing | Convert the data to float64 and return the array formed by selecting elements along that axis using integer array indexing. | https://www.tensortonic.com/problems/numpy-fancy-indexing |
| Normalize Columns | Standardize each NumPy matrix column by subtracting its mean and dividing by its population standard deviation. | https://www.tensortonic.com/problems/numpy-normalize-columns |
| Sort and Argsort | Return NumPy values sorted along a selected axis together with the indices that produce the same ordering. | https://www.tensortonic.com/problems/numpy-sort-argsort |
| One-Hot Encoding (Multi-class) | Convert multiclass integer labels into a NumPy one-hot matrix with one active column per sample. | https://www.tensortonic.com/problems/one-hot-encoding |
| Aggregation Functions | Implement Aggregation Functions, and return a dict mapping each function name to a dict of group label to aggregated value. | https://www.tensortonic.com/problems/pandas-aggregation-functions |
| Change Data Types | Create a DataFrame, convert the specified column to the target type, and return the dtypes before and after conversion. | https://www.tensortonic.com/problems/pandas-change-dtypes |
| Concatenate DataFrames | Concatenate multiple pandas DataFrames vertically and return the combined records with a reset index. | https://www.tensortonic.com/problems/pandas-concatenate-dataframes |
| Drop Duplicates | Create a DataFrame, remove duplicate rows, and return the cleaned result along with counts of rows before and after deduplication. | https://www.tensortonic.com/problems/pandas-drop-duplicates |
| GroupBy Basics | Create a DataFrame and compute the sum, mean, and count of the value column for each group. | https://www.tensortonic.com/problems/pandas-groupby-basics |
| Handle Missing Values | Create a pandas DataFrame, count missing entries per column, and replace every null with a supplied fill value. | https://www.tensortonic.com/problems/pandas-handle-missing |
| Merge DataFrames | Use two dictionaries of column data and a key column present in both, create two DataFrames and merge them on the key column using a specified join type. | https://www.tensortonic.com/problems/pandas-merge-dataframes |
| Multi-Level GroupBy | Create a DataFrame, group by all specified columns, apply the aggregation, and return the result as a flat table. | https://www.tensortonic.com/problems/pandas-multi-level-groupby |
| Pivot Tables | Build a pandas pivot table with selected index, columns, values, aggregation, and zero-filled missing combinations. | https://www.tensortonic.com/problems/pandas-pivot-tables |
| Replace Values | Create a DataFrame, replace all occurrences of the old value with the new value in the specified column, and count how many replacements were made. | https://www.tensortonic.com/problems/pandas-replace-values |
| Resetting Index | Set a pandas column as the index, then restore the default integer index while retaining the original values. | https://www.tensortonic.com/problems/pandas-resetting-index |
| Setting Index | Set a named pandas DataFrame column as the index and report the resulting records and index metadata. | https://www.tensortonic.com/problems/pandas-setting-index |
| PCA Projection | Project centered observations onto supplied principal components to produce lower-dimensional features. | https://www.tensortonic.com/problems/pca-projection |
| Percent Change | Compute period-over-period percentage changes in a numeric time series with defined initial-value handling. | https://www.tensortonic.com/problems/percent-change |
| Implement ReLU Activation | Apply the ReLU activation element-wise by replacing negative values with zero and preserving nonnegative inputs. | https://www.tensortonic.com/problems/relu-activation |
| Implement Sigmoid in NumPy | Implement a vectorized sigmoid activation in NumPy for scalars, lists, vectors, and matrices, including large positive and negative inputs. | https://www.tensortonic.com/problems/sigmoid-numpy |
| Implement Softmax Function | Implement numerically stable softmax by shifting logits before exponentiation and normalizing probabilities. | https://www.tensortonic.com/problems/softmax-function |
| One-Sample t-Test | Compute a one-sample t-statistic in NumPy using the sample mean, Bessel-corrected deviation, and hypothesized mean. | https://www.tensortonic.com/problems/t-test-one-sample |
| Xavier Initialization | Scale raw weights into the Xavier uniform range using a bound derived from fan-in and fan-out. | https://www.tensortonic.com/problems/xavier-initialization |

View my verified ML profile: [TensorTonic profile](https://www.tensortonic.com/profile/achraf)
<!-- tensortonic:end -->
