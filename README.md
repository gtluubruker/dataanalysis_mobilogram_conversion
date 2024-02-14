# dataanalysis_mobilogram_conversion

This Python script allows for users to convert a table containing 1/K0 - intensity pairs to a table of collisional cross 
section (CCS) - intensity pairs from TIMS-MS data acquired on the Bruker timsTOF. The output can be used to plot CCS vs 
intensity in your plotting environment of choice.

#### macOS IS NOT SUPPORTED!

Bruker's TDF-SDK is currently only compatible with Windows and Linux.

## Installation

This script has been tested using a conda virtual environment. While other virtual environments or setups may function, 
there is no guarantee that the script will be compatible with other environments. Instructions to reproduce the 
environment used during development are below.

1. If not installed, install Anaconda from [here](https://www.anaconda.com/download).

2. Open `Anaconda Prompt`.

3. Create a new conda virtual environment:
```
conda create -n timstof_targeted_3d_maldi_analysis python=3.11
```

4. Activate the venv:
```
conda activate timstof_targeted_3d_maldi_analysis
```

5. Install this package:
```
pip install git+https://github.com/gtluubruker/dataanalysis_mobilogram_conversion
```

## Usage

## In Bruker DataAnalysis 6.1

Please note that steps may vary slightly in older versions of DataAnalysis.

1. Load a TIMS-MS run into DataAnalysis.
2. In the "Heatmap" window view, right click on the heatmap and select "Export Heatmap..." to export an *.xyz file 
containing the 1/K0, m/z, and intensity values. This will be used as your input.

#### Parameters

`convert_mobilogram`<br>
`--input`: File path for .xyz file exported from Bruker DataAnalysis heatmap.<br>
`--outdir`: Path to folder in whch to write output .xy file. Default = same as input path.<br>
`--outfile`: User defined filename for output .xy file.<br>
`--charge`: Assumed charge to be used for 1/K0 -> CCS conversion. Default = 1.<br>
`--decimals`: Number of decimal places to round CCS values to.<br>
`--include_header`: Include header in output .xy file.<br>

### Example

An array of CCS values can only be obtained by assuming the charge of the features. The default assumption is charge=1.

```
convert_mobilogram --input mobilogram.xyz --charge 1
```
