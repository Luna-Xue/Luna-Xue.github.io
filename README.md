# Xiaochan Xue - Personal Website

Jekyll-based academic website hosted on GitHub Pages.

## How to Update Content

All content is driven by YAML data files in `_data/` and HTML pages in `pages/`. You rarely need to touch layouts or includes.

### Add News

Edit `_data/news.yml`. Add a new entry at the **top** of the file:

```yaml
- label: paper
  title: "One paper accepted to <strong>VENUE 2026</strong>"
  date: Mar, 2026
```

Labels can be: `paper`, `award`, `job`, `service`, `other`.

### Add a Publication

Edit `_data/projects.yml`. Add a new entry at the **top**:

```yaml
- name: "Paper Title Here"
  date: "2026"
  publish: VENUE 2026
  authors: Author One, <strong>Xiaochan Xue</strong>, Author Two
  details: https://link-to-paper-or-project
  attach:
    - url: "https://arxiv.org/abs/XXXX"
      icon: file
      label: PDF
    - url: "https://github.com/repo"
      icon: github
      label: Code
  cate:
    - "ml_systems"
    - "architecture"
```

Available categories: `ml_systems`, `architecture`, `privacy_ml`, `ml_for_eda`, `gnn`, `cv_nlp`, `llm_agents`, `emerging_tech`.

### Update Team Members

Edit `_data/team.yml`.

**Add a current member** under the appropriate section (`postdoc`, `phd`, or `master`):

```yaml
    - name: New Student
      area: Research Area Description
```

**Move someone to alumni** — remove from `current` and add under `alumni.phd` or `alumni.other`:

```yaml
    - name: Student Name
      year: "2026"
      position: Job Title at Company
```

### Update Other Pages

These pages are plain HTML with Jekyll front matter. Edit directly:

| Page | File |
|------|------|
| Teaching | `pages/teaching/index.html` |
| Projects | `pages/projects/index.html` |
| Awards & Activities | `pages/awards/index.html` |
| Home bio / research areas | `_includes/about.html` |
| Home header (title, subtitle) | `_includes/home_header.html` |
| Navigation links | `_config.yml` → `nav.main` |
| Contact links | `_config.yml` → `contact_urls` |

### Add Images

Place images in `assets/img/`. Reference them in YAML or HTML as `/assets/img/filename.jpg`.

## Test Locally with Docker

```bash
# Build the Docker image (first time only, or after Gemfile changes)
docker build -t jekyll-site .

# Serve the site at http://localhost:4000
docker run --rm -p 4000:4000 -v "$(pwd):/site" jekyll-site
```

Open [http://localhost:4000](http://localhost:4000) in your browser.

## Deploy

Push to the `main` branch. GitHub Pages builds and deploys automatically.

```bash
git add -A
git commit -m "Update content"
git push
```

## File Structure

```
_config.yml          # Site settings, nav, contact info
_data/
  news.yml           # News entries (shown on home + news page)
  projects.yml       # Publications (shown on publications page)
  team.yml           # Team members (shown on team page)
_includes/
  about.html         # Home page bio + news + research areas
  home_header.html   # Home page header (photo, title, links)
  nav.html           # Navigation bar
  project-outline.html  # Publication card template
_layouts/
  default.html       # Base page layout
pages/
  research/          # Publications page
  team/              # Team page
  teaching/          # Teaching page
  projects/          # Projects page
  awards/            # Awards & Activities page
  news/              # Full news page
assets/
  css/               # Stylesheets (SCSS)
  js/                # JavaScript
  fonts/             # Font Awesome
  img/               # Images
index.html           # Home page
Dockerfile           # For local testing
```
