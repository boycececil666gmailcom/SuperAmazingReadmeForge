import os
import sys
import tempfile
import webbrowser
from urllib.parse import quote_plus

import markdown as md_lib
from jinja2 import Environment, FileSystemLoader

from src.core.badge_map import BADGE_MAP
from src.core.config_io import _get_base_dir, load_theme
from src.core.schema import ProfileConfig


def _get_sections_dir() -> str:
    return os.path.join(_get_base_dir(), "templates", "sections")


def render_readme(config: ProfileConfig) -> str:
    theme = load_theme(config.theme)
    env = Environment(
        loader=FileSystemLoader(_get_sections_dir()),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    style_social = theme.get("badge_style_social", "for-the-badge")

    socials = []
    if config.socials.github:
        socials.append({
            "label": "GitHub",
            "badge_url": f"https://img.shields.io/badge/GitHub-181717?style={style_social}&logo=github&logoColor=white",
            "url": f"https://github.com/{config.socials.github}",
        })
    if config.socials.linkedin:
        socials.append({
            "label": "LinkedIn",
            "badge_url": f"https://img.shields.io/badge/LinkedIn-0A66C2?style={style_social}&logo=linkedin&logoColor=white",
            "url": config.socials.linkedin,
        })
    if config.socials.email:
        socials.append({
            "label": "Email",
            "badge_url": f"https://img.shields.io/badge/Email-D14836?style={style_social}&logo=gmail&logoColor=white",
            "url": f"mailto:{config.socials.email}",
        })
    if config.socials.twitter:
        socials.append({
            "label": "Twitter",
            "badge_url": f"https://img.shields.io/badge/Twitter-1DA1F2?style={style_social}&logo=twitter&logoColor=white",
            "url": config.socials.twitter,
        })

    taglines_encoded = ";".join(quote_plus(t) for t in config.taglines)

    ctx = {
        "config": config,
        "theme": theme,
        "github_username": config.github_username,
        "taglines_encoded": taglines_encoded,
        "socials": socials,
        "about_text": config.about,
        "tier1": config.skills.tier1,
        "tier2": config.skills.tier2,
        "tier3": config.skills.tier3,
        "projects": config.projects,
        "background": config.background,
        "footer_text": config.footer_text,
        "badge_map": BADGE_MAP,
    }

    parts = []
    for section in config.sections:
        tmpl_name = f"{section}.md.j2"
        try:
            tmpl = env.get_template(tmpl_name)
            parts.append(tmpl.render(**ctx))
        except Exception:
            pass

    return "\n".join(parts)


def preview_in_browser(markdown_content: str) -> None:
    html_body = md_lib.markdown(
        markdown_content,
        extensions=["tables", "fenced_code", "nl2br"],
    )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>README Preview</title>
  <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown-dark.min.css">
  <style>
    body {{
      box-sizing: border-box;
      min-width: 200px;
      max-width: 980px;
      margin: 0 auto;
      padding: 45px;
    }}
    @media (max-width: 767px) {{ body {{ padding: 15px; }} }}
  </style>
</head>
<body class="markdown-body">
{html_body}
</body>
</html>"""

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", delete=False, encoding="utf-8"
    ) as f:
        f.write(html)
        tmp_path = f.name

    webbrowser.open(f"file:///{tmp_path.replace(os.sep, '/')}")
