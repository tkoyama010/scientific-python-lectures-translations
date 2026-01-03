"""
Download scikit-learn datasets for Read the Docs builds.

This script pre-downloads datasets to avoid HTTP 403 errors during
sphinx-gallery execution in the RTD build environment.
"""

import urllib.request
from pathlib import Path


def download():
    """Download required scikit-learn datasets."""
    # Set data directory relative to project root
    data_home = Path(__file__).parent / "scikit_learn_data"
    data_home.mkdir(exist_ok=True)

    print(f"Downloading datasets to {data_home.absolute()}...")

    # Override urllib User-Agent to avoid 403 errors
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-agent", "Mozilla/5.0")]
    urllib.request.install_opener(opener)

    # Import after setting up opener
    from sklearn.datasets import fetch_california_housing, fetch_olivetti_faces

    try:
        # California Housing dataset
        print("Downloading California Housing dataset...")
        fetch_california_housing(data_home=str(data_home), download_if_missing=True)
        print("✓ Successfully downloaded: California Housing")

        # Olivetti Faces dataset
        print("Downloading Olivetti Faces dataset...")
        fetch_olivetti_faces(data_home=str(data_home), download_if_missing=True)
        print("✓ Successfully downloaded: Olivetti Faces")

        print("\nAll datasets downloaded successfully!")

    except Exception as e:
        print(f"Error during download: {e}")
        # Re-raise to fail the build if downloads fail
        raise


if __name__ == "__main__":
    download()
