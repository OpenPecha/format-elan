from format_elan.export_elan import get_tsv
from pathlib import Path

input_path = "./tests/export_elan/data/input_elan.eaf"
expected_out = Path("./tests/export_elan/data/expected_output.txt").read_text(encoding="utf-8")

def test_get_tsv():
    output_tsv = get_tsv(input_path)
    assert output_tsv == expected_out

if __name__ == "__main__":
    test_get_tsv()