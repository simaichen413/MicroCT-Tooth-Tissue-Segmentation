# Installation and inference

## Environment

Install a suitable PyTorch environment and nnU-Net v2:

```bash
pip install nnunetv2
```

Set a writable model results directory (macOS/Linux):

```bash
export nnUNet_results="$HOME/nnUNet_results"
mkdir -p "$nnUNet_results"
```

For Windows PowerShell:

```powershell
$env:nnUNet_results = "$HOME\nnUNet_results"
New-Item -ItemType Directory -Force $env:nnUNet_results
```

## Obtain and install the model

The pretrained model is available upon reasonable request for academic and research purposes. Contact **[simaichen413@gmail.com](mailto:simaichen413@gmail.com)** with a brief description of the intended use.

The model package is a standard nnU-Net ZIP export named `Dataset413_model.zip`. The ZIP can be installed directly without manually extracting or rearranging its internal folders:

```bash
nnUNetv2_install_pretrained_model_from_zip /path/to/Dataset413_model.zip
```

To inspect an archive before installation, use the included checking script:

```bash
python scripts/check_model_zip.py /path/to/Dataset413_model.zip --full
```

## Input file layout

One input CT channel is expected; suffix each case ID with `_0000`:

```text
imagesTs/
├── tooth001_0000.nii.gz
└── tooth002_0000.nii.gz
```

Ensure the source micro-CT volume has correct physical spacing and orientation metadata. The trained configuration uses a target resampling spacing of approximately 0.0418 mm, handled by nnU-Net preprocessing.

## Prediction

```bash
nnUNetv2_predict -i ./imagesTs -o ./predictions -d Dataset413_microctbycsm -c 3d_fullres -f 0 -tr nnUNetTrainer
```

For macOS/Linux:

```bash
bash scripts/predict.sh ./imagesTs ./predictions
```

For Windows PowerShell:

```powershell
.\scripts\predict.ps1 -InputDir .\imagesTs -OutputDir .\predictions
```

The full dataset name (`Dataset413_microctbycsm`) selects this model explicitly; this is useful when other nnU-Net models with dataset ID 413 are installed.

Outputs are multiclass masks, one for each case (`tooth001.nii.gz`). The labels are 0 background, 1 pulp cavity, 2 enamel, and 3 dentin. Fold 0 is the available model fold. System RAM and GPU memory requirements depend on original volume dimensions.
