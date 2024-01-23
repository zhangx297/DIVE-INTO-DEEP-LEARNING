import torch 
from d2l import torch as d2l

def show_heatmaps(matrices, xlabel, ylabel, titles=None, figsize=(2.5, 2.5), cmap='Reds'):
    "显示矩阵热图"
    d2l.use_svg_display()
    num_rows, num_cols = matrices.shape[0], matrices.shape[1]
    fig, axes = d2l.plt.subplots(num_rows, num_cols, figsize=figsize, sharex=True, sharey=True, squeeze=False)
    print(fig, "\n", axes)
    for i, (row_axes, row_matrices) in enumerate(zip(axes, matrices)):
        print(i, "\n", row_axes, "\n", row_matrices)
        for j, (ax, matrix) in enumerate(zip(row_axes, row_matrices)):
            print(j, "\n", ax, "\n", matrix)
            pcm = ax.imshow(matrix.detach().numpy(), cmap=cmap)
            print(pcm)
            if i == num_rows - 1:
                ax.set_xlabel(xlabel)
            if j == 0:
                ax.set_ylabel(ylabel)
            if titles:
                ax.set_title(titles[j])
    fig.colorbar(pcm, ax=axes, shrink=0.6)

attention_weights = torch.eye(10).reshape((1, 1, 10, 10)) #生成单位矩阵
print(attention_weights)
show_heatmaps(attention_weights, xlabel='Keys', ylabel='Queries')