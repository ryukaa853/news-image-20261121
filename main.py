"""Salin gambar front-page koran yang sudah jadi ke direktori output.

Gambar final (entry.png) tinggal di samping file ini di dalam repo.
Tugas program ini cuma satu: menyalin file itu apa adanya ke
direktori tujuan, sehingga setiap run menghasilkan byte yang sama.
Tidak ada gambar yang digambar ulang di sini, tidak ada jaringan,
hanya modul standar Python.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    # Lokasi gambar sumber: satu folder dengan file ini.
    sumber = Path(__file__).resolve().parent / "entry.png"

    # Tujuan mengikuti env MAKEFUN_OUTPUT_DIR, default /output.
    tujuan_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    tujuan_dir.mkdir(parents=True, exist_ok=True)
    tujuan = tujuan_dir / "entry.png"

    # Salin byte demi byte; file hasil identik dengan sumber.
    shutil.copyfile(sumber, tujuan)
    print(f"Disalin: {sumber} -> {tujuan}")


if __name__ == "__main__":
    main()
