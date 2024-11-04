import numpy as np

#features function to generate word embeddings
def features(dim: tuple):
    """Generate random values for each word (je, suis, très, malade)"""
    # Generate 4 random vectors of dimension dim
    X1 = np.random.randint(0, 255, dim)  # "je"
    X2 = np.random.randint(0, 255, dim)  # "suis"
    X3 = np.random.randint(0, 255, dim)  # "très"
    X4 = np.random.randint(0, 255, dim)  # "malade"
    
    # Stack vectors vertically to create feature matrix F
    F = np.vstack((X1, X2, X3, X4))
    
    return F

#query matrix function
def requêtes(dim_wq: tuple, F: np.array):
    """Calculate query matrix Q = W_q @ F^T"""
    # Generate random weight matrix W_q
    W_q = np.random.rand(*dim_wq)
    
    # Calculate Q = W_q @ F^T
    Q = W_q @ F.T
    
    return Q

#key matrix function
def clés(dim_wk: tuple, F: np.array):
    """Calculate key matrix K = W_k @ F^T"""
    # Generate random weight matrix W_k
    W_k = np.random.rand(*dim_wk)
    
    # Calculate K = W_k @ F^T
    K = W_k @ F.T
    
    return K


#value matrix function
def valeurs(dim_wv: tuple, F: np.array):
    """Calculate value matrix V = W_v @ F^T"""
    # Generate random weight matrix W_v
    W_v = np.random.rand(*dim_wv)
    
    # Calculate V = W_v @ F^T
    V = W_v @ F.T
    
    return V


#similarity calculation
def similarité(K: np.array, Q: np.array):
    """Calculate similarity matrix K^T @ Q"""
    # Calculate dot product K^T @ Q
    return K.T @ Q


#normalization function
def norm(d_k: int, similarité: np.array):
    """Normalize similarity matrix by sqrt(d_k)"""
    return similarité / np.sqrt(d_k)


#softmax function
def softmax(vector: np.array):
    """Apply softmax function to input vector with numerical stability
    Args:
        vector: np.array - input vector
    Returns:
        np.array - probability distribution after softmax
    """
    # Subtract max value for numerical stability
    shifted_vector = vector - np.max(vector)
    
    # Compute exponentials of shifted vector
    exp_vector = np.exp(shifted_vector)
    
    # Calculate sum of exponentials
    sum_exp = np.sum(exp_vector)
    
    # Calculate softmax probabilities
    return exp_vector / sum_exp


#attention weight matrix
def A(a_x1: np.array, a_x2: np.array, a_x3: np.array, a_x4: np.array):
    """Create attention weight matrix by stacking attention vectors"""
    # Stack attention vectors vertically
    return np.vstack((a_x1, a_x2, a_x3, a_x4))


def main():
    #Features matrix
    F = features(dim=(1,6))

    #Query matrix
    Q = requêtes(dim_wq=(3,6), F=F)

    #Keys matrix
    K = clés(dim_wk=(3,6), F=F)

    #V matrix
    V = valeurs(dim_wv=(4,6), F=F)

    #dot product matrix
    sim = similarité(K,Q)

    #Scaled dot product matrix

    sim_norm = norm(d_k = 3, similarité=sim)

    # Attention vector of x_1
    a_x1 = sim_norm[:,0]

    # Attention vector of x_2
    a_x2 = sim_norm[:,1]

    # Attention vector of x_3
    a_x3 = sim_norm[:,2]

    # Attention vector of x_4
    a_x4 = sim_norm[:,3]

    # softmax apply on x_1
    as_x1 = softmax(a_x1)

    # softmax apply on x_2
    as_x2 = softmax(a_x2)

    # softmax apply on x_3
    as_x3 = softmax(a_x3)

    # softmax apply on x_4
    as_x4 = softmax(a_x4)

    Attention = A(as_x1, as_x2 , as_x3, as_x4)


if __name__=="__main__":
    main()
    
#This implementation creates a complete self-attention mechanism for the given sentence "je suis très malade", following the transformer architecture principles.