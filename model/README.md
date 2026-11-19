# Model availability

The trained nnU-Net v2 model for **enamel, dentin, and pulp-cavity segmentation in ex vivo micro-CT images** is available upon reasonable request for academic and research purposes.

Contact: **[simaichen413@gmail.com](mailto:simaichen413@gmail.com)**. Please briefly describe your research purpose when requesting access.

The weights are supplied as `Dataset413_model.zip`, a standard nnU-Net v2 model export. Install the received archive directly:

```bash
nnUNetv2_install_pretrained_model_from_zip /path/to/Dataset413_model.zip
```

The model uses dataset ID `413`, `3d_fullres`, `nnUNetTrainer`, and Fold `0`.
