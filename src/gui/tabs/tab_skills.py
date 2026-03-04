import customtkinter as ctk

from src.core.badge_map import BADGE_MAP
from src.core.schema import ProfileConfig

_HINT = (
    "Enter skill names — one per line or comma-separated. "
    "Names must match the Available Skills list below to get auto-badges."
)


class SkillsTab(ctk.CTkFrame):
    def __init__(self, parent, config: ProfileConfig):
        super().__init__(parent, fg_color="transparent")
        self.pack(fill="both", expand=True)
        self._build(config)

    def _build(self, config: ProfileConfig):
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True)
        scroll.columnconfigure(1, weight=1)

        ctk.CTkLabel(
            scroll, text=_HINT, text_color="gray", wraplength=520,
            anchor="w", justify="left"
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        tiers = [
            ("Tier 1 — Primary Focus", "_tier1"),
            ("Tier 2 — Building Experience", "_tier2"),
            ("Tier 3 — Exploring", "_tier3"),
        ]
        for row, (label, attr) in enumerate(tiers, start=1):
            ctk.CTkLabel(scroll, text=label, anchor="w").grid(
                row=row, column=0, sticky="nw", padx=(0, 12), pady=4
            )
            tb = ctk.CTkTextbox(scroll, height=80)
            tb.grid(row=row, column=1, sticky="ew", pady=4)
            setattr(self, attr, tb)

        ctk.CTkLabel(scroll, text="Available Skills", anchor="w", text_color="gray").grid(
            row=4, column=0, sticky="nw", padx=(0, 12), pady=(12, 4)
        )
        available = ctk.CTkTextbox(scroll, height=80)
        available.grid(row=4, column=1, sticky="ew", pady=(12, 4))
        available.insert("1.0", ", ".join(sorted(BADGE_MAP.keys())))
        available.configure(state="disabled")

        self.load_from(config)

    # ── helpers ───────────────────────────────────────────────────────────────

    @staticmethod
    def _set_textbox(tb: ctk.CTkTextbox, value: str) -> None:
        tb.delete("1.0", "end")
        if value:
            tb.insert("1.0", value)

    @staticmethod
    def _parse(tb: ctk.CTkTextbox) -> list[str]:
        raw = tb.get("1.0", "end").strip()
        items = [i.strip() for line in raw.splitlines() for i in line.split(",")]
        return [i for i in items if i]

    # ── public interface ───────────────────────────────────────────────────────

    def load_from(self, config: ProfileConfig) -> None:
        self._set_textbox(self._tier1, "\n".join(config.skills.tier1))
        self._set_textbox(self._tier2, "\n".join(config.skills.tier2))
        self._set_textbox(self._tier3, "\n".join(config.skills.tier3))

    def apply_to(self, config: ProfileConfig) -> None:
        config.skills.tier1 = self._parse(self._tier1)
        config.skills.tier2 = self._parse(self._tier2)
        config.skills.tier3 = self._parse(self._tier3)
