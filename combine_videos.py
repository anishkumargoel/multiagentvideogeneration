from pathlib import Path
import re
import shutil
import subprocess
import sys


INPUT_DIR = Path(__file__).resolve().parent / "inputvideos"
OUTPUT_FILE = Path(__file__).resolve().parent / "combined.mp4"


def natural_sort_key(path: Path):
    match = re.search(r"P(\d+)$", path.stem, re.IGNORECASE)
    number = int(match.group(1)) if match else sys.maxsize
    return (number, path.name.lower())


def find_ffmpeg():
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        return ffmpeg

    candidates = [
        Path.home() / "AppData/Local/Microsoft/WinGet/Packages",
        Path("C:/ffmpeg/bin/ffmpeg.exe"),
        Path("C:/Program Files/ffmpeg/bin/ffmpeg.exe"),
    ]

    package_dir = candidates.pop(0)
    if package_dir.exists():
        candidates.extend(package_dir.glob("**/ffmpeg.exe"))

    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)

    return None


def main():
    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        raise RuntimeError("FFmpeg was not found. Restart VS Code and add FFmpeg to PATH.")

    videos = sorted(INPUT_DIR.glob("P*.mp4"), key=natural_sort_key)
    if not videos:
        raise FileNotFoundError(f"No P*.mp4 videos found in {INPUT_DIR}")

    concat_file = INPUT_DIR / "combine_list.txt"
    with concat_file.open("w", encoding="utf-8") as file:
        for video in videos:
            file.write(f"file '{video.as_posix().replace(chr(39), chr(39) * 2)}'\n")

    try:
        command = [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", str(concat_file),
            "-c", "copy",
            str(OUTPUT_FILE),
        ]
        subprocess.run(command, check=True)
        print(f"Combined {len(videos)} videos into: {OUTPUT_FILE}")
    finally:
        concat_file.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
