# Enzo Juhel - Portfolio

This is a high-performance, statically generated portfolio built using [Eleventy (11ty)](https://www.11ty.dev/). The visual design rigorously follows the [GNOME Human Interface Guidelines (HIG)](https://developer.gnome.org/hig/) and Libadwaita patterns, delivering a responsive, clean, and app-like experience complete with native Day/Night modes.

## Getting Started

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Run a local development server:**
   ```bash
   npx @11ty/eleventy --serve
   ```
   This will build the site to the `_site` directory and start a hot-reloading server, usually at `http://localhost:8080`.

## Managing Content

This portfolio utilizes a data-driven architecture to make adding and updating content as seamless as possible without touching complex layout code.

### 1. How to Add or Edit a Case Study

Case studies are powered by a central JSON manifest and individual markdown files.

**Step 1: Define the metadata**
Open `src/_data/cases.json` and add a new entry. For example:
```json
{
  "slug": "new-project",
  "title": "My Awesome Project",
  "summary": "A brief one-sentence description.",
  "date": "01/01/2026 - Present"
}
```
*Note: The `date` field will automatically be parsed and rendered as a split "Start" and "End" box. You can separate dates using commas, hyphens, or en-dashes (`-` or `–`).*

**Step 2: Add the detailed Markdown write-up**
Create a new folder matching the `slug` you defined above, and place a `content.md` file inside it:
```bash
mkdir -p src/assets/cases/new-project
touch src/assets/cases/new-project/content.md
```
Write your full case study in this `content.md` file (using standard Markdown for headers, lists, paragraphs, etc.). Eleventy will automatically parse it and inject it directly into the modal for that case study when clicked.

### 2. How to Update the CV (Résumé)

The "View Résumé (PDF)" button in the hero section points to a specific asset path. 

To update your CV, simply replace the file located at:
```text
src/assets/cv/CV - Enzo Juhel.pdf
```

If you need to change the filename entirely (for example, to `resume_enzo_juhel_2026.pdf`), you must also update the link inside `src/index.njk`. Open `src/index.njk` and modify the `href` attribute in the Hero section:
```html
<a href="/assets/cv/resume_enzo_juhel_2026.pdf" target="_blank" class="button primary pill">View Résumé (PDF)</a>
```

*(Note: Eleventy is configured to automatically copy the entire `src/assets/` directory to the final build, so any PDFs or images placed there will be served correctly.)*
