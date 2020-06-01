
# learn_chain_proj_matrix

A function successively learning a projections matrix on the residue of the previous one. The projections
matrices are then concatenated and return as one single projection matrix. Note that the final projection
matrix may not produce fvs of the size the sum of the components of each part, i.e., care must be taken
to ensure each classes called must be able to produce the required number of components. For example,
if the number of classes is 10, then lda can only produce 9 dimensions. To obtain say 12 dimension, the user
will need to chain two lda's, for example with size 9 and 3 respectively.


```python
if pre_projection is not None:
    X = np.dot(X, pre_projection)

all_proj_matrices = []
for mat_dict in chain:
    kwargs_feat = mat_dict['kwargs']
    proj_matrix = learn_spect_proj(X, y,
                                   spectral_proj_name=mat_dict['type'],
                                   kwargs_feat=kwargs_feat)
    all_proj_matrices.append(proj_matrix)
    X = residue(proj_matrix, X)

```
