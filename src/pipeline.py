import argparse
import sys
from download_data import download_data
from clean_data import clean_data
from analyze_data import analyze_data

def main():
    parser = argparse.ArgumentParser(description="Formula 1 Lap Times Evolution Analysis Pipeline")
    parser.add_argument('--download', action='store_true', help="Download data")
    parser.add_argument('--clean', action='store_true', help="Clean data")
    parser.add_argument('--analyze', action='store_true', help="Analyze data")
    
    # To handle Jupyter notebook arguments
    if 'ipykernel_launcher' in sys.argv[0]:
        sys.argv = sys.argv[:1]
    
    args = parser.parse_args()
    
    if args.download:
        download_data()
    if args.clean:
        clean_data()
    if args.analyze:
        analyze_data()

if __name__ == "__main__":
    main()

