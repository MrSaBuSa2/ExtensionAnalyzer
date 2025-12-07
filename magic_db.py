MAGIC_SIGNATURES = {
    # Images
    b"\xFF\xD8\xFF": "JPEG image",
    b"\x89PNG\r\n\x1A\n": "PNG image",
    b"GIF87a": "GIF image",
    b"GIF89a": "GIF image",
    b"BM": "Bitmap image (BMP)",
    b"\x49\x49\x2A\x00": "TIFF image (LE)",
    b"\x4D\x4D\x00\x2A": "TIFF image (BE)",

    # Video
    b"\x00\x00\x00\x18ftyp": "MP4 video",
    b"\x1A\x45\xDF\xA3": "MKV / WebM container",
    b"RIFF": "RIFF container (AVI/WAV distinction needed)",

    # Audio
    b"ID3": "MP3 (ID3 tagged)",
    b"\xFF\xFB": "MP3 (raw)",
    b"fLaC": "FLAC audio",
    b"OggS": "OGG audio container",

    # Archives
    b"PK\x03\x04": "ZIP archive (ZIP/DOCX/XLSX/PPTX/APK)",
    b"Rar!\x1A\x07\x00": "RAR archive v1",
    b"Rar!\x1A\x07\x01\x00": "RAR archive v5",
    b"\x1F\x8B": "GZIP compressed file",
    b"7z\xBC\xAF'\x1C": "7-Zip archive",

    # Documents
    b"%PDF": "PDF document",
    b"\xD0\xCF\x11\xE0": "OLE2 container (DOC/XLS/PPT anciens)",
    b"{\\rtf": "RTF document",

    # Executables
    b"MZ": "PE executable (Windows EXE/DLL)",
    b"\x7FELF": "ELF executable",
    b"\xCF\xFA\xED\xFE": "Mach-O 64-bit executable",
    b"\xCE\xFA\xED\xFE": "Mach-O 32-bit executable",
    b"\xCA\xFE\xBA\xBE": "Mach-O fat binary",

    # Databases
    b"SQLite format 3\x00": "SQLite database",

    # Scripts / text
    b"#!/bin/bash": "Bash script",
    b"#!/usr/bin/env python": "Python script",
    b"<?xml": "XML document",
    b"<!DOCTYPE html": "HTML document",
}
