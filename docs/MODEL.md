# Model details

## Intended application

Three-dimensional multiclass segmentation of **enamel, dentin, and pulp cavity** in ex vivo micro-CT images of teeth, using nnU-Net v2. This model segments tissue compartments within a tooth, rather than assigning a tooth identity in the full dentition.

## Configuration

| Parameter | Value |
|---|---|
| Dataset | `Dataset413_microctbycsm` |
| Dataset ID | `413` |
| Input channel | CT (`_0000.nii.gz`) |
| Trainer | `nnUNetTrainer` |
| Configuration | `3d_fullres` |
| Plans | `nnUNetPlans` |
| Available fold | 0 |
| Network | `PlainConvUNet` (3D) |
| Preprocessing target spacing (mm) | 0.041862, 0.041811, 0.041854 |
| Patch size (voxels) | [160, 112, 128] |
| Dataset entries in the exported metadata | 100 |
| Internal validation cases in Fold 0 | 20 |

The target spacing above is taken from the **model's preprocessing plans**; it is not a statement that every original scan used that acquisition voxel size.

## Weights

The pretrained checkpoint is available upon reasonable request for academic and research purposes. Contact **[simaichen413@gmail.com](mailto:simaichen413@gmail.com)**.

The original nnU-Net export uses the following model directory inside the ZIP:

```text
Dataset413_microctbycsm/
└── nnUNetTrainer__nnUNetPlans__3d_fullres/
    ├── dataset.json
    ├── plans.json
    └── fold_0/
        └── checkpoint_final.pth
```

Additional training information and validation results may be present in the archive; nnU-Net's ZIP installer handles the directory structure.

## Labels and evaluation

See [labels](LABELS.md) and [internal validation](VALIDATION.md). Detailed label metrics are available in `metadata/validation_by_label.csv`.

## Framework citation

Isensee F, Jaeger PF, Kohl SAA, Petersen J, Maier-Hein KH. nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. *Nature Methods*. 2021;18:203–211. https://doi.org/10.1038/s41592-020-01008-z
