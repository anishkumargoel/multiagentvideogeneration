from pathlib import Path
import shutil
import subprocess


PROJECT_DIR = Path(__file__).resolve().parent
VIDEO_FILE = PROJECT_DIR / "combined.mp4"
AUDIO_DIR = PROJECT_DIR / "inputaudios"
OUTPUT_FILE = PROJECT_DIR / "with_replaced_audio.mp4"


def find_ffmpeg():
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        return ffmpeg

    package_dir = Path.home() / "AppData/Local/Microsoft/WinGet/Packages"
    candidates = package_dir.glob("**/ffmpeg.exe") if package_dir.exists() else []

    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)

    return None


def main():
    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        raise RuntimeError("FFmpeg was not found. Install FFmpeg and restart VS Code.")

    if not VIDEO_FILE.is_file():
        raise FileNotFoundError(f"Combined video not found: {VIDEO_FILE}")

    audio_files = sorted(
        [
            file
            for file in AUDIO_DIR.iterdir()
            if file.is_file() and file.suffix.lower() in {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg"}
        ]
        if AUDIO_DIR.exists()
        else []
    )

    if not audio_files:
        raise FileNotFoundError(f"No alternate audio file found in: {AUDIO_DIR}")

    audio_file = audio_files[0]
    command = [
        ffmpeg,
        "-hide_banner",
        "-y",
        "-i", str(VIDEO_FILE),
        "-i", str(audio_file),
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        "-movflags", "+faststart",
        str(OUTPUT_FILE),
    ]

    subprocess.run(command, check=True)
    print(f"Replaced the original audio with: {audio_file.name}")
    print(f"Created: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
