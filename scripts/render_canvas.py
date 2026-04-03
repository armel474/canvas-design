#!/usr/bin/env python3
"""
render_canvas.py — Utilitaire de rendu canvas pour le skill canvas-design.

Usage:
    python render_canvas.py --help
    python render_canvas.py --output /path/to/output.png --width 2400 --height 3200
    python render_canvas.py --output /path/to/output.pdf --width 2400 --height 3200

Ce script initialise un canvas Pillow avec les dimensions spécifiées et retourne
le chemin du fichier de sortie. Il sert de point d'entrée pour les scripts de
rendu générés dynamiquement par Manus.

Polices disponibles : voir templates/fonts/ dans le répertoire du skill.
"""

import argparse
import os
import sys
from pathlib import Path

FONTS_DIR = Path(__file__).parent.parent / "templates" / "fonts"
SUPPORTED_FORMATS = {".png", ".pdf"}


def list_fonts():
    """Liste toutes les polices disponibles dans templates/fonts/."""
    fonts = sorted(FONTS_DIR.glob("*.ttf"))
    if not fonts:
        print("Aucune police trouvée dans templates/fonts/")
        return
    print(f"Polices disponibles ({len(fonts)}) :")
    for f in fonts:
        print(f"  {f.name}")


def get_font_path(font_name: str) -> str:
    """Retourne le chemin absolu d'une police par son nom de fichier (sans extension)."""
    # Cherche d'abord le nom exact
    exact = FONTS_DIR / f"{font_name}.ttf"
    if exact.exists():
        return str(exact)
    # Cherche de manière insensible à la casse
    for f in FONTS_DIR.glob("*.ttf"):
        if f.stem.lower() == font_name.lower():
            return str(f)
    raise FileNotFoundError(
        f"Police '{font_name}' introuvable dans {FONTS_DIR}. "
        f"Utilisez --list-fonts pour voir les polices disponibles."
    )


def create_canvas(output_path: str, width: int = 2400, height: int = 3200):
    """
    Crée un canvas Pillow blanc aux dimensions données et sauvegarde en PNG ou PDF.
    Retourne le chemin absolu du fichier créé.
    """
    try:
        from PIL import Image
    except ImportError:
        print("Pillow non installé. Exécutez : sudo pip3 install pillow", file=sys.stderr)
        sys.exit(1)

    output = Path(output_path)
    suffix = output.suffix.lower()

    if suffix not in SUPPORTED_FORMATS:
        print(f"Format non supporté : {suffix}. Utilisez .png ou .pdf", file=sys.stderr)
        sys.exit(1)

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas = Image.new("RGB", (width, height), color=(255, 255, 255))

    if suffix == ".pdf":
        canvas.save(str(output), "PDF", resolution=300)
    else:
        canvas.save(str(output), "PNG")

    print(f"Canvas créé : {output.resolve()} ({width}x{height})")
    return str(output.resolve())


def main():
    parser = argparse.ArgumentParser(
        description="Utilitaire de rendu canvas pour le skill canvas-design Manus."
    )
    parser.add_argument("--output", "-o", help="Chemin du fichier de sortie (.png ou .pdf)")
    parser.add_argument("--width", type=int, default=2400, help="Largeur en pixels (défaut: 2400)")
    parser.add_argument("--height", type=int, default=3200, help="Hauteur en pixels (défaut: 3200)")
    parser.add_argument("--list-fonts", action="store_true", help="Lister les polices disponibles")
    parser.add_argument("--get-font", metavar="NOM", help="Retourner le chemin d'une police")

    args = parser.parse_args()

    if args.list_fonts:
        list_fonts()
        return

    if args.get_font:
        try:
            path = get_font_path(args.get_font)
            print(path)
        except FileNotFoundError as e:
            print(str(e), file=sys.stderr)
            sys.exit(1)
        return

    if not args.output:
        parser.print_help()
        sys.exit(0)

    create_canvas(args.output, args.width, args.height)


if __name__ == "__main__":
    main()
