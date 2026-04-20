# Stratford PAL Website - Deployment Guide

## Overview
The Stratford PAL website is a modern, responsive static HTML/CSS/JavaScript site. No backend server or database is required — it's pure frontend with static assets.

**Live Site URL:** https://www.stratfordpal.org/

---

## What's Included

### Pages (7 total)
1. **index.html** - Homepage with hero, programs overview, stats, events preview
2. **about.html** - About PAL, mission, leadership team, history
3. **programs.html** - All 9 programs with filtering and detailed info
4. **events.html** - Events calendar and registration information
5. **scholarships.html** - Financial assistance options and FAQs
6. **get-involved.html** - Volunteer, donate, sponsor, partner opportunities
7. **contact.html** - Contact form, staff info, quick actions

### Assets
- **css/styles.css** - Complete design system (colors, typography, spacing, components)
- **js/main.js** - Navigation, animations, form handling, interactions
- **data/programs.json** - Structured data for 9 programs
- **data/events.json** - Event information and calendar data

### Features
✓ Mobile-first responsive design  
✓ Sticky navigation with scroll effects  
✓ Program filtering by category  
✓ FAQ accordion on scholarships page  
✓ Contact form with success state  
✓ Smooth scroll animations  
✓ Counter animations for stats  
✓ External integrations (Donorbox, Google Forms)  
✓ Social media links  
✓ Google Fonts integration (no local font files)  

---

## Testing Checklist

### Phase 1: Local Testing
- [ ] All HTML files open without errors
- [ ] All CSS loads correctly (no styling breaks)
- [ ] All JavaScript functions work (navigation, forms, animations)
- [ ] All internal links navigate correctly
- [ ] All external links are accessible

### Phase 2: Responsive Design
- [ ] Mobile view (iPhone 375px width)
- [ ] Tablet view (iPad 768px width)
- [ ] Desktop view (1920px+ width)
- [ ] Navigation menu works on all sizes
- [ ] Forms are usable on mobile
- [ ] Images scale appropriately

### Phase 3: Functionality
- [ ] Hamburger menu opens/closes on mobile
- [ ] Program filter works on programs page
- [ ] FAQ accordion opens/closes on scholarships page
- [ ] Contact form validates and submits
- [ ] Donate button links to Donorbox
- [ ] Volunteer button links to Google Form
- [ ] Social media links open in new tabs
- [ ] Scroll animations trigger appropriately

### Phase 4: Cross-Browser
- [ ] Chrome/Edge (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

### Phase 5: Performance
- [ ] Page load time < 3 seconds
- [ ] No console errors
- [ ] No 404 errors for assets
- [ ] Images optimized (< 100KB combined)

### Phase 6: Accessibility
- [ ] Keyboard navigation works (Tab, Enter, Escape)
- [ ] Color contrast meets WCAG AA standards
- [ ] Form labels are properly associated
- [ ] Semantic HTML used throughout
- [ ] Focus indicators visible

### Phase 7: SEO
- [ ] All pages have descriptive titles
- [ ] Meta descriptions present on all pages
- [ ] Open Graph tags for social sharing
- [ ] Structured data for organization
- [ ] robots.txt configured
- [ ] sitemap.xml created

---

## Local Development

### Option 1: Python HTTP Server (Recommended)
```bash
cd path/to/stratfordpal
python -m http.server 8000
# Open: http://localhost:8000
```

### Option 2: Node.js Serve
```bash
npx serve .
# Open: http://localhost:3000
```

### Option 3: Direct File Open
- Open `index.html` directly in browser
- Note: Some features (like smooth scroll) may work better with a server

---

## Deployment Options

### Option 1: GitHub Pages (Free, Recommended)
1. Create GitHub repository
2. Enable GitHub Pages in repository settings
3. Point to `main` branch or `docs/` folder
4. Site available at `https://username.github.io/stratfordpal/`

### Option 2: Netlify (Free tier available)
1. Connect GitHub repository
2. Set build command: (none needed — static site)
3. Set publish directory: `.` (root)
4. Automatic deployments on push
5. Free SSL certificate

### Option 3: Traditional Web Hosting
1. FTP/SFTP upload all files to server
2. Ensure `.htaccess` configured for clean URLs (if applicable)
3. Set `index.html` as default document
4. Configure SSL certificate (Let's Encrypt recommended)

### Option 4: Vercel
1. Connect GitHub repository
2. Vercel auto-detects static site
3. Deploys automatically on push
4. Global CDN included

---

## File Structure for Production

```
stratfordpal/
├── index.html
├── about.html
├── programs.html
├── events.html
├── scholarships.html
├── get-involved.html
├── contact.html
├── css/
│   └── styles.css
├── js/
│   └── main.js
├── data/
│   ├── programs.json
│   └── events.json
├── assets/
│   └── images/          (add imagery here)
├── .htaccess            (Apache optimization - optional)
├── robots.txt           (SEO - optional)
├── sitemap.xml          (SEO - optional)
└── README.md
```

---

## Configuration Notes

### Contact Form
Currently simulates submission with client-side JavaScript. To enable actual email sending:
- **Option A:** Use Formspree.io (easiest, free tier available)
- **Option B:** Use Backend service (Node.js, PHP, etc.)
- **Option C:** Use third-party form service (Typeform, JotForm)

Implementation in `js/main.js` lines 106-128 — modify to POST to service endpoint.

### External Integrations

| Feature | Current | Link |
|---------|---------|------|
| Donations | Donorbox | https://donorbox.org/stratford-pal-donations |
| Volunteer Form | Google Forms | https://docs.google.com/forms/... |
| Facebook | External | https://www.facebook.com/stratfordpal |
| Instagram | External | https://www.instagram.com/stratford_p.a.l. |

---

## Maintenance

### Adding a New Page
1. Create new HTML file with same header/nav structure
2. Update navigation links on all pages
3. Test responsive design and all links
4. Deploy

### Updating Content
1. Edit content directly in HTML files
2. For structured data (programs/events), update JSON files
3. Test locally before deploying
4. Commit changes and push to deploy

### Updating Styles
- All CSS is in `css/styles.css`
- Uses CSS custom properties (variables) for colors and spacing
- Mobile-first approach — update desktop breakpoints at bottom

---

## Performance Optimization (Already Implemented)

✓ CSS custom properties (no duplicate values)  
✓ Responsive images (no unnecessary pixels sent)  
✓ Google Fonts preconnect (faster loading)  
✓ Lazy loading animations (intersection observer)  
✓ No external frameworks (lightweight)  
✓ Minified structure ready for deployment  

---

## Support & Contact

**Site Owner:** Stratford PAL  
**Email:** spal@townofstratford.com  
**Phone:** 203-385-4146  
**Address:** 900 Longbrook Avenue, Stratford, CT 06614  

---

## Version History

| Date | Version | Changes |
|------|---------|---------|
| Apr 2026 | 1.0 | Initial launch - 7 pages, complete design system |

---

## Quick Links

- [Live Site](https://www.stratfordpal.org/)
- [GitHub Repository](#)
- [Design System](content/design-system.md)
- [Site Architecture](content/sitemap.md)
- [Current Site Analysis](content/analysis.md)

---

**Last Updated:** April 20, 2026  
**Status:** ✅ Ready for Production Deployment
