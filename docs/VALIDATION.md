# Internal validation

The exported nnU-Net v2 model includes `fold_0/validation/summary.json` with evaluation results for **20 validation cases**.

| Label | Structure | Mean Dice | Mean IoU |
|---:|---|---:|---:|
| 1 | Pulp cavity | 0.952791 | 0.913324 |
| 2 | Enamel | 0.969263 | 0.942905 |
| 3 | Dentin | 0.982726 | 0.966307 |
| — | Foreground mean (three classes) | 0.968260 | 0.940845 |

The foreground mean is the unweighted mean of the three per-class scores in the nnU-Net summary. These scores describe internal Fold 0 validation, not external test performance. The report does not establish reproducibility on other micro-CT scanners or voxel settings.

