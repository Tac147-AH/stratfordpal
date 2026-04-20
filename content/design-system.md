# Stratford PAL — Design System

## Brand Identity
**Name:** Stratford PAL — Police Athletic League
**Tagline:** "Inspiring Positive Change" / "Building Confidence, Connection & Opportunity"
**Tone:** Warm · Direct · Community-oriented · Credible · Energetic but not loud

---

## Color Palette

| Token          | Hex       | Usage                              |
|----------------|-----------|------------------------------------|
| `--navy`       | `#1B2A4A` | Primary brand — headers, nav, backgrounds |
| `--navy-dark`  | `#0F1D35` | Deepest navy — hero, footer, CTAs  |
| `--navy-light` | `#253660` | Gradient endpoint, accents         |
| `--gold`       | `#F4A900` | Primary accent — CTAs, highlights, eyebrows |
| `--gold-dark`  | `#D4900A` | Hover state for gold               |
| `--gold-light` | `#FFD166` | Light gold for subtle accents      |
| `--blue`       | `#2563EB` | Links, info badges                 |
| `--white`      | `#FFFFFF` | Background, text on dark           |
| `--off-white`  | `#F7F8FA` | Alternate backgrounds              |
| `--gray-50`    | `#F9FAFB` | Section backgrounds                |
| `--text`       | `#1C2333` | Primary body text                  |
| `--text-light` | `#4B5563` | Secondary text, metadata           |
| `--success`    | `#16A34A` | Checkmarks, success states, green badges |

**Color Meaning:**
- Navy = Trust, authority, police, stability
- Gold = Community, energy, warmth, youth
- White/Light gray = Openness, clarity, accessibility

---

## Typography

**Heading Font:** Montserrat (700, 800, 900 weights)
- Used for: all headings, nav links, buttons, eyebrows, stats
- Feels: Bold, modern, trustworthy

**Body Font:** Inter (400, 500, 600 weights)
- Used for: all body text, form labels, metadata
- Feels: Clean, readable, professional

**Type Scale:**
- h1: clamp(2rem, 5vw, 3.5rem)
- h2: clamp(1.6rem, 3.5vw, 2.5rem)
- h3: clamp(1.2rem, 2.5vw, 1.6rem)
- h4: 1.2rem
- Body: 1rem / line-height 1.75
- Small: 0.85–0.9rem

**Eyebrow Labels:**
- All-caps, 0.75rem, 0.12em letter-spacing, Montserrat 700
- Gold color on light backgrounds, Gold on dark

---

## Spacing System

Built on a 0.25rem (4px) base unit:
- `--space-1`: 4px
- `--space-2`: 8px
- `--space-3`: 12px
- `--space-4`: 16px
- `--space-5`: 20px
- `--space-6`: 24px
- `--space-8`: 32px
- `--space-10`: 40px
- `--space-12`: 48px
- `--space-16`: 64px
- `--space-20`: 80px
- `--space-24`: 96px

**Section padding:** `var(--space-20)` top and bottom (80px)
**Container max-width:** 1180px

---

## Button System

**Primary (gold):** `.btn-primary`
- Use for: main CTAs ("Explore Programs", "Register", "Donate Now")
- Background: gold | Text: navy-dark | Hover: darker gold

**Navy:** `.btn-navy`
- Use for: secondary actions ("Learn More", "Get Involved")
- Background: navy | Text: white | Hover: darker navy

**Secondary (outline white):** `.btn-secondary`
- Use for: secondary CTAs on dark backgrounds
- Background: transparent | Border: white | Text: white

**Outline:** `.btn-outline`
- Use for: tertiary actions on light backgrounds
- Background: transparent | Border: navy | Text: navy → on hover: navy bg + white text

**Sizes:**
- `.btn-sm`: small (program cards, event rows)
- Default: standard
- `.btn-lg`: large (hero, CTA sections)

**Shape:** `border-radius: 9999px` (fully rounded) for all buttons

---

## Card Components

**Program Card** (`.program-card`)
- White background, subtle border + shadow
- 4px gradient top border on hover (gold → navy-light)
- Lifts on hover (-4px transform)

**Program Full Card** (`.program-full-card`)
- Navy gradient header + meta bar + two-column body
- Used on programs.html for full detail view

**Event Card** (`.event-card`)
- 3-column grid: date block | info | action button
- Date block in navy with gold day number

**Involve Card** (`.involve-card`)
- White background, gold bottom border animation on hover
- Used for Volunteer / Donate / Sponsor / Partner sections

**Staff Card** (`.staff-card`)
- Centered, avatar initial circle in navy/gold gradient
- Soft shadow

---

## Layout Principles

1. **Mobile-first** — styles built for mobile, enhanced for desktop
2. **Container max:** 1180px with 24px side padding (16px mobile)
3. **Grid system:** CSS Grid — 2, 3, 4 columns depending on content type
4. **Section alternation:** White → Gray-50 → Navy → White to create visual rhythm
5. **Card layouts:** Used throughout — no long text-only blocks on any page

---

## Component Inventory

- `nav` — Fixed, transparent → scrolled (navy-dark), mobile hamburger
- `.page-hero` — Inner page hero with breadcrumb + eyebrow + headline
- `.hero` — Full-height homepage hero with split layout
- `.mission-strip` — Gold strip with 5 value icons
- `.eyebrow` — Section label (all-caps, gold, small)
- `.section-header` — Centered section title + subtitle
- `.program-card` — Program grid cards
- `.program-full-card` — Full program detail on programs.html
- `.event-card` / `.event-full-card` — Event listing rows
- `.scholarship-highlight` — Two-column blue box for scholarships
- `.involve-card` — Get involved ways
- `.staff-card` — Team member cards
- `.contact-form` — Styled form container
- `.notice-box` — Gold-tinted info/alert boxes
- `.badge` — Inline category labels
- `.partner-chip` — Rounded partner name pills
- `.footer` — 4-column footer grid
- `.cta-banner` — Navy gradient full-width CTA section

---

## Responsive Breakpoints

- `1024px`: 4-col → 2-col grids; 3-col programs → 2-col
- `900px`: Nav collapses to hamburger; side-by-side → stacked
- `768px`: 2-col → 1-col grids; about/contact sections stack
- `640px`: Mobile card layouts; footer stacks; events simplify
- `480px`: Smallest adjustments for very small screens
