import os
from docx2pdf import convert
from pathlib import Path
import logging
import argparse
from typing import Union, List
from concurrent.futures import ThreadPoolExecutor
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DocxToPdfConverter:
    def __init__(self):
        self.supported_formats = {'.docx'}

    def _is_valid_file(self, file_path: Union[str, Path]) -> bool:
        """
        Check if the file is valid and has a supported format.

        Args:
            file_path: Path to the file

        Returns:
            bool: True if file is valid, False otherwise
        """
        path = Path(file_path)
        return (
                path.exists() and
                path.is_file() and
                path.suffix.lower() in self.supported_formats
        )

    def _get_output_path(self, input_path: Union[str, Path]) -> Path:
        """
        Generate the output PDF path from the input path.

        Args:
            input_path: Path to the input file

        Returns:
            Path: Path object for the output PDF file
        """
        input_path = Path(input_path)
        return input_path.with_suffix('.pdf')

    def convert_single_file(self, input_path: Union[str, Path]) -> bool:
        """
        Convert a single DOCX file to PDF.

        Args:
            input_path: Path to the input DOCX file

        Returns:
            bool: True if conversion was successful, False otherwise
        """
        input_path = Path(input_path)

        if not self._is_valid_file(input_path):
            logger.error(f"Invalid file: {input_path}")
            return False

        output_path = self._get_output_path(input_path)

        try:
            logger.info(f"Converting: {input_path.name}")
            start_time = time.time()

            # Perform the conversion
            convert(str(input_path), str(output_path))

            duration = time.time() - start_time
            logger.info(f"Converted {input_path.name} to PDF in {duration:.2f} seconds")
            return True

        except Exception as e:
            logger.error(f"Error converting {input_path.name}: {str(e)}")
            return False

    def convert_directory(self, directory_path: Union[str, Path], recursive: bool = False) -> tuple[int, int]:
        """
        Convert all DOCX files in a directory to PDF.

        Args:
            directory_path: Path to the directory
            recursive: Whether to process subdirectories

        Returns:
            tuple: (number of successful conversions, total number of files processed)
        """
        directory_path = Path(directory_path)
        if not directory_path.is_dir():
            logger.error(f"Invalid directory path: {directory_path}")
            return 0, 0

        # Collect all DOCX files
        pattern = '**/*.docx' if recursive else '*.docx'
        docx_files = list(directory_path.glob(pattern))

        if not docx_files:
            logger.info(f"No DOCX files found in {directory_path}")
            return 0, 0

        # Convert files using thread pool
        successful = 0
        total = len(docx_files)

        with ThreadPoolExecutor() as executor:
            results = list(executor.map(self.convert_single_file, docx_files))
            successful = sum(results)

        logger.info(f"Converted {successful} out of {total} files successfully")
        return successful, total


def main():
    parser = argparse.ArgumentParser(description='Convert DOCX files to PDF')
    parser.add_argument('path', help='Path to DOCX file or directory')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Process subdirectories recursively')
    args = parser.parse_args()

    converter = DocxToPdfConverter()
    path = Path(args.path)

    if path.is_file():
        success = converter.convert_single_file(path)
        exit_code = 0 if success else 1
    elif path.is_dir():
        successful, total = converter.convert_directory(path, args.recursive)
        exit_code = 0 if successful == total else 1
    else:
        logger.error(f"Invalid path: {path}")
        exit_code = 1

    return exit_code


if __name__ == "__main__":
    exit(main())