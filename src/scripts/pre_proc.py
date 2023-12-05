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
        self.HOME: str = Path.home()

        if PATH is not None:
            self.PATH: str = PATH
        else:
            self.PATH: str = f"{self.HOME}/datasets"

    def fetch(PATH: str) -> list[str] | None:
        if not exists(PATH):
            return None

        file_paths: list[str] = []
        for file in next(walk(PATH))[2]:
            if file.endswith("xls"):
                filenames: list[str] = file.split(" ")
                file_paths.append(
                    (
                        f"{filenames[0]}_"
                        + filenames[1]
                            .replace('(', '')
                            .replace(')','')
                    )
                )
                continue

        return file_paths

    def rename_all(self: Self) -> int:
        """Rename all the files in the given path.

        Returns:
            integer indicating the status of the function.
        """
        ...

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
