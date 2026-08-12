from pathlib import Path

from scanner import FileSystemScanner


def test_scanner_discovers_files(tmp_path):

    file1 = tmp_path / "hello.txt"
    file2 = tmp_path / "data.csv"

    file1.write_text(
        "Hello World",
        encoding="utf-8"
    )

    file2.write_text(
        "name,age\nJohn,25",
        encoding="utf-8"
    )

    scanner = FileSystemScanner(
        calculate_hash=True
    )

    records = scanner.scan(
        str(tmp_path)
    )

    assert len(records) == 2


def test_file_metadata(tmp_path):

    file_path = tmp_path / "test.txt"

    file_path.write_text(
        "Hello",
        encoding="utf-8"
    )

    scanner = FileSystemScanner(
        calculate_hash=True
    )

    records = scanner.scan(
        str(tmp_path)
    )

    record = records[0]

    assert record.name == "test.txt"

    assert record.extension == ".txt"

    assert record.size > 0

    assert record.category == "documents"

    assert record.file_hash is not None


def test_hash_consistency(tmp_path):

    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    content = "same content"

    file1.write_text(
        content,
        encoding="utf-8"
    )

    file2.write_text(
        content,
        encoding="utf-8"
    )

    scanner = FileSystemScanner(
        calculate_hash=True
    )

    records = scanner.scan(
        str(tmp_path)
    )

    hashes = {
        record.file_hash
        for record in records
    }

    assert len(hashes) == 1