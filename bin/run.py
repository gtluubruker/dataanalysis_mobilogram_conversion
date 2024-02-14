import os
import argparse
import numpy as np
import pandas as pd
from pyTDFSDK.init_tdf_sdk import init_tdf_sdk_api
from pyTDFSDK.tims import tims_oneoverk0_to_ccs_for_mz


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        help='File path for .xyz file exported from Bruker DataAnalysis heatmap.',
                        required=True,
                        type=str)
    parser.add_argument('--outdir',
                        help='Path to folder in which to write output .xy file. Default = same as input path.',
                        default='',
                        type=str)
    parser.add_argument('--outfile',
                        help='User defined filename for output .xy file.',
                        default='',
                        type=str)
    parser.add_argument('--charge',
                        help='Assumed charge to be used for 1/K0 -> CCS conversion. Default = 1.',
                        default=1,
                        type=int)
    parser.add_argument('--decimals',
                        help='Number of decimal places to round CCS values to.',
                        default=1,
                        type=int)
    parser.add_argument('--include_header',
                        help='Include header in output .xy file.',
                        action='store_true')
    arguments = parser.parse_args()
    return vars(arguments)


def run():
    # Parse arguments.
    args = get_args()

    # Set output directory to default if not specified.
    if args['outdir'] == '':
        args['outdir'] = os.path.split(args['input'])[0]

    if args['outfile'] == '':
        args['outfile'] = os.path.splitext(os.path.split(args['input'])[1])[0]

    # Initialize TDF-SDK API.
    dll = init_tdf_sdk_api()

    # Read in heatmap exported from Bruker DataAnalysis.
    heatmap_df = pd.read_table(args['input'], sep=' ', names=['ook0', 'mz', 'intensity'])

    # Convert 1/K0 to CCS with assumed charge value.
    heatmap_df['ccs'] = [tims_oneoverk0_to_ccs_for_mz(dll, ook0=row['ook0'], charge=args['charge'], mz=row['mz'])
                         for index, row in heatmap_df.iterrows()]

    # Get df/table with 2 columns: rounded CCS value and intensity.
    heatmap_df = heatmap_df[['ccs', 'intensity']]
    heatmap_df = heatmap_df.round({'ccs': args['decimals']})
    # Aggregate duplicate rounded CCS values.
    heatmap_df = heatmap_df.groupby('ccs', as_index=False).aggregate('sum')

    # Write out .xy file.
    heatmap_df.to_csv(os.path.join(args['outdir'], args['outfile'] + '_converted.xy'),
                      sep=' ',
                      index=False,
                      header=args['include_header'])


if __name__ == '__main__':
    run()
