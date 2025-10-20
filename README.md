# Stolen Words

**A Forensic Analysis of Editorial Transformation**

*A Forensic Analysis of Bhagavad-gītā As It Is*

## Overview

This repository contains the complete source files for "Stolen Words," a comprehensive forensic analysis documenting systematic editorial changes in spiritual texts. The investigation reveals how 541 out of 700 verses (77%) in one of the world's most influential spiritual texts have been systematically altered, fundamentally redirecting readers toward entirely different spiritual conclusions.

## Repository Contents

### Main Files
- `manuscript.org` - Complete book source in Org-mode format (244 pages)
- `manuscript.tex` - LaTeX compiled version 
- `manuscript.pdf` - Final 244-page book
- `bg.html` - Original 1972 Bhagavad-gita source for comparison

### Supporting Files
- `cc-by-nc-nd.png` - Creative Commons license image
- `latex_6x9_amazon.org` - LaTeX template documentation for 6x9 Amazon KDP format
- `manual.org` - Practical Application Guide (Appendix F content)

## Book Specifications

- **Format**: 6×9 inch (Amazon KDP standard)
- **Pages**: 244 pages
- **Typography**: Professional layout with Times font, microtype optimization
- **License**: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0
- **Publication**: First Edition: October 2025

## Key Features

### Forensic Analysis
- 541 out of 700 verses systematically altered (77%)
- Comprehensive documentation of verse 3.43 transformation: "control the lower self by the higher self" → "steady the mind by deliberate spiritual intelligence [Kṛṣṇa consciousness]"
- Analysis of "forgotten soul" vs "forgetful soul" paradigm shift in purports
- Mathematical documentation eliminating random editorial patterns

### Literary Structure (Umberto Eco Style)
1. **Maya's Story** - The investigative discovery
2. **The Discovery** - Finding the textual alterations  
3. **The Monk's Journey** - Historical context of original creation
4. **Two Different Souls** - Analysis of consciousness programming
5. **The Forensic Evidence** - Systematic documentation of changes
6. **The Language of the Heart** - Impact on spiritual development

### Appendices
- Complete verse analysis
- Theological terms redefined
- Editorial timeline
- Statistical references
- Practical application guide
- Comprehensive glossary

## Technical Details

### LaTeX Configuration
- Custom 6×9 inch page layout
- Professional typography with microtype
- Fancy headers with "Stolen Words" branding
- Automatic page numbering (including chapter pages)
- Optimized hyphenation and line breaking

### Compilation
The book compiles successfully using Emacs Org-mode export:
```bash
/Applications/Emacs.app/Contents/MacOS/Emacs --batch --no-init-file --load ~/.emacs.d/init.el --visit manuscript.org --funcall org-latex-export-to-pdf
```

Or using standard pdfLaTeX:
```bash
pdflatex manuscript.tex
```

## Author Information

**CENTROS DE BHAKTI YOGA**
Research Team
CIF G-76660679

## License

This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.

## Version Information

**Current Version**: v1.2 (October 20, 2025)

See [VERSION.md](VERSION.md) for complete version history and roadmap.

### Quick Version Summary

- **v1.2 (Current)** - Complete 244-page manuscript with Umberto Eco literary style
  - Three-part narrative structure with fictional framework
  - Comprehensive documentation of 541 altered verses (77%)
  - Professional LaTeX formatting for Amazon KDP
  - Complete bibliography, glossary, and methodology sections

- **v2.0 (Planned)** - Major structural revisions based on reader assessment
  - Tighten mid-book sections for better reader retention
  - Reduce repetition and technical density
  - Enhance narrative flow while maintaining scholarly rigor
  - See VERSION.md for complete roadmap

### Version Numbering

Following semantic versioning:
- **Major (X.0.0)**: Structural changes, major rewrites
- **Minor (1.X.0)**: Content improvements, moderate edits
- **Patch (1.2.X)**: Typo fixes, small corrections

---

*Dedicated to all sincere spiritual seekers who value authentic spiritual transmission over institutional convenience.*