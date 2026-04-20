# Stratford PAL — Website Rebuild

A modern, fully redesigned website for the Stratford Police Athletic League (stratfordpal.org).

---

## How to Run

This is a **static HTML/CSS/JS site** — no build tools, no framework, no server required.

### Option 1: Open directly
Open `index.html` in any web browser. All pages work via file:// protocol.

### Option 2: Local dev server (recommended for full link testing)
If you have Python installed:
```
python -m http.server 8000
```
Then open: http://localhost:8000

Or with Node/npx:
```
npx serve .
```

---

## Project Structure

```
stratfordpal/
├── index.html            ← Home page
├── about.html            ← About Us
├── programs.html         ← All Programs (9 programs)
├── events.html           ← Events & Calendar
├── scholarships.html     ← Scholarships & Financial Assistance
├── get-involved.html     ← Get Involved (Volunteer/Donate/Sponsor)
├── contact.html          ← Contact Us
│
├── css/
│   └── styles.css        ← Full design system + all page styles
│
├── js/
│   └── main.js           ← Navigation, animations, forms
│
├── assets/
│   └── images/           ← (placeholder for downloaded images)
│
├── data/
│   ├── programs.json     ← Structured program data (9 programs)
│   └── events.json       ← Structured event/calendar data
│
└── content/
    ├── analysis.md       ← Current site analysis (strengths/weaknesses)
    ├── sitemap.md        ← Site architecture & page outlines
    └── design-system.md  ← Full design system documentation
```

---

## Pages

| Page | File | Status |
|------|------|--------|
| Home | index.html | ✅ Complete |
| About | about.html | ✅ Complete |
| Programs | programs.html | ✅ Complete (9 programs) |
| Events | events.html | ✅ Complete |
| Scholarships | scholarships.html | ✅ Complete |
| Get Involved | get-involved.html | ✅ Complete |
| Contact | contact.html | ✅ Complete |

---

## Key Features

- **Mobile-first responsive design** — works on all screen sizes
- **Sticky nav** with scroll effect and mobile hamburger menu
- **Program filter** on programs page (by category)
- **FAQ accordion** on scholarships page
- **Scroll animations** on all major sections
- **Counter animations** for stats
- **Contact form** with success state
- **Consistent design system** — colors, typography, spacing tokens in CSS custom properties
- **All assets local** — no external dependencies except Google Fonts

---

## Content Sources

All content extracted directly from the live site at stratfordpal.org:
- **Contact:** 203-385-4146 | spal@townofstratford.com
- **Address:** 900 Longbrook Avenue, Stratford, CT 06614
- **Staff:** Lt. Kevin Albohn (Executive Director), Ofc. Jose Dias (Director)
- **Social:** facebook.com/stratfordpal | instagram.com/stratford_p.a.l.
- **Donation:** donorbox.org/stratford-pal-donations
- **Volunteer form:** Google Forms (embedded link)

---

## External Links Preserved

- Donation: https://donorbox.org/stratford-pal-donations
- Volunteer application: https://docs.google.com/forms/d/e/1FAIpQLSexzMQw8GGF9QR-0dC2WvcNEvJoCclQll_2JktCxaUYVaYPPg/viewform
- Facebook: https://www.facebook.com/stratfordpal
- Instagram: https://www.instagram.com/stratford_p.a.l.

---

## Design Decisions

1. **Navy + Gold palette** — trust/authority (navy) + community energy (gold)
2. **Montserrat headings + Inter body** — modern, readable, accessible
3. **Card layouts throughout** — replaces long text blocks from original site
4. **All 7 pages built** — original site had 404 errors on Contact, Events, Scholarships, Get Involved
5. **Program filter** on programs page for discoverability
6. **FAQ accordion** on scholarships for concise info delivery
7. **Hero visual panel** on homepage shows programs at a glance
8. **Announcement banner** for time-sensitive info (Chess Club, registration dates)
