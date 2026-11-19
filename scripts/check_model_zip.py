#!/usr/bin/env python3
"""Verify the nnU-Net Dataset413_microctbycsm model ZIP before installation."""
from __future__ import annotations
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

PREFIX = 'Dataset413_microctbycsm/nnUNetTrainer__nnUNetPlans__3d_fullres/'
REQUIRED = [PREFIX + x for x in ('dataset.json', 'plans.json', 'fold_0/checkpoint_final.pth')]


def main() -> int:
    parser = argparse.ArgumentParser(description='Check the ex vivo tooth micro-CT nnU-Net model archive')
    parser.add_argument('archive', type=Path, help='Path to a received nnU-Net model ZIP')
    parser.add_argument('--full', action='store_true', help='Verify ZIP member CRCs (slower)')
    parser.add_argument('--sha256', help='Optional known SHA-256 checksum of the received ZIP')
    args = parser.parse_args()

    digest = hashlib.sha256()
    with args.archive.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    observed = digest.hexdigest()
    print('SHA-256:', observed)
    if args.sha256 and observed.lower() != args.sha256.lower():
        raise SystemExit('SHA-256 checksum mismatch')

    with zipfile.ZipFile(args.archive) as archive:
        missing = sorted(set(REQUIRED) - set(archive.namelist()))
        if missing:
            raise SystemExit('Missing required model files: ' + ', '.join(missing))
        dataset = json.loads(archive.read(PREFIX + 'dataset.json'))
        plans = json.loads(archive.read(PREFIX + 'plans.json'))
        expected_labels = {'background': 0, 'pulp_cavity': 1, 'enamel': 2, 'dentin': 3}
        if dataset.get('labels') != expected_labels:
            raise SystemExit('Unexpected label mapping in model archive')
        if '3d_fullres' not in plans.get('configurations', {}):
            raise SystemExit('3d_fullres configuration is missing')
        if args.full:
            failed = archive.testzip()
            if failed:
                raise SystemExit('ZIP integrity check failed for: ' + failed)
    print('OK: model ZIP has the required nnU-Net structure and four label definitions')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
