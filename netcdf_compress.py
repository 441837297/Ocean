import xarray as xr
import os
import sys
import argparse

def compress_nc(input_path, output_path, complevel):
    """
    压缩单个NetCDF文件
    """
    with xr.open_dataset(input_path) as src:
        src.to_netcdf(output_path, encoding={var: {'zlib': True, 'complevel': complevel} for var in src.variables})
    print(f"Compressed {input_path} to {output_path} with compression level {complevel}")

def process_directory(input_dir, output_dir, complevel):
    """
    处理目录中的所有NetCDF文件
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.nc'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            compress_nc(input_path, output_path, complevel)

def main():
    parser = argparse.ArgumentParser(description="Compress NetCDF files.")
    parser.add_argument("input", help="Input file or directory")
    parser.add_argument("output", help="Output file or directory")
    parser.add_argument("-c", "--complevel", type=int, default=5, choices=range(1, 10),
                        help="Compression level (1-9, default: 5)")
    args = parser.parse_args()

    if os.path.isfile(args.input):
        # 处理单个文件
        if not args.output.endswith('.nc'):
            print("Error: When input is a file, output must be a .nc file")
            sys.exit(1)
        compress_nc(args.input, args.output, args.complevel)
    elif os.path.isdir(args.input):
        # 处理目录
        process_directory(args.input, args.output, args.complevel)
    else:
        print("Error: Input must be a file or directory")
        sys.exit(1)

if __name__ == "__main__":
    main()
