---
name: canvas-design
description: "Creation d'oeuvres visuelles originales (posters, affiches, art graphique) en .png ou .pdf haute resolution. Utiliser quand l'utilisateur demande un poster, une affiche, une piece d'art visuel, un design graphique statique, ou toute composition visuelle de qualite professionnelle ou museale. Workflow en deux etapes : (1) philosophie de design en .md, (2) rendu canvas Python/Pillow en .png ou .pdf."
---

# Canvas Design

Créer des œuvres visuelles originales de qualité professionnelle. Output : fichiers `.md` (philosophie), `.png` et/ou `.pdf` (rendu final).

**Workflow en deux étapes obligatoires :**
1. Philosophie de design → fichier `.md`
2. Rendu canvas → fichier `.png` ou `.pdf` via script Python/Pillow

---

## ÉTAPE 1 : PHILOSOPHIE DE DESIGN

Créer une PHILOSOPHIE VISUELLE (pas un layout ou un template) qui sera exprimée à travers :
- Forme, espace, couleur, composition
- Images, graphiques, formes, motifs
- Texte minimal comme accent visuel

### Nommer le mouvement (1-2 mots)
Exemples : "Brutalisme Joyeux", "Silence Chromatique", "Rêves Métabolistes"

### Rédiger la philosophie (4-6 paragraphes)
Exprimer comment la philosophie se manifeste à travers :
- Espace et forme
- Couleur et matière
- Échelle et rythme
- Composition et équilibre
- Hiérarchie visuelle

**Règles critiques :**
- Chaque aspect de design mentionné une seule fois, sans redondance
- Insister **plusieurs fois** sur l'artisanat : "méticuleusement travaillé", "fruit d'une expertise profonde", "attention painstaking", "exécution de maître"
- Laisser de l'espace créatif : spécifique sur la direction esthétique, mais concis pour permettre des choix interprétatifs
- La philosophie guide vers l'expression VISUELLE, pas textuelle

Sauvegarder en `.md`.

---

## ÉTAPE 2 : RENDU CANVAS

### Initialiser le canvas

```bash
python skills/canvas-design/scripts/render_canvas.py --output /chemin/sortie.png --width 2400 --height 3200
```

Formats supportés : `.png` (recommandé), `.pdf` (300 DPI).

### Récupérer une police

```bash
python skills/canvas-design/scripts/render_canvas.py --get-font "Lora-Regular"
# → /home/ubuntu/skills/canvas-design/templates/fonts/Lora-Regular.ttf

python skills/canvas-design/scripts/render_canvas.py --list-fonts
# → Liste complète des 54 polices disponibles
```

### Créer le rendu avec Python/Pillow

Après avoir initialisé le canvas, écrire un script Python complet utilisant `Pillow` (PIL) pour dessiner la composition. Utiliser les polices bundlées dans `templates/fonts/`.

```python
from PIL import Image, ImageDraw, ImageFont

# Charger le canvas de base
img = Image.new("RGB", (2400, 3200), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Charger une police bundlée
font_path = "/home/ubuntu/skills/canvas-design/templates/fonts/Lora-Regular.ttf"
font = ImageFont.truetype(font_path, size=120)

# Dessiner des éléments
draw.rectangle([0, 0, 2400, 3200], fill=(10, 10, 10))
draw.text((200, 400), "TITRE", font=font, fill=(255, 255, 255))

img.save("/chemin/sortie.png", "PNG")
```

### Polices disponibles (54 fichiers .ttf)

| Famille | Variantes disponibles |
|---|---|
| ArsenalSC | Regular |
| BigShoulders | Regular, Bold |
| Boldonse | Regular |
| BricolageGrotesque | Regular, Bold |
| CrimsonPro | Regular, Bold, Italic |
| DMMono | Regular |
| EricaOne | Regular |
| GeistMono | Regular, Bold |
| Gloock | Regular |
| IBMPlexMono | Regular, Bold |
| IBMPlexSerif | Regular, Bold, Italic, BoldItalic |
| InstrumentSans | Regular, Bold, Italic, BoldItalic |
| InstrumentSerif | Regular, Italic |
| Italiana | Regular |
| JetBrainsMono | Regular, Bold |
| Jura | Light, Medium |
| LibreBaskerville | Regular |
| Lora | Regular, Bold, Italic, BoldItalic |
| NationalPark | Regular, Bold |
| NothingYouCouldDo | Regular |
| Outfit | Regular, Bold |
| PixelifySans | Medium |
| PoiretOne | Regular |
| RedHatMono | Regular, Bold |
| Silkscreen | Regular |
| SmoochSans | Medium |
| Tektur | Regular, Medium |
| WorkSans | Regular, Bold, Italic, BoldItalic |
| YoungSerif | Regular |

---

## PRINCIPES DE QUALITÉ

- **90% visuel, 10% texte** : les idées se communiquent par l'espace, la forme, la couleur — pas par des paragraphes
- **Texte minimal et design-forward** : utiliser des polices différentes si plusieurs textes, intégrer la typographie comme élément artistique
- **Artisanat de maître** : la composition finale doit sembler avoir demandé des heures de travail méticuleux
- **Aucun chevauchement** : chaque élément doit avoir de l'espace respiratoire, rien ne déborde des marges
- **Référence subtile** : le sujet est un fil conceptuel discret tissé dans l'œuvre — perceptible par les initiés, apprécié de tous

## ÉTAPE FINALE : SECOND PASSAGE

Après le premier rendu, revenir sur le code et raffiner. Ne pas ajouter de nouveaux éléments graphiques — rendre ce qui existe plus précis, plus crisp, plus philosophiquement cohérent. Se demander : "Comment rendre ce qui est déjà là plus proche d'une œuvre d'art ?"

Livrer : le fichier `.md` de philosophie + le fichier `.png` ou `.pdf` final.
