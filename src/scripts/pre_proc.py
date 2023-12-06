from os import rename, walk
from os.path import exists
from pathlib import Path
from typing import Optional
from typing_extensions import Self


class PreProcessData:
    def __init__(
            self: Self,
            PATH: Optional[str] = None
        ) -> None:
        """
        Arguments:
            PATH: Optional[str] -> None -- the path of the data.
        """
        self.HOME: str = Path.home()

        self.file_paths: list[str] = [] # list of all datasets
                                        # in the given path
        if PATH is not None:
            self.PATH: str = PATH
        else:
            self.PATH: str = f"{self.HOME}/datasets" # default path of data

    def fetch(self: Self) -> None:
        if not exists(self.PATH):
            return None

        for file in next(walk(self.PATH))[2]:
            if file.endswith("xls"):
                self.file_paths.append(file)
                continue

    def rename_all(self: Self, file_paths: list[str]) -> int:
        """Rename all the files in the given path.

        Returns:
            integer indicating the status of the function.
        """

        for file in file_paths:
            filenames: list[str] = file.split(" ")
            rename(
                f"{self.PATH}/{file}",
                (
                    f"{self.PATH}/"
                    + f"{filenames[0]}_"
                    + filenames[1]
                        .replace('(', '')
                        .replace(')','')
                )
            )

    def clean_data(
            self: Self,
            filenames: list[str],
            exclude: Optional[list[str] | str] = None,
            include: Optional[list[str] | str] = None,
            filename: Optional[str] = None,
            output_path: Optional[str] | None = None
        )  -> int:
        """Remove all of the unnecessary data from the given dataset.

        Arguments:
            filenames: list[str] - array containing all of the filenames
            exclude: list[str] | str | None - data to exclude, default to none.
            include: list[str] | str | None - data to include, default to none.
            filename: str | None - new filename, defaults to none.
            output_path: str | None - location where the processed dataset will
                be output.
        """
        ...
