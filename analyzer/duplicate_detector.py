from collections import defaultdict

from models.file_model import FileRecord


class DuplicateDetector:

    def find_duplicates(
        self,
        files: list[FileRecord]
    ):

        hash_groups = defaultdict(list)

        for file in files:

            if not file.file_hash:
                continue

            hash_groups[file.file_hash].append(file)

        duplicate_groups = []

        for file_hash, group in hash_groups.items():

            if len(group) > 1:

                duplicate_groups.append(group)

                for file in group:

                    file.is_duplicate = True
                    file.duplicate_group = file_hash

        return duplicate_groups