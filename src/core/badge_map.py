# Maps skill/tool names to shields.io badge image URLs.
# Badge style tokens like `flat-square` can be replaced at render time via the theme.

BADGE_MAP: dict[str, str] = {
    # ── Languages ──────────────────────────────────────────────────────────────
    "Python":       "https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white",
    "JavaScript":   "https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black",
    "TypeScript":   "https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white",
    "C#":           "https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white",
    "C++":          "https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white",
    "C":            "https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black",
    "Java":         "https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white",
    "Kotlin":       "https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white",
    "Go":           "https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white",
    "Rust":         "https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white",
    "Swift":        "https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white",
    "PHP":          "https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white",
    "Ruby":         "https://img.shields.io/badge/Ruby-CC342D?style=flat-square&logo=ruby&logoColor=white",
    "R":            "https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white",
    "Scala":        "https://img.shields.io/badge/Scala-DC322F?style=flat-square&logo=scala&logoColor=white",
    "Dart":         "https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white",
    "Lua":          "https://img.shields.io/badge/Lua-2C2D72?style=flat-square&logo=lua&logoColor=white",
    "GDScript":     "https://img.shields.io/badge/GDScript-478CBF?style=flat-square&logo=godotengine&logoColor=white",
    "HTML":         "https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white",
    "CSS":          "https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white",
    "SQL":          "https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white",
    "Shell":        "https://img.shields.io/badge/Shell-121011?style=flat-square&logo=gnubash&logoColor=white",
    "PowerShell":   "https://img.shields.io/badge/PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white",

    # ── Game Engines / 3D ──────────────────────────────────────────────────────
    "Unity":          "https://img.shields.io/badge/Unity-FFFFFF?style=flat-square&logo=unity&logoColor=black",
    "Unreal Engine":  "https://img.shields.io/badge/Unreal-0E1128?style=flat-square&logo=unrealengine&logoColor=white",
    "Godot":          "https://img.shields.io/badge/Godot-478CBF?style=flat-square&logo=godotengine&logoColor=white",
    "Blender":        "https://img.shields.io/badge/Blender-E87D0D?style=flat-square&logo=blender&logoColor=white",
    "Three.js":       "https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=threedotjs&logoColor=white",

    # ── AI / ML ────────────────────────────────────────────────────────────────
    "TensorFlow":      "https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white",
    "PyTorch":         "https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white",
    "Stable Diffusion":"https://img.shields.io/badge/Stable%20Diffusion-FF6B35?style=flat-square&logoColor=white",
    "Hugging Face":    "https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black",
    "OpenAI":          "https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white",
    "LangChain":       "https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white",
    "MCP":             "https://img.shields.io/badge/MCP-000000?style=flat-square&logo=anthropic&logoColor=white",
    "scikit-learn":    "https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white",
    "pandas":          "https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white",
    "NumPy":           "https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white",
    "OpenCV":          "https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white",

    # ── Web Frameworks ─────────────────────────────────────────────────────────
    "React":    "https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB",
    "Vue.js":   "https://img.shields.io/badge/Vue.js-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white",
    "Angular":  "https://img.shields.io/badge/Angular-DD0031?style=flat-square&logo=angular&logoColor=white",
    "Next.js":  "https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white",
    "Node.js":  "https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white",
    "Express":  "https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white",
    "Django":   "https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white",
    "FastAPI":  "https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white",
    "Flask":    "https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white",
    "Spring":   "https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=spring&logoColor=white",
    "Flutter":  "https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white",

    # ── DevOps / Cloud ─────────────────────────────────────────────────────────
    "Docker":          "https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white",
    "Kubernetes":      "https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white",
    "Git":             "https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white",
    "GitHub Actions":  "https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white",
    "AWS":             "https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white",
    "Azure":           "https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white",
    "GCP":             "https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white",
    "Linux":           "https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black",

    # ── Databases ──────────────────────────────────────────────────────────────
    "PostgreSQL": "https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white",
    "MySQL":      "https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white",
    "MongoDB":    "https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white",
    "Redis":      "https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white",
    "SQLite":     "https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white",

    # ── Robotics / Embedded ────────────────────────────────────────────────────
    "ROS 2":        "https://img.shields.io/badge/ROS%202-22314E?style=flat-square&logo=ros&logoColor=white",
    "Raspberry Pi": "https://img.shields.io/badge/Raspberry%20Pi-A22846?style=flat-square&logo=raspberrypi&logoColor=white",
    "STM32":        "https://img.shields.io/badge/STM32-03234B?style=flat-square&logo=stmicroelectronics&logoColor=white",
    "Arduino":      "https://img.shields.io/badge/Arduino-00979D?style=flat-square&logo=arduino&logoColor=white",

    # ── Design / Other ─────────────────────────────────────────────────────────
    "Photoshop": "https://img.shields.io/badge/Photoshop-31A8FF?style=flat-square&logo=adobephotoshop&logoColor=white",
    "Figma":     "https://img.shields.io/badge/Figma-F24E1E?style=flat-square&logo=figma&logoColor=white",
    "Ethereum":  "https://img.shields.io/badge/Ethereum-3C3C3D?style=flat-square&logo=ethereum&logoColor=white",
    "Solidity":  "https://img.shields.io/badge/Solidity-363636?style=flat-square&logo=solidity&logoColor=white",
}
