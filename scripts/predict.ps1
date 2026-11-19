param(
  [Parameter(Mandatory=$true)][string]$InputDir,
  [Parameter(Mandatory=$true)][string]$OutputDir
)
& nnUNetv2_predict -i $InputDir -o $OutputDir -d Dataset413_microctbycsm -c 3d_fullres -f 0 -tr nnUNetTrainer
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
