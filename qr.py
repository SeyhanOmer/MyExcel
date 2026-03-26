from pathlib import Path
import re

import pandas as pd
import qrcode


INPUT_FILE = "normal.xlsx"
OUTPUT_FILE = "cikti_qr.xlsx"
SOURCE_COLUMN = "A"
OUTPUT_DIR = "qr"
RESULT_COLUMN_NAME = "qr_file"


def sanitize_filename(value: str, max_length: int = 80) -> str:
    """
    hücredeki bilgiye göre anlaml ıve doğru dosyaadı oluşturuyoruz.
    """
    value = str(value).strip()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"\s+", "_", value)
    return value[:max_length] if value else "empty"


def create_qr(data: str, output_path: Path) -> None:
    """
    QR kodu oluşturup resmini alalım
    """
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)


def main() -> None:
    input_path = Path(INPUT_FILE)
    output_path = Path(OUTPUT_FILE)
    qr_dir = Path(OUTPUT_DIR)

    if not input_path.exists():
        raise FileNotFoundError(f"dosya yok: {INPUT_FILE}")

    qr_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_excel(input_path)

    if SOURCE_COLUMN not in df.columns and SOURCE_COLUMN != "A":
        raise ValueError(
            f"kolon: '{SOURCE_COLUMN}' yok "
            f"gerçek bir kolon adı yaz"
        )

    # eğer excel kolon adı bilinmiyorsa A ile başla
    if SOURCE_COLUMN == "A":
        source_series = df.iloc[:, 0]
    else:
        source_series = df[SOURCE_COLUMN]

    qr_files = []

    for index, value in source_series.items():
        if pd.isna(value):
            qr_files.append("")
            continue

        text = str(value).strip()
        if not text:
            qr_files.append("")
            continue

        safe_name = sanitize_filename(text)
        file_name = f"row_{index + 2}_{safe_name}.png"
        file_path = qr_dir / file_name

        create_qr(text, file_path)
        qr_files.append(str(file_path))

    df[RESULT_COLUMN_NAME] = qr_files
    df.to_excel(output_path, index=False)

    print(f"bitti-QR resmi burada: {qr_dir}")
    print(f"Excel dosyasıda burada: {output_path}")


if __name__ == "__main__":
    main()
