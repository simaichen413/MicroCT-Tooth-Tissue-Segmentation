# Segmentation labels

The model generates a single-channel **integer label map**, with each voxel classified into one of four mutually exclusive categories.

| Numeric label | Original `dataset.json` label | Anatomical structure |
|---:|---|---|
| `0` | `background` | Background |
| `1` | `pulp_cavity` | Pulp cavity |
| `2` | `enamel` | Enamel |
| `3` | `dentin` | Dentin |