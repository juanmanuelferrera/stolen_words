# LaTeX Book Template - Quick Reference Guide

## File Created
`latex_template_6x9_book.org`

## What This Template Provides

### ✅ Professional 6×9 inch Amazon KDP Book Format
- Correct margins meeting Amazon requirements
- Professional typography with Libertinus Serif font
- Ragged right layout (avoids spacing issues)
- Widow/orphan control
- Custom hyphenation dictionary

### ✅ Multiple Page Styles
1. **frontmatter** - For TOC, acknowledgements (page numbers, no headers)
2. **fancy** - Main content (page numbers + headers with book title)
3. **plain** - First pages of sections
4. **chapterpage** - Chapter opening pages
5. **sectionopening** - Section opening pages
6. **none** - Blank pages

### ✅ Professional Typography
- Optimized line spacing (1.08)
- Proper paragraph spacing
- Section heading control
- Microtype optimization for print

## How to Use This Template

### Step 1: Copy Template to New Project
```bash
cp latex_template_6x9_book.org ~/path/to/your/new-book/book.org
```

### Step 2: Customize Basic Info
Edit these lines at the top:
```org
#+TITLE: Your Book Title Here
#+SUBTITLE: Your Subtitle Here
#+Author: Your Name
#+DATE: First Edition, Month Year
```

### Step 3: Customize Running Header
Find this line (around line 95):
```org
#+LATEX_HEADER:   \fancyhead[LE]{\small\textsc{Your Book Title}}%
```
Change "Your Book Title" to your actual book title.

### Step 4: Add Custom Hyphenation Words
Find the hyphenation section and add words specific to your book:
```org
#+LATEX_HEADER: \hyphenation{your-custom-words here}
```

### Step 5: Customize Front Matter
Replace the example front matter (half-title, title page, copyright) with your content.

### Step 6: Add Your Content
Start writing after the `\startmainmatter` command:
```org
#+LATEX: \startmainmatter

* Chapter 1: Your First Chapter
Your text here...
```

## Key Features to Customize

### 1. Book Title in Headers
**Location:** Line ~95
**What to change:** "Your Book Title" → Your actual title
**Why:** Appears on left pages (verso)

### 2. Hyphenation Dictionary
**Location:** Lines 68-69
**What to change:** Add your domain-specific words
**Why:** Prevents bad line breaks

### 3. Colors (Optional)
**Location:** Lines 154-157
**What to change:** RGB values
**Why:** For any colored elements you might add

### 4. Copyright Page
**Location:** Around line 270
**What to change:**
- Copyright year
- Your name
- Your website
- ISBN
- Country

## Chapter and Section Formatting

### Creating Chapters
```org
#+LATEX: \cleardoublepage
#+LATEX: \vspace*{0.20\textheight}
#+LATEX: \section*{1. Chapter Title}
#+LATEX: \addcontentsline{toc}{section}{1. Chapter Title}
#+LATEX: \markright{Chapter Title}
#+LATEX: \thispagestyle{chapterpage}

Your chapter content...
```

### Creating Sections
```org
#+LATEX: \cleardoublepage
#+LATEX: \vspace*{0.15\textheight}
#+LATEX: \section*{Section Name}
#+LATEX: \addcontentsline{toc}{section}{Section Name}
#+LATEX: \markright{Section Name}
#+LATEX: \thispagestyle{sectionopening}

Your section content...
```

### Creating Bold Subheaders
```org
#+LATEX: \vspace{0.5cm}
@@latex:\textbf{Your Subheader}@@
#+LATEX: \vspace{0.2cm}

Your text...
```

## Compilation

### From Emacs
```
C-c C-e l p
```

### From Command Line
```bash
/Applications/Emacs.app/Contents/MacOS/Emacs --batch \
  --no-init-file \
  --load ~/.emacs.d/init.el \
  --visit your-book.org \
  --funcall org-latex-export-to-pdf
```

### From Standard LaTeX
If you export to .tex first:
```bash
xelatex your-book.tex
xelatex your-book.tex  # Run twice for TOC
```

## Page Layout Quick Reference

### Margins (Amazon KDP Compliant)
- Inner (gutter): 15mm (0.59")
- Outer: 10mm (0.39")
- Top: 13mm (0.51")
- Bottom: 13mm (0.51")

### Typography
- Font: Libertinus Serif 12pt
- Line spacing: 1.08
- Paragraph spacing: 4pt
- Layout: Ragged right (not justified)

### Page Numbering
- Front matter: Roman numerals (if enabled)
- Main content: Arabic numerals starting at 1
- Position: Centered at bottom

## Common Customizations

### Change Font
```org
#+LATEX_HEADER: \setmainfont{Your Font Name}
```
Common alternatives:
- Libertinus Serif (default)
- EB Garamond
- Crimson Text
- Linux Libertine

### Adjust Line Spacing
```org
#+LATEX_HEADER: \setstretch{1.15}  % Increase from 1.08
```

### Change to Full Justification
Remove or comment out:
```org
# #+LATEX_HEADER: \RaggedRight
```

### Adjust Margins
Edit the geometry values (lines 15-25):
```org
#+LATEX_HEADER:   inner=18mm,  % Wider gutter
#+LATEX_HEADER:   outer=12mm,  % Wider outside
```

## Troubleshooting

### Headers not showing
Make sure you have:
```org
#+LATEX: \markright{Your Chapter Name}
```

### Page numbers missing
Ensure you called:
```org
#+LATEX: \startmainmatter
```

### Spacing issues
Check that you're using `\vspace{0.5cm}` consistently for subheaders.

### Font not found
Install Libertinus Serif or change to a system font:
```bash
brew install --cask font-libertinus  # macOS
```

## Files Included

1. **latex_template_6x9_book.org** - The reusable template
2. **TEMPLATE_USAGE.md** - This file (usage guide)

## Version History

- **v2.7 (2025-11-08)**: Template extracted from "Stolen Words"
  - Ragged right layout
  - Optimized hyphenation
  - Professional page styles
  - Amazon KDP compliant margins

## Credits

Template created for "Stolen Words" by Br. Jagannatha Mishra Dasa
Optimized through iterative development with Claude Code assistance
Released under same Creative Commons license as the book

## Support

For issues or questions:
1. Check manuscript.org for working examples
2. Review LaTeX logs for specific errors
3. Consult Org-mode LaTeX export documentation

---

**Quick Start Command:**
```bash
cp latex_template_6x9_book.org my-new-book.org
# Edit my-new-book.org with your content
# C-c C-e l p to compile
```
